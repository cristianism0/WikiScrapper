from bs4.element import Tag
from pathlib import Path
import csv

def months_extract(soup)-> list:
    '''Parser the HTML and extract the DIVS that contain the curiosities'''
    
    divs = soup.select("div.mw-heading.mw-heading3")
        
    months = []
    for div in divs:
        h3 = div.find("h3")
        if h3:
            months.append(h3.text.strip())
            
    return months

def curiosity_extract(soup)-> dict:
    """Parser throught the DIVS and collect the curiosities"""    
    id_months = months_extract(soup)
    
    all_curiosities = {}
    
    for id in id_months:
        
        # Find the curiosities for each month (div) 
        div = soup.find('h3', id = id).parent       
        
        pre_curiosity = div.next_siblings    
        
        curiosity = []

        for childrens in pre_curiosity:
            # The curiosities in at the ul tag, so we need to iterate over 
            if isinstance(childrens, Tag) and childrens.name == 'ul':

                for li in childrens.find_all('li'):               
                    data = li.get_text(strip=False)             
                    curiosity.append(data)
                    
                break
                    
        all_curiosities.update({id : curiosity})  

    return all_curiosities

def scrap_input(curiosity: dict, data_path: Path, csv_name: str):
    """Create the .csv file with the content"""
    # Create the dir for scrappers.

    Path(data_path).mkdir(exist_ok=True)

    # Treat the name
    csv_name.strip()
    csv_name = csv_name + '.csv'

    with open(data_path / Path(csv_name), 'w', newline='', encoding='utf8') as scrap:
        field_names = ['Month', 'Curiosities']
        writer = csv.DictWriter(scrap, fieldnames=field_names)
        writer.writeheader()
        for months in curiosity:
            for item in curiosity[months]:
                writer.writerow({'Month': months, 'Curiosities': item})
    



