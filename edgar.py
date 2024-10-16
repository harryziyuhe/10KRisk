import os, sys
from utils import *
from get_tenk import *
import pandas as pd
if __name__ == "__main__":
    #if not os.path.exists("data/company_cik.csv"):
    #    get_company_CIK()
    #try:
    #    with open('ticker_list.txt', 'r') as file:
    #        content = file.read()
    #        tickers = content.split(',')
    #        ticker_list = [ticker.strip() for ticker in tickers]
    #except FileNotFoundError:
    #    print("Error: Ticker file was not found.")
    #    sys.exit()
    #df_CIK = pd.read_csv("data/company_cik.csv")
    #df_CIK['cik'] = df_CIK['cik'].astype(str).str.zfill(10)

    sp500 = pd.read_csv("data/SP500.csv")
    sector = input("Please input the sector for SP500: ")
    companies = sp500.loc[sp500['Sector'] == sector, ]

    for i, company in companies.iterrows():
        cik = str(company['CIK']).zfill(10)
        ticker = company['Ticker']
        if cik is None:
            continue
        if not os.path.exists(f"data/records/{ticker}.csv"):
            print(f"Getting submission records for {ticker} with CIK {cik}")
            get_records(ticker, cik)
        if not os.path.exists(f"data/filings/{ticker}.csv"):
            print(f"Getting 10-K contents for {ticker} with CIK {cik}")
            tenktext(ticker)

    