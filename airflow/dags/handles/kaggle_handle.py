import os
import json
import requests
import zipfile
import time
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleHandle():
    """Class to handle kagle datasets. You can use it to 
    facilitates processes as the authentication, and download data from . 
    """
    def __init__(self, api_credentials_path=None):
        '''Initializes the KaggleHandle class and set the environment variables for authetication on kagle api
        
        Args:
            api_credentials_path (str): path to kaggle api json file with credentials.
        '''
        
        kaggle_username, kaggle_api_key = self.get_api_credentials(path=api_credentials_path)
        
        if kaggle_username and kaggle_api_key: 
            
            # Setting the environment variables for kaggle api authentication
            os.environ['KAGGLE_USERNAME'] = kaggle_username
            os.environ['KAGGLE_API_KEY'] = kaggle_api_key
        else:
            print('class instantiated without auth key')
            
    def get_api_credentials(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
        
        username = data["username"]
        api_key = data["key"]
        
        return username, api_key
        
    def Kaggle_authenticate(self):
        """Autenticate with kagle api using the environment variables or json file with api key on path ".kaggle/kaggle.json".
        """
        try:
            self.api = KaggleApi.authenticate()
        except:
            raise Exception('Authentication Failed!')

    def dataset_download(self, url, download_folder):
        """handles the download of a dataset from kaggle

        Args:
            url (str): url used for download
            download_folder (str): path to drop the files downloaded
        """
        pass
    
    def download_dataset_from_url(self, url, file_name, file_path, unzip=None):
        """Download dataset directly from a url

        Args:
            url (str): string the represents the download link from dataset on kaggle
        """
        
        self.path = file_path+file_name+'.zip'
        
        req = requests.get(url)
        content = req.content
        file = open(self.path, 'wb')
        file.write(content)
        file.close()
        
        if unzip:
            self.__unzip(file_name=file_name)
        
    def __unzip(self, file_name):
        
        file = zipfile.ZipFile(self.path)
        file.extractall(file_name+time.strftime("%Y%m%d-%H%M%S"))

        
        
        
        