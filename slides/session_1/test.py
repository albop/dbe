import requests

x = "Hello world"
url = "https://www.escp.eu/"
response = requests.get(url)

if response.status_code == 200:
    webpage_text = response.text
    print(webpage_text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
