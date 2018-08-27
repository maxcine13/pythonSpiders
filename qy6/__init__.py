# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time

# db = database.DB('192.168.1.105', 'skb', pwd='', tb='qiluwang')
url = 'http://www.qy6.com/qyml'
hsoup = html.getHtmlSoup(url)
for a in hsoup.find_all('a', {'target': '_blank'}):
    hangye = a.string
    hurl = a['href']
    if str(hurl).startswith('http://'):
        continue
    urls = hangye+' http://www.qy6.com'+hurl
    print urls
    file.writefile('qy6.txt', 'a+', urls.encode('utf8'))
