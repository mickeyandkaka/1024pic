#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

scrap_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36'
        }

def save_img(src):
	r = requests.get(src, timeout = 5, headers = scrap_header)
	file_name = src.split('/')[-1]
	suffix = file_name.split('.')[-1]
	name = file_name.split('.')[-2]

	output_name = name + '.' + suffix
	f = open(output_name, 'wb')
	f.write(r.content)
	f.flush()
	f.close()

def main():
	url       = sys.argv[1]
	response  = requests.get(url, timeout = 5, headers = scrap_header)
	html      = response.content.decode('gbk')
	soup      = BeautifulSoup(html)
	
	div_tags  = soup.find_all('div')
	top_level = None
	content   = None

	for div in div_tags:
		class_list = div.get('class')
		if class_list is None:
			continue

		if(class_list[0] == 'tpc_content'):
			top_level = div
			break

	images = top_level.find_all('img')
	for img in images:
		src = img.get('src')
		save_img(src)



if __name__ == '__main__':
	main()
