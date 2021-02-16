from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.standvirtual.com/carros/').text
print(html_text)
