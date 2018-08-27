# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time

db = database.DB('192.168.1.105', 'skb', tb='company_qy6_823')
db.create('name', 'scop', 'com_mode', 'business_mode', 'com_size', 'trade', 'regMoney', 'faRen'
          , 'regDate', 'person','phone', 'fax', 'mphone', 'address')
lurl = file.readfile('qy6.txt')
for url in lurl:
    try:
        urls = url.split(' ')
        hangye = urls[0]
        hurl = urls[1]
        soup = html.getHtmlSoup(hurl)
        tb = soup.select('body')[0].select('center')[1]
        td = tb.find_all('td')
        size = len(td)
        page = int(td[size - 1].find_all('strong')[3].string)
        for p in xrange(1, page + 1):
            purl = str(hurl).rstrip('qyC0101.html') + 'pqyC0101_p%d.html' % p
            psoup = html.getHtmlSoup(purl)
            tbs = psoup.select('body')[0].select('center')[1]
            tds = tbs.find_all('td')
            sizea = len(tds)
            for x in xrange(50, sizea):
                a = tds[x].find_all('a', {'target': '_blank'})
                if len(a) > 0:
                    url1 = a[0]['href']
                    hrefs = str(url1).split('comp')
                    url2 = hrefs[0] + 'about' + hrefs[1]
                    url3 = hrefs[0] + 'con' + hrefs[1]
                    soup = html.getHtmlSoup(url1)
                    ll = soup.select('body')[0].select('center')
                    if len(ll) > 1:
                        li = ll[1].find_all('td', {'align': 'center'})[1]
                        l1s = li.find_all('tbody')[0].find_all('td')
                        l2s = li.find_all('tbody')[1].find_all('td')
                    else:
                        l1s = html.getHtmlSoup(url2).select('body')[0].select('center')[0].find_all('tbody')[
                            0].find_all('td')
                        l2s = html.getHtmlSoup(url3).select('body')[0].select('center')[0].find_all('tbody')[
                            0].find_all('td')
                    name = a[0].strong.string
                    scop = str(l1s[0]).split('<br/>')[1].rstrip('</td>').strip()
                    com_mode = str(l1s[1]).split('<br/>')[1].rstrip('</td>').strip()
                    business_mode = str(l1s[2]).split('<br/>')[1].rstrip('</td>').strip()
                    com_size = str(l1s[3]).split('<br/>')[1].rstrip('</td>').strip()
                    print str(l1s[4]).split('<br/>')[1].rstrip('</td>').strip()
                    trade = str(l1s[5]).split('<br/>')[1].rstrip('</td>').strip()
                    print str(l1s[6]).split('<br/>')[1].rstrip('</td>').strip()
                    print str(l1s[7]).split('<br/>')[1].rstrip('</td>').strip()
                    regMoney = str(l1s[8]).split('<br/>')[1].rstrip('</td>').strip()
                    faRen = str(l1s[9]).split('<br/>')[1].rstrip('</td>').strip()
                    regDate = str(l1s[10]).split('<br/>')[1].rstrip('</td>').strip()
                    print str(l1s[11]).split('<br/>')[1].rstrip('</td>').strip()
                    print str(l1s[12]).split('<br/>')[1].rstrip('</td>').strip()
                    person = l2s[1].font.string.strip()
                    phone = l2s[4].string.strip()
                    fax = l2s[6].string.strip()
                    mphone = l2s[8].string.strip()
                    address = l2s[12].string.strip()
                    db.create(name, scop, com_mode, business_mode, com_size, trade, regMoney, faRen, regDate, person,
                              phone, fax, mphone, address)
    except BaseException, e:
        print e
        print 'error'
        file.writefile('error_qy6.log', 'a+', str(purl + '' + url1))
