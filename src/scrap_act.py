import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv

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

def curiosity_extract(soup)-> dict:
    '''LÊ O HTML E COLETA AS CURIOSIDADES'''
    
    id_months = months_extract(soup)
    
    all_curiosities = {
    }
    
    for id in id_months:
        
        div = soup.find('h3', id = id).parent       #SELECIONA OS MESES
        
        pre_curiosity = div.next_siblings       #SELECIONA A UL QUE CONTEM AS CURIOSIDADES DE ACORDO COM O MES
        
        curiosity = []
        for childrens in pre_curiosity:
            if isinstance(childrens, Tag) and childrens.name == 'ul':

                for li in childrens.find_all('li'):               #COLETA AS CURIOSIDADES DOS LI
                    data = li.get_text(strip=True)             #SELECIONA CADA LI PARA SUBTRAIR O TEXTO
                    curiosity.append(data)
                    
                break
                    
        all_curiosities.update({id : curiosity})  #INSERE NO DICT

    return all_curiosities

def scrap_input(curiosity: dict):
    
    try:
        
        with open('data/scrap.csv', 'w', newline='', encoding='utf8') as scrap:
            field_names = ['Mês', 'Curiosidades']
            writer = csv.DictWriter(scrap, fieldnames=field_names)
            writer.writeheader()
            for months in curiosity:
                for item in curiosity[months]:
                    writer.writerow({'Mês': months, 'Curiosidades': item})
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as e:
        print(f'Arquivo não escrito pois erro inesperado: {e}')



