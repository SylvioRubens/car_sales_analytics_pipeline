from kaggle.api.kaggle_api_extended import KaggleApi
import requests
import zipfile
import time

class KaggleHandle():
    """Class to handle kagle datasets. You can use it to 
    facilitates processes as the authentication. 
    """
    def __init__(self):
        self.Kaggle_authenticate()

    def Kaggle_authenticate(self):
        """Autenticate with kagle using a key.json

        Args:
            key_file (str): file with api key created in kaggle site
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

        
        
        
        