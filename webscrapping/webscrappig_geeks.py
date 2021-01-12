from bs4 import BeautifulSoup
import requests
import csv
import sys

source = requests.get('https://www.geeksforgeeks.org/python-programming-language/python-tutorial/?ref=lbp#modules').text

soup = BeautifulSoup(source, 'html5lib')

with open('webgeekscrap.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['titles'])
    for article in soup.find_all('article'):
        for uls in article.find_all('ul'):
            try:
                for titles in uls.find_all('li'):
                    title = titles.a.text
                    csv_writer.writerow([title])
                    print(title)
                    if title == 'Exception handling':
                        sys.exit()
            except Exception as e:
                print(e)
