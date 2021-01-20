import argparse
import base64
from bs4 import BeautifulSoup
import requests
import json
import  os

if  __name__  ==  "__main__" : 
	parser = argparse.ArgumentParser(description='scrape a webpage')
	parser.add_argument('-t', '--type', choices=['All', 'png', 'jpg'], default='All', help='The image type we want to scrape')
	parser.add_argument('-f', '--format', choices=['img', 'json'], default='img', help='The format images are _saved to')
	parser.add_argument('url', help='The URL we want to scrape for images.')
	args = parser.parse_args()
	scrape(args.url, args.format, args.type)

def scrape(url, format_, type_):  
	try:     
		page = requests.get(url)
	except Exception as e:
		print(str(e))
	else:  
		soup = BeautifulSoup(page, 'html.parser')
		images = _fetch_images(soup, url)
		images = _filter_images(images, type_)
		_save(images, format_, type_)

def _fetch_images(soup, base_url):
	images = []
	for img in soup.findAll('img'): 
		src = img.get('src')
		img_url = f'{base_url}/{src}'
		name = img_url.split('/')[-1]
		images.append(dict(name=name, url=img_url))
	return images

def _filter_images(images, type_):  
    if type_ == 'All':  
        return images
    ext_map = {
		'png': ['.png'],
		'jpg': ['.jpg', '.jpeg'],
	}
    return [
		img for img in images if _match_extensions(img('name'), ext_map[type_])
	]

def _match_extensions(filename, extension_list):  
    name, extension = os.path.splitext(filename.lower())
    return extension in extension_list

def _save(images, format_):
    if images:
		if format_ == 'img':
			_save_images(images)
		else:
			_save_json(images)
		print('Done')
    else:
		print('No images to save.')

def _save_images(images):
	for img in images:
		img_data = requests.get(img['url']).content
		with open(img['name'], 'wb') as f:
			f.write(img_data)

def _save_json(images):
	data = {}
	for img in images:
		img_data = requests.get(img['url']).content
		b64_img_data = base64.b64encode(img_data)
		str_img_data = b64_img_data.decode('utf-8')
		data[img['name']] = str_img_data
	with open('images.json', 'w') as ijson:
		ijson.write(json.dumps(data))