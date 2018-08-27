# -*-coding:utf-8-*-
import util.dbutil as database
import util.htmlUtil as html
import util.fileutil as file, time
import sys, company

reload(sys)

sys.setdefaultencoding("utf-8")

db = database.DB('192.168.1.105', 'skb', tb='company_kejiqi_827')
db.create('name', 'scop', 'com_mode', 'business_mode', 'com_size', 'trade', 'regMoney', 'area'
          , 'regDate', 'person', 'position', 'phone', 'fax', 'mphone', 'address', 'email')
urltxt = file.readfile('kejiqi_category_url.txt')
for txt in urltxt:
    trade = txt.split(' ')[0]
    urls = txt.split(' ')[1]
    page = 1
    while True:
        url = urls + 'pn%d.html' % page
        try:
            soup = html.getHtmlSoup(url)
            list = soup.find_all('div', {'class': 'invite_item clearfix'})
            if len(list) <= 0:
                file.writefile('kejiqi_com_error1.log', 'a+', url)
                break
            for li in list:
                comurl = li.h2.a.get('href')
                dic = company.companyMsg(comurl)
                # for key, value in dic.items():
                #     print key, value
                name = dic[u'公司名称：']
                scop = dic[u'经营范围：']
                com_mode = dic[u'公司类型：']
                business_mode = dic[u'经营模式：']
                com_size = dic[u'公司规模：']

                trade = dic[u'主营行业：']
                regMoney = dic[u'注册资本：']
                regDate = dic[u'注册年份：']
                person = dic[u'联 系 人：']
                phone = dic[u'公司电话：']

                fax = dic[u'公司传真：']
                mphone = dic[u'手机号码：']
                address = dic[u'公司地址：']
                email = dic[u'电子邮件：']
                area = dic[u'所 在 地：']
                position = dic[u'部门(职位)：']
                db.insert(name, scop, com_mode, business_mode, com_size, trade, regMoney, area
                          , regDate, person, position, phone, fax, mphone, address, email)
        except BaseException, e:
            file.writefile('kejiqi_com_error.log', 'a+', url)
            print e
    page += 1
