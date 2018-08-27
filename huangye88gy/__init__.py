# -*- coding:utf-8 -*-
import myUtil as u
import sys

reload(sys)

sys.setdefaultencoding("utf-8")
text = u.readfile('gy_hy88.txt')
u.writeCsv('gy_hy.csv', ['companyName', 'address', 'radic', 'linkman', 'phone', 'tele', 'fax'])
for lin in text:
    if lin is None or lin is '':
        continue
    tradic = lin.split(' ')[0]
    urls = lin.split(' ')[1]
    # print tradic, urls
    i = 1
    while (True):
        url = urls + 'pn%d' % i
        try:
            soup = u.getHtmlSoup(url)
            dls = soup.find_all('dl', {'itemtype': 'http://data-vocabulary.org/Organization'})
            for dl in dls:
                companyName = dl.find('dt').h4.a.string
                # print dl.find('dt').span.a.string#手机号，不需要
                curl = dl.find('dt').h4.a.get('href') + 'company_contact.html'
                # print curl
                try:
                    comsoup = u.getHtmlSoup(curl)
                    dic = {'联系人': None, '手机': None, '电话': None, '传真': None, '地址': None}
                    uls = comsoup.find('ul', {'class': 'con-txt'})
                    # print uls
                    for li in uls.find_all('li'):
                        title = li.find('label').string
                        title = title.decode('utf-8')[:-1].encode('utf-8')
                        if dic.has_key(title):
                            content = ''
                            if str(li).__contains__('href'):
                                content = li.find('a').string
                            else:
                                content = str(li).split('</label>')[1].rstrip('</li>')
                            if content is '':
                                content = None
                            dic[title] = content
                        # dic['tradic'] = tradic
                        # dic['companyName'] = companyName
                    linkman = dic['联系人']
                    phone = dic['手机']
                    tele = dic['电话']
                    fax = dic['传真']
                    address = dic['地址']
                    print curl
                    print companyName, address, tradic, linkman, phone, tele, fax
                    list = [companyName, address, tradic, linkman, phone, tele, fax]
                    u.writeCsv('gy_hy.csv', list)
                except BaseException, e:
                    print 'error', e
                    u.writefile('gy_errorlog1.txt', curl)
            page = int(soup.find('div', {'class': 'page_tag Baidu_paging_indicator'}).span.string)
            print page
            if i != page:
                break
            i += 1
        except BaseException, e:
            print '%s is error' % url
            u.writefile('gy_errorlog.txt', url)
