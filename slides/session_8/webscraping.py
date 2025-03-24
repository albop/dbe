# %%
url = "https://en.wikipedia.org/wiki/European_Central_Bank"

# download the text from the link above

import requests

url = "https://en.wikipedia.org/wiki/European_Central_Bank"

response = requests.get(url)

# Ensure the request was successful
if response.status_code == 200:
    text = response.text
else:
    print(f"Failed to download the page, status code: {response.status_code}")

#%%

from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

url = "https://en.wikipedia.org/wiki/European_Central_Bank"
response = urlopen(url)

html = response.read().decode()
parser = MyHTMLParser()
parser.feed(html)

webpage_text = parser.text

#%%

# count occurence of word inflation in webpage_text

# Convert the text to lowercase to ensure the count is case-insensitive
webpage_text_lower = webpage_text.lower()

# Count the occurrence of the word "inflation"
inflation_count = webpage_text_lower.count("inflation")

inflation_count