import requests
from bs4 import BeautifulSoup
import scrapper

URL = 'https://pt.wikipedia.org/wiki/Wikipédia:Sabia_que'

def request(url: str = URL) -> str:
    """Request the HTML page and generate the soup"""

    headers = {"User-Agent": "MeuWebScraper/1.0 (estudo de Python)"}
    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def main():
    '''Ask for request and run the scrapper.'''
      
    soup = request()

    curiosities = scrapper.curiosity_extract(soup)

    # Select the path for .csv files be.
    DATA_PATH = 'data'
    
    try:
        scrapper.scrap_input(curiosities,
                            data_path= DATA_PATH,
                            csv_name= 'scrap')
        print(f'The scrapped was succesfuly made. Check at: {DATA_PATH} directory!')
    except Exception as e:
        print(f'Unexpected error has ocurred: {e}')

if __name__ == '__main__':
    main()