# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time
import sys

reload(sys)

sys.setdefaultencoding("utf-8")

for p in xrange(1, 33):
    url = 'http://www.cn716.com/company%d' % p
    soup = html.getHtmlSoup(url, 'GB2312')
    divs = soup.find_all('span', {'class': 'class2_1x'})
    for dd in divs:
        cate = dd.a.string
        curl = dd.find('a')['href']
        if str(cate).startswith('未分类') or str(cate).startswith('其他'):
            file.writefile('cn716_error_url.txt', 'a+', str(cate.lstrip('.') + ' ' + 'http://www.cn716.com/' + curl))
            continue
        print cate, 'http://www.cn716.com/' + curl
        file.writefile('cn716_category_url1.txt', 'a+', str(cate.lstrip('.') + ' ' + 'http://www.cn716.com/' + curl))
