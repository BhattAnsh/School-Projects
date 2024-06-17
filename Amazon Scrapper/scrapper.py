from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = "https://www.amazon.com/s?k=books"


HEADERS = ({'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})

while True:
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code == 200:
            break  # Exit the loop if the status code is 200
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        # You can add more error handling code here if needed

soup = bs(response.content, 'html.parser')
print(soup.find_all('div', attrs={'class': "a-cardui _cDEzb_grid-cell_zFYyO p13n-grid-content"}))