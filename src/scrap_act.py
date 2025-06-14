import requests
from bs4 import BeautifulSoup
import csv


#requisição da pagina
url = 'https://pt.wikipedia.org/wiki/Wikipédia:Sabia_que'   #PRESTAR ATENÇÃO PRA NÃO CORRER O RISCO DE GERAR CODFICAÇÃO NA URL :)))

headers = {"User-Agent": "MeuWebScraper/1.0 (estudo de Python)"}
response = requests.get(url, headers=headers)
html = response.text

#ARQUIVO HTML
soup = BeautifulSoup(html, 'html.parser')

def months_extract(soup)-> list:
    '''LÊ O HTML E COLETA OS MESES DAS CURIOSIDADES'''
    
    #SELEÇÃO DOS TITULOS VIA SELETOR CSS
    divs = soup.select("div.mw-heading.mw-heading3")            ##CUIDADO COM OS ESPAÇOS NO NOME DA CLASS, POIS INTERFERE NO DOM
    
    #REORGANIZA OS ITENS FORMATADOS DE CADA <h3> POR CADA <div>
    
    months = []
    for div in divs:
        h3 = div.find("h3")
        if h3:
            months.append(h3.text.strip())
            
    return months

def curiosity_extract(soup):
    '''LÊ O HTML E COLETA AS CURIOSIDADES'''
    
#ainda em construção.
    curiosities = soup.find_all('li')
    
    all_curiosities = []
    for cur in curiosities:
        all_curiosities.append(cur.text.strip())
        
    return all_curiosities

def scrap_input():
    
    with open('data\scrap.csv', 'w', newline= '') as scrap:
        fild_names = ['Titulo', 'Preço']
        writer = csv.DictWriter(scrap, fieldnames=fild_names)
        writer.writerow({'Titulo': 1, 'Preço': 1})
        
a = months_extract(soup)
print(a)
