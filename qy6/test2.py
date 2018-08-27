# -*-coding:utf-8-*-
import myUtil.htmlUtil as html
import myUtil.dbutil as database

db = database.DB('192.168.1.105', 'skb', tb='company_wy0823')
db.create('companyName', 'address', 'phone', 'mphone', 'person', 'fax', 'categroy', 'area')
try:
    strpage = str(html.getHtmlSoup('http://www.wyw.cn/companylist').find('div', {'id': 'fenye'})).strip()
    page = int(str(strpage[:-6]).strip()[-16:].strip().lstrip('共').rstrip('页'))
    print page

    for p in xrange(0, page):
        url = 'http://www.wyw.cn/companylist/Default.aspx?start=%d' % (p * 99)
        print url
        soup = html.getHtmlSoup(url)
        for li in soup.find_all('div', {'class': 'zuobox_contect'})[0].find_all('li'):
            curl = 'http://www.wyw.cn' + li.find('a')['href']
            print curl
            csoup = html.getHtmlSoup(curl)
            ul = csoup.find('ul', {'class': 'lh20'})
            if ul is None:
                continue
            else:
                uls = ul.find_all('li')
            # print uls
            companyname = uls[0].find('a').string
            address = uls[1].string.lstrip(u'公司地址： ')
            tel = uls[2].string.lstrip(u'联系电话： ')
            mobile = uls[3].string.lstrip(u'手机号码： ')
            fax = uls[4].string.lstrip(u'公司传真： ')
            per = str(uls[5]).split('<a')[0].lstrip('<li>')
            person = str(per).split('：')[1]
            area = address.split(u'市')[0] + u'市'
            print companyname, address, tel, mobile, person, fax, '卫浴', area
            db.insert(companyname, address, tel, mobile, person, fax,'卫浴',area)
            # break
        # break
except BaseException, e:
    print e
    print 'page error'
