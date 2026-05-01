from bs4 import BeautifulSoup
import requests 

soup = BeautifulSoup(requests.get("https://www.w3schools.com/html/html_tables.asp").text)
# first we should find our table object:
table = soup.find('table', id="customers")
# then we can iterate through each row and extract either header or row values:
header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)
['Company', 'Contact', 'Country']
for row in rows:
    print(row)
['Alfreds Futterkiste', 'Maria Anders', 'Germany']
['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico']
['Ernst Handel', 'Roland Mendel', 'Austria']
['Island Trading', 'Helen Bennett', 'UK']
['Laughing Bacchus Winecellars', 'Yoshi Tannamuri', 'Canada']
['Magazzini Alimentari Riuniti', 'Giovanni Rovelli', 'Italy']