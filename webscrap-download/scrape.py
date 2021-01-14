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
    #scrape(args.url, args.format, args.type)