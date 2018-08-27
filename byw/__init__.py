# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time


db = database.DB('192.168.1.105', 'skb', tb='company_byw_824')
db.create('name', 'address', 'area', 'phone', 'fax', 'person', 'mphone',
          'com_mode', 'com_size', 'regMoney', 'regDate', 'business_mode', 'scop', 'trade')
url = 'http://www.byf.com/b2b/dianqihangye/'
soup = html.getHtmlSoup(url)
hyangdiv = soup.find('div', {'class': 'clist'})
try:
    for a in hyangdiv.find_all('a'):
        hangye = a.string
        url = a['href']
        while True:
            soup = html.getHtmlSoup(url)
            comli = soup.find('div', {'class': 'list'})
            for li in comli.find_all('li'):
                print 'page'
                contacturl = li.find('div', {'class': 'dz'}).a['href']
                crediturl = str(contacturl).replace('contact', 'credit')
                consoup = html.getHtmlSoup(contacturl)
                div = consoup.find('div', {'class': 'm-content'})
                # ul = div.find_all('ul')
                dict = {u'公司地址：': None, u'公司电话：': None, u'公司传真：': None, u'联 系 人：': None, u'手机号码：': None}
                for ul in div.find_all('ul'):
                    t = ul.find('li', {'class': 'cl'}).string
                    if dict.has_key(t):
                        dict[t] = ul.find('li', {'class': 'cr'}).string
                address = dict[u'公司地址：']
                phone = dict[u'公司电话：']
                fax = dict[u'公司传真：']
                person = dict[u'联 系 人：']
                mphone = dict[u'手机号码：']
                credsoup = html.getHtmlSoup(crediturl)
                tds = credsoup.find_all('td', {'class': 'jstdR'})
                cname = tds[0].string
                c_mode = tds[1].string
                area = tds[2].string
                c_size = tds[3].string
                r_money = tds[4].string
                r_date = tds[5].string
                b_mode = tds[7].string
                b_scop = tds[8].string
                trade = hangye
                print cname, address, area, phone, fax, person, mphone
                print c_mode, c_size, r_money, r_date, b_mode, b_scop, trade
                db.insert(cname, address, area, phone, fax, person, mphone, c_mode, c_size, r_money, r_date, b_mode, b_scop,
                          trade)
            pagediv = soup.find('div', {'class': 'page_news'})
            nexturl = pagediv.find_all('a')[-1]['href']
            print nexturl
            print hangye
            if str(nexturl).endswith('.html'):
                url = nexturl
            else:
                break
except BaseException, e:
    print e
    print 'error'
    file.writefile('error_byw.log', 'a+', string=str(hangye + ' ' + url+' '+cname))
