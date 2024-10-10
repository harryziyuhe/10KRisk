import requests, os, warnings
from utils import *
import pandas as pd
from sec_downloader import Downloader
import sec_parser as sp
from tqdm import tqdm


text_elements = ['TextElement', 'TopSectionTitle', 'TitleElement']

def get_records(ticker, cik = None):
    if cik is None:
        cik = get_CIK(ticker)

    endpoint = f"https://data.sec.gov/submissions/CIK{cik}.json"

    headers = {
        "User-Agent": load_identity()
    }

    response = requests.get(endpoint, headers=headers)

    data = response.json()
    accession_numbers = []
    filing_dates = []
    primary_documents = []
    forms = []
    urls = []

    for i, accession_number in enumerate(data['filings']['recent']['accessionNumber']):
        filing_date = data['filings']['recent']['filingDate'][i]
        primary_document = data['filings']['recent']['primaryDocument'][i]
        form = data['filings']['recent']['form'][i]
        document_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number.replace('-', '')}/{primary_document}"

        accession_numbers.append(accession_number)
        filing_dates.append(filing_date)
        primary_documents.append(primary_document)
        forms.append(form)
        urls.append(document_url)

    df_records = pd.DataFrame({
        'accession': accession_numbers,
        'time': filing_dates,
        'primarydoc': primary_documents,
        'form': forms,
        'url': urls
    })

    df_records.to_csv(f"data/records/{ticker}.csv")

def tenktext(ticker):
    if not os.path.exists(f"data/records/{ticker}.csv"):
        get_records(ticker)
    df_records = pd.read_csv(f"data/records/{ticker}.csv")
    
    accession_numbers = []
    filing_dates = []
    contents = []

    dl = Downloader("UCSD", "zih028@ucsd.edu")

    for _, row in tqdm(df_records.iterrows(), total=df_records.shape[0]):
        if row['form'] == "10-K":
            accession_numbers.append(row['accession'])
            filing_dates.append(row['time'])
            html = dl.download_filing(url=row['url']).decode()
            parser = sp.Edgar10QParser()
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", message="Invalid section type for")
                elements: list = parser.parse(html)
            text = ''
            for element in elements:
                if element.__class__.__name__ in text_elements:
                    text = " ".join([text, element.text])
            contents.append(text)

    df_filings = pd.DataFrame({
        'accession': accession_numbers,
        'time': filing_dates,
        'text': contents
    })

    df_filings.to_csv(f"data/filings/{ticker}.csv", index = False)

if __name__ == "__main__":
    get_records("0000789019")
