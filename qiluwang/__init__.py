# -*-coding:utf-8-*-
import myUtil.htmlUtil as html
import myUtil.fileutil as file

url = 'http://www.76330.com/list-1-951.html'
bsoup = html.getHtmlSoup(url)
areadiv = bsoup.find('div', {'id': 'nav'})
for li in areadiv.find_all('li'):
    us = li.find('a')['href']
    print us
    file.writefile('area_url.txt', 'a+', us)