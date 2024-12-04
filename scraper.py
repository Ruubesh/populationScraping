import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/world-population-by-year/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'table table-hover table-condensed'})
rows = table.find('tbody').find_all('tr')

population_list = []

for row in rows:
    dic = {
        'Year': row.find_all('td')[0].text.strip(),
        'World Population': row.find_all('td')[1].text.strip(),
        'Yearly Change': row.find_all('td')[2].text.strip(),
        'Net Change': row.find_all('td')[3].text.strip(),
        'Density (P/Km²)': row.find_all('td')[4].text.strip()
    }

    population_list.append(dic)

df = pd.DataFrame(population_list)
df.to_excel('population_data.xlsx', index=False)
