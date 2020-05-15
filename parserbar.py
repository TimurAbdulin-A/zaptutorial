import requests
from bs4 import BeautifulSoup as BS
brand = input('ВВедите название производителя:  ')
number = input('ВВедите номер детали:  ')

r = requests.get('https://******.ru/parts/'+str(brand)+'/'+str(number))
html = BS(r.content, 'html.parser')

for el in html.select('.characteristicsListRow'):
    title = el.select('span:nth-of-type(2)')
    print( title[0].text )
