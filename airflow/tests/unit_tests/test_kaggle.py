from dags.handles.kaggle_handle import KaggleHandle
import pytest
from unittest.mock import patch

def test_authenticate_failure():
    with patch('dags.handles.kaggle_handle.KaggleApi') as MockKagleAPI:
    
        MockKagleAPI.authenticate.side_effect = Exception('Authentication Failed!')
        
        kaggle_handle = KaggleHandle()
        
        with pytest.raises(Exception, match='Authentication Failed!'):
            kaggle_handle.authenticate()