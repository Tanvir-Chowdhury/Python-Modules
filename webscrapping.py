from bs4 import BeautifulSoup
import requests
import csv

'''with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    #print(soup.prettify()) # it makes the code prettier

#article = soup.find('div', class_ = 'article')
#print(match)
for article in soup.find_all('div', class_ = 'article'):
    summary = article.p.text
    headline = article.h2.a.text
    print(headline)
    print(summary)
    print()'''

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

with open('webscrapping.csv', 'w') as csv_file:

    csv_writer = csv.writer(csv_file)
    #csv_writer.writerow(['headline', 'summary', 'link'])
    csv_writer.writerow(['link'])

    for article in soup.find_all('article'):
        headline = article.h2.a.text

        '''if headline == 'Update (2019-09-03)':
            continue'''

        summary = article.find('div', 'entry-content').p.text
        print(headline)
        print(summary)
        try:
            vid_id = article.find('iframe', class_ = 'youtube-player')['src']
            vid_id = vid_id.split('/')[4]
            vid_id = vid_id.split('?')[0]
            link = f'https://www.youtube.com/watch?v={vid_id}'
            print(link)
        except TypeError as e:
            pass
        
        #csv_writer.writerow([headline, summary, link])
        csv_writer.writerow([link])
        print()