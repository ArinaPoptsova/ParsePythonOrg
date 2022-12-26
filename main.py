import requests
from bs4 import BeautifulSoup

response = requests.get('https://python.org').text
soup = BeautifulSoup(response, 'lxml')
menu = soup.select('#content > div > section > div:nth-of-type(3) > div:nth-of-type(2) > div > ul > li > a')

for option in menu:
    opt_link = option.get('href')
    opt_page = requests.get(f'https://python.org{opt_link}').text
    opt_soup = BeautifulSoup(opt_page, 'lxml')
    opt_info = opt_soup.select('#content > div > section > article')[0]
    info_print = f'Event: {opt_info.find("h1").get_text()} \n ' \
                 f'Date: {opt_info.select("h3 > time:nth-of-type(1)")[0].get_text()}, ' \
                 f'{opt_info.select("h3 > time:nth-of-type(3)")[0].get_text()} \n' \
                 f'Description: {opt_info.find("div").get_text()} \n\n'
    print(info_print)
