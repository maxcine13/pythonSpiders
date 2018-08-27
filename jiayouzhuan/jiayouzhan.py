# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file,time

db = database.DB('192.168.1.193', 'skt', pwd='root', tb='company_jiayouzhuan')
db.delete()
# db.create("name", "area", "address", "trade", "mobile", "tele", "qq", "email")
base = 'https://www.atobo.com.cn'
urls = file.readfile('area_url.txt')
for url in urls:
    print url
    file.writefile('area_url_log.txt', 'w', url)
    soup = html.getHtmlSoup(url)
    pages = soup.find('li', {'class': 'spagelist'})
    cpage = pages.find_all('strong')[0].string
    page = pages.find_all('strong')[1].string
    print page
    lastpage = 0
    for x in range(49, int(page) + 1):
        nurl = url[:-1] + '-y%d' % x
        nsoup = html.getHtmlSoup(nurl)
        div = nsoup.find('div',{'class':'product_contextlist bplist'})
        for li in div.find_all('li',{'class':'pp_name'}):
            time.sleep(3)
            u1 = li.find_all('a')[0]['href']+'/WebSite/bexd122859-c13.html'
            u2 = li.find_all('a')[1]['href']
            print u1,u2
            detail = html.getHtmlSoup('http:'+u1)
            gs = html.getHtmlSoup('http:'+u2)
            title = gs.find('div',{'class':'cur_post'})
            area = title.find_all('a')[2].string+' '+title.find_all('a')[3].string
            table = gs.find('table',{'class':'gsinfotable'})
            print area
            break
        npages = nsoup.find('li', {'class': 'spagelist'})
        ncpage = npages.find_all('strong')[0].string
        print lastpage, ncpage
        if lastpage == int(ncpage):
            print lastpage
            break
        else:
            lastpage = int(ncpage)
        print nurl
    break
del db
