# -*-coding:utf-8-*-
import myUtil.dbutil as database
import myUtil.htmlUtil as html
import myUtil.fileutil as files
import time, random

import sys

reload(sys)
sys.setdefaultencoding('utf8')

db = database.DB('192.168.1.193', 'skt', pwd='root', tb='company_qiye0712')
db.create('company_name', 'address', 'hangye', 'area', 'person', 'mobile')
for i in xrange(1002, 1035):
    m = "%06d" % i
    x = 1
    while True:
        url = 'http://www.qiye.net/company_pr%s-p%x' % (m, x)
        print url
        x += 1
        try:
            soup = html.getHtmlSoup(url)
            lis = soup.find('ul', {'class': 'companyList'})
            if lis is None:
                files.writefile('city.log', 'w', m)
                break
            areas = soup.find('div', {'class': 'crumbs'})
            area = str(areas).split('</em>')[2].rstrip('        </div>')
            for li in lis.find_all('li'):
                name = li.find('strong').find('a')['title']
                address = str(li.find_all('dl')[0].find_all('dd')[3].string).strip(u'企业地址：')
                hangye = str(li.find_all('dl')[1].find_all('dd')[1].string).strip(u'主营行业：')
                if hangye is None:
                    continue
                urls = 'http://www.qiye.net' + li.find_all('dl')[1].find('dt').find_all('a')[0]['href']
                soups = html.getHtmlSoup(urls)
                lianxi = soups.find('ul', {'class': 'contactbox'})
                person = str(lianxi.find_all('li')[0]).split('</span>')[1].strip('</li>')
                mobile = str(lianxi.find_all('li')[3]).split('</span>')[1].strip('</li>')
                db.insert(name, address, hangye, area, person, mobile)
                time.sleep(random.choice(seq=range(10, 15)))
            files.writefile('city.log', 'w', x)
        except BaseException, e:
            print e
    # files.writefile('city.log', 'w', m)
