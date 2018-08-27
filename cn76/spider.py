# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time
import sys, company, re

reload(sys)

sys.setdefaultencoding('gb2312')

db = database.DB('192.168.1.105', 'skb', tb='company_cn716_827')
db.create('name', 'scop', 'trade', 'area'
          , 'person', 'phone', 'mphone', 'address')
urltxt = file.readfile('cn716_category_url1.txt')
for txt in urltxt:
    trade = txt.split(' ')[0]
    urls = txt.split(' ')[1]
    soup = html.getHtmlSoup(urls, 'gb2312')
    sell = soup.find('div', class_='sell_1_b1_page')
    try:
        page = int(sell.find_all('span', class_='read')[-1].string) + 1
        for p in xrange(1, page):
            purl = urls + '_%d' % p
            print purl
            try:
                for li in html.getHtmlSoup(purl, 'gb2312').find_all('ul', class_='sell_new'):
                    # http://www.cn716.com/
                    url = 'http://www.cn716.com/' + li.find('li').a.get('href')
                    manpros = li.find('li').find_all('span')[2]
                    scop = str(manpros).split('<a')[0].split('>')[1].strip()
                    dic = company.companyMsg(url)
                    # print dic
                    cname = dic[u'公 司 名：']
                    address = dic[u'公司地址：']
                    area = dic[u'所 在 地：']
                    phone = dic[u'联系电话：']
                    person = dic[u'联 系 人：']
                    mphone = dic[u'手    机：']
                    print cname, scop,trade, area ,person, phone, mphone, address
                    # db.insert(cname, scop,trade, area ,person, phone, mphone, address)
            except BaseException,e:
                print 'list is error'
                print e
                file.writefile('cn716_error.log', 'a+', str(trade + ' ' + purl+' list error'))
            # break
    except BaseException,e:
        print 'page is error'
        print e
        file.writefile('cn716_error.log', 'a+', str(trade + ' ' + urls+' page error'))
