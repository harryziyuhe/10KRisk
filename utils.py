import requests, json, sys, zipfile, io
import pandas as pd

def set_identity(name):
    identity = {"name": name}
    with open("identity.json", "w") as f:
        json.dump(identity, f, ident = 4)

def load_identity():
    try:
        with open("identity.json", "r") as f:
            identity = json.load(f)
            name = identity["name"]
            return name
    except FileNotFoundError:
        print("Please set identity and then continue.")
        sys.exit()

def get_company_CIK():
    url = "https://storage.googleapis.com/kaggle-data-sets/2471230/7005648/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241010%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241010T161424Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=4840fea971f9bb1693d9118a20810c371a65161847870f7e32e612ea0ab4a26286c9f23d4c1fb08106b74baf0ee2298fb251aedd77ca6c3b548eaafcb0e27db600d5b5b165c812bef52016fc7ffce8b409fee89425ea833eb5b3e82756cdac7cdf057b91ad9ebab8e56000c9baf9d11551c195e5541ad38066911ded416904cc61ef845a53a02c948f88f917bb903c35cedcf26478609586ea44b39dab5e861444daccabe71d57980b19bcbf4ea36bb83d81fe141dc8b5e47979ecde79c6bb5dc9c3f1035f837384a6bc859c031f39cb4dacef4a62f2be8a44698d934504401bedafb6e65a47a7dc93fcd630951c2a0cbbbd759d23f4b92fedc3c03945e03dcb"
    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    for file_name in zip_file.namelist():
        if file_name.endswith('.json'):
            with zip_file.open(file_name) as f:
                CIK_dict = json.load(f)
                CIK_df = pd.DataFrame(CIK_dict['data'], columns = CIK_dict['fields'])
                CIK_df.to_csv("data/company_cik.csv", index = False)
                break

if __name__ == "__main__":
    get_company_CIK()