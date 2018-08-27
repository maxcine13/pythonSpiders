# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time
import sys, company

reload(sys)

sys.setdefaultencoding("utf-8")

db = database.DB('192.168.1.105', 'skb', tb='company_qy6_823')
db.create('name', 'address', 'area', 'phone', 'fax',
          'trade', 'email', 'person','mphone', 'position')
url = 'http://www.tonbao.com/company/'
soup = html.getHtmlSoup(url)
divs = soup.find('div', {'class': 'left_box'}).find('div', {'class': 'catalog'})
trade = ''
purl = ''
for td in divs.find_all('td'):
    try:
        lurl = td.find('p').find('a')['href']
        trade = td.find('p').a.strong.span.string
        print lurl
        lsoup = html.getHtmlSoup(lurl)
        page = int(str(lsoup.find('div', {'class': 'pages'}).cite.string).split('/')[1].strip(u'页'))
        for p in xrange(1, page + 1):
            purl = lurl + str(p)
            csoup = html.getHtmlSoup(purl)
            comp = csoup.find_all('div', {'class': 'list'})
            curl = comp[0].find('a')['href'] + 'contact/'
            dic = company.getCompanyMsg(curl)
            dic = {u'公司名称：': None, u'公司地址：': None, u'所在地区：': None, u'公司电话：': None,
                   u'公司传真：': None, u'电子邮件：': None, u'联 系 人：': None, u'部门(职位)：': None,
                   u'手机号码：': None}
            cname = dic[u'公司名称：']
            address = dic[u'公司地址：']
            area = dic[u'所在地区：']
            phone = dic[u'公司电话：']
            fax = dic[u'公司传真：']
            email = dic[u'电子邮件：']
            person = dic[u'联 系 人：']
            position = dic[u'部门(职位)：']
            mphone = dic[u'手机号码：']
            db.create(cname, address, area, phone, fax,
                      trade, email, person,mphone, position)
    except BaseException, e:
        print e
        file.writefile('tongbao_error.log', 'a+', str(trade + ' ' + purl))
