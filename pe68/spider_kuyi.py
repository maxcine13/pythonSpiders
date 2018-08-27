# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys, MySQLdb, time

reload(sys)
sys.setdefaultencoding('utf-8')


def connections(db):
    conn = MySQLdb.connect('192.168.1.105', 'root', '', db, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT VERSION()")
    print cur.fetchall()
    return (conn, cur)


def createTable(cur):
    cur.execute("DROP TABLE IF EXISTS company_qeco")
    createTable = "create table company_qeco(" \
                  "id INT PRIMARY KEY auto_increment," \
                  "companyName VARCHAR (225), " \
                  "linkman VARCHAR (225), " \
                  "address VARCHAR (225), " \
                  "city VARCHAR (225), " \
                  "comType VARCHAR (225), " \
                  "comSize VARCHAR (225), " \
                  "phone VARCHAR (225), " \
                  "telephone VARCHAR (225), " \
                  "rec_ins VARCHAR (225), " \
                  "tradeName VARCHAR (225), " \
                  "beizhu VARCHAR (225)" \
                  ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cur.execute(createTable)


def getHtmlSoup(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0"}
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    text = response.text
    return BeautifulSoup(text, 'html.parser')


def getPhone(num, strPhone):
    if strPhone is None:
        return None
    uuu = 'http://192.168.1.114:8080/skbcj/index.php/Index/index5?web=%s&tel=%s' % (num, strPhone)
    resp1 = requests.get(uuu)
    return resp1.text.lstrip('﻿')


(conn, cur) = connections('skt')
# createTable(cur)
for i in range(1, 1232000):
    baseurl = 'http://%d.company.kuyiso.com/' % i
    url = baseurl + 'company_contact.html'
    soup = getHtmlSoup(url)
    try:
        title = soup.find('a', {'class': 'businessName fl'}).string
        soup1 = soup.select_one('.basicMsg')
        lis = soup1.find_all('li')
        print len(lis)
        linkman = str(lis[1])
        if linkman is not None:
            linkman = linkman.split('</span>')[1].rstrip('</li>').strip()
        print 1, linkman
        phone = lis[2].font.string
        phones = getPhone(i, phone)
        print 2, phones
        comType = str(lis[3])
        if comType is not None:
            comType = comType.split('</span>')[1].rstrip('</li>').strip()
        print 3, comType
        telphone = lis[4].font.string
        telephones = getPhone(i, telphone)
        print 4, telephones
        comSize = str(lis[5])
        if comSize is not None:
            comSize = comSize.split('</span>')[1].rstrip('</li>').strip()
        print 5, comSize
        address = lis[8].var.string
        print 8, address
        city = lis[9].a.string
        print 9, city
        if len(lis) == 13:
            rec_ins = lis[10].div.string
            print 10, rec_ins
            tradeNames = lis[11].find_all('a')
            tradeName = ''
            for name in tradeNames:
                tradeName += name.string + ' '
            print 11, tradeName
            beizhu = lis[12].var.string
            print 12, beizhu
        else:
            rec_ins = None
            print 10, rec_ins
            tradeNames = lis[11].find_all('a')
            tradeName = ''
            for name in tradeNames:
                tradeName += name.string + ' '
            print 11, tradeName
            beizhu = lis[10].var.string
            print 12, beizhu
        sqli = "insert into company_qeco values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sqli,
                    (title, linkman, address, city, comType, comSize, phones, telephones, rec_ins, tradeName, beizhu))
        conn.commit()
        time.sleep(3)
    except BaseException, e:
        print '%d page is error' % i
        print e
cur.close()
conn.commit()
conn.close()
# for num in range(1,len(lis)):
#     print lis[num]
# # print soup1
