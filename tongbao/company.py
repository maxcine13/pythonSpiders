# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as file, time


def getCompanyMsg(url):
    try:
        soup = html.getHtmlSoup(url)
        dic = {u'公司名称：': None, u'公司地址：': None, u'所在地区：': None, u'公司电话：': None,
               u'公司传真：': None, u'电子邮件：': None, u'联 系 人：': None, u'部门(职位)：': None,
               u'手机号码：': None}
        for tr in soup.find('div', {'class': 'px13 lh18'}).find_all('tr'):
            title = tr.find_all('td')[0].string
            if dic.has_key(title):
                dic[title] = tr.find_all('td')[1].string
        for key, value in dic.items():
            print key, value
        return dic
    except BaseException, e:
        print e
        print 'company page error'
