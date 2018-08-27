# -*-coding:utf-8-*-
import myUtil.htmlUtil as html
import myUtil.fileutil as file
import sys

reload(sys)

sys.setdefaultencoding("gb2312")


def companyMsg(url):
    try:
        co_soup = html.getHtmlSoup(url, 'gb2312')
        contactdiv = co_soup.find('div', {'class': 'codebuy'})
        if contactdiv is None or str(contactdiv).__len__() < 20:
            file.writefile('cn716_com_error.log', 'a+', url)
            return
        dic = {u'公 司 名：': None, u'公司地址：': None, u'所 在 地：': None,
               u'联系电话：': None, u'联 系 人：': None, u'手    机：': None, }
        tds = contactdiv.find_all('td')
        for i in xrange(0, len(tds)):
            title = tds[i].string
            if title is not None:
                title = title.strip()
            # print title
            if dic.has_key(title):
                tda = tds[i + 1].find_all('a')
                if len(tda) > 0:
                    values = ''
                    for a in tda:
                        values += a.string
                    dic[title] = values
                else:
                    dic[title] = tds[i + 1].string
        # for key, value in dic.items():
        #     print key, value
        return dic
    except BaseException, e:
        print 'company page error'
        print url
        file.writefile('cn716_com_error.log', 'a+', str(url))
        print e

# companyMsg('http://www.cn716.com/sellmarket/qyjj654956')
