# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time

# db = database.DB('192.168.1.105', 'skb', pwd='', tb='qiluwang')

for area in xrange(1, 32):
    url = 'http://www.76330.com/list-%d-1.html' % area
    psoup = html.getHtmlSoup(url)
    pl = psoup.find('ul', {'class': 'pagelist'})
    page = int(pl.find('b').string) / 10 + 1
    print page
    for p in xrange(0, page):
        urlp = 'http://www.76330.com/list-%d-%d.html' % (area, p)
        print url
        soup = html.getHtmlSoup(urlp)
        try:
            for li in soup.find_all('a', {'class': 'title'}):
                curl = li['href']
                companyname= li.string
                csoup = html.getHtmlSoup(curl)
                div = csoup.find('div',{'class':'base0910'})

            print ''
        except:
            print ''
        break
    break
