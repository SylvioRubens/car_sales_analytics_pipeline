from handles.kaggle_handle import KaggleHandle
import json
import os

def download_kagle_dataset(url, file_name, file_path=None):
    # with open("config.json", "r") as file:
    #     key = json.load(file)
        
    if file_path is None:
        file_path = os.getcwd()
            
    kaggle = KaggleHandle()
        
    kaggle.download_dataset_from_url(url=download_link, file_name='teste', file_path=file_path, unzip=True)
    
if __name__=='__main__':
    download_link = 'https://storage.googleapis.com/kaggle-data-sets/3483/5614/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240414%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240414T235205Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=30f6aff00d3650fb3c304499ca40dd9aae5eb9c958cf3945bd0f76c9ecc2c5ea8b54682da8e086d74c9e867527453638d086595e091f22de85fe1662905261996de8842c16b525d26388e6f1eb440432f5bc05c7fb04b77ed9d78823e1c4d7ead6f9ad2fd9c5a067a58e2218dc668426e4df50a3a285e5f9d7f2c071a9838eae8c4de529f6f2c748f5ccd872ab7b7943fc1ab22ae0d2b8bac0448deda68dfe18afe1ca31aaf9c2ea1e3faf4fcf9c4be667d1135bbfeb515f0e4d0a778c74a2fc9f1d02c5ae2aa1b7f6e8c00bb19b2c7108f7ea528e22add95c036a1141489669bd2491976a2d7cb9842f730bf073076d1b0099545bcd03fd6714cba02086cb97'

    download_kagle_dataset(url=download_link, file_name='teste')
    
    