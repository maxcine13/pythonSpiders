# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys, myUtil as util

reload(sys)
sys.setdefaultencoding('utf-8')
try:
    dic = {}
    urls = []
    list = util.readfile('pe68_cats1.txt')
    for x in list:
        s = x.split(' ')
        dic[s[0] + '|' + s[1]] = s[2]
        urls.extend(s[2])
    for k, v in dic.items():
        print k, v
        sucess = util.readfile('pe68_sucess.txt')
        if v in sucess:
            continue
        soup = util.getHtmlSoup(v)
        page = 1
        try:
            pagediv = soup.select('.pages')[0]
            page = str(pagediv.find('cite').string).split('/')[1].__str__()[:-3]
            print page
        except:
            page = 1
            print 'page is error'
        print page
        for x in range(1, int(page) + 1):
            url = str(v).rstrip('.html') + '-%d.html' % x
            soups = util.getHtmlSoup(url)
            comdiv = soups.select('.list')
            for com in comdiv:
                u = str(com.find('a').get('href')) + 'introduce/'
                util.writefile('pe68_comp.txt', u)
                print u
        util.writefile('pe68_sucess.txt', str(k).split('|')[1])
        # with open('pe68_sucess', 'a') as f:
        #     f.write('\n' + str(k).split('|')[1])
except BaseException, e:
    print 'error', e
