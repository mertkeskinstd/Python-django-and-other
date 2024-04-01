import requests
from bs4 import BeautifulSoup

url="https://www.omu.edu.tr/tr"

a=requests.get(url)
print(a.text)