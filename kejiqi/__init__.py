# -*-coding:utf-8-*-
import util.dbutil as database
import util.htmlUtil as html
import util.fileutil as file, time
import sys

reload(sys)

sys.setdefaultencoding("utf-8")

url = 'http://www.kejiqi.com/company/'
soup = html.getHtmlSoup(url)
divs = soup.find_all('dl', {'class': 'category_item'})
for dd in divs:
    cate = dd.find('dt').a.string
    curl = dd.find('dt').find('a')['href']
    print cate, curl
    file.writefile('kejiqi_category_url.txt', 'a+', str(cate + ' ' + curl))


