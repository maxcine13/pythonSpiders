# -*-coding:utf-8-*-
import util.htmlUtil as html
import util.fileutil as file
import sys

reload(sys)

sys.setdefaultencoding("utf-8")

url = 'http://cn.kejiqi.com/bjpd/'


def companyMsg(url):
    print url
    contact = url + 'contact/'
    credit = url + 'credit/'
    try:
        co_soup = html.getHtmlSoup(contact)
        cr_soup = html.getHtmlSoup(credit)
        contactdiv = co_soup.find('div', {'class': 'px13 lh18'})
        creditdiv = cr_soup.find('div', {'class': 'px13 lh18'})
        if contactdiv is None or str(contactdiv).__len__() < 20:
            file.writefile('kejiqi_com_error.log', 'a+', url)
            return
        if creditdiv is None or str(creditdiv).__len__() < 20:
            file.writefile('kejiqi_com_error.log', 'a+', url)
            return
        dic = {u'公司名称：': None, u'公司地址：': None, u'所 在 地：': None, u'公司电话：': None,
               u'公司传真：': None, u'电子邮件：': None, u'联 系 人：': None, u'部门(职位)：': None,
               u'手机号码：': None, u'公司类型：': None, u'公司规模：': None, u'注册资本：': None,
               u'注册年份：': None, u'经营模式：': None, u'经营范围：': None, u'主营行业：': None}
        tds = contactdiv.find_all('td')
        for i in xrange(0, len(tds)):
            title = tds[i].string
            if dic.has_key(title):
                dic[title] = tds[i + 1].string
        tds = creditdiv.find_all('td')
        for i in xrange(0, len(tds)):
            title = tds[i].string
            if str(title).__eq__('主营行业：'):
                dic[title] = tds[i + 1].find_all('a')[0].string
            elif dic.has_key(title):
                dic[title] = tds[i + 1].string
        # for key, value in dic.items():
        #     print key, value
        return dic
    except BaseException, e:
        print 'company page error'
        print url
        file.writefile('kejiqi_com_error.log', 'a+', url)
        print e
