import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import scrap_act as s_act
import csv

def run_scrapper():
    '''RODA O SCRAPPER'''
      
    #requisição da pagina
    url = 'https://pt.wikipedia.org/wiki/Wikipédia:Sabia_que'   #PRESTAR ATENÇÃO PRA NÃO CORRER O RISCO DE GERAR CODIFICAÇÃO NA URL :)))

    headers = {"User-Agent": "MeuWebScraper/1.0 (estudo de Python)"}
    response = requests.get(url, headers=headers)
    html = response.text

    #ARQUIVO HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    months = s_act.months_extract(soup)
    curiosities = s_act.curiosity_extract(soup)
    
    s_act.scrap_input(curiosities)  
    

    