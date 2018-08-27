# -*-coding:utf-8-*-
import myUtil.htmlUtil as html

soup = html.getHtmlSoup('http://www.wyw.cn/companylist/345345/')
print soup.find('ul', {'class': 'lh20'})

