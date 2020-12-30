from requests_html import HTML, HTMLSession

Session = HTMLSession()
r = Session.get("https://coreyms.com")


# genereting dynamic  javascript code
with open('simple2.html') as html_file:
    source = html_file.read()
    html = HTML(html = source)
    html.render()
print(html.find('#footer', first=True).html)

# genereting child links
for link in r.html.links:
    print(link)

# genereting absolute links
for link in r.html.absolute_links:
    print(link)

# genereting articles with summary and links.
articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    summary = article.find('.entry-content p', first=True).text 
    print(f'headline: {headline}')
    print(f'summary: {summary}')
    try:
        vid_id = article.find('iframe', first=True).attrs['src'].split('/')[4].split('?')[0]
        vid_link = f'https://youtube.com/watch?v={vid_id}'
        print(f'link: {vid_link}')
    except Exception as e:
        print(f'link: None')
    
    print()