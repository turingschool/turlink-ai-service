import requests

def ping(url):
    res = requests.post(url)
    
    if res.status_code == 200:
        return (True, res.json())
    return (False, None)