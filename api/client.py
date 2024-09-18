import requests

def ping(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Assuming the URL returns JSON
        else:
            return {"error": "Ping failed", "status_code": response.status_code}
    except requests.RequestException as e:
        return {"error": str(e)}
    
def get_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text()  # Assuming the URL returns HTML or text
        else:
            return {"error": "link connetion failed", "status_code": response.status_code}
    except requests.RequestException as e:
        return {"error": str(e)}
