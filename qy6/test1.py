# -*-coding:utf-8-*-
import myUtil.htmlUtil as html

# soup = html.getHtmlSoup('http://www.qy6.com/qyml/compzrzg14233863.html')
soup = html.getHtmlSoup('http://www.qy6.com/qyml/compsdlmjq1234.html')
ll = soup.select('body')[0].select('center')
if len(ll) > 1:
    li = ll[1].find_all('td', {'align': 'center'})[1]
    l1 = li.find_all('tbody')[0]
    l2 = li.find_all('tbody')[1]
    l1s = l1.find_all('td')
    l2s = l2.find_all('td')
else:
    hrefs = str('http://www.qy6.com/qyml/compsdlmjq1234.html').split('comp')
    url2 = hrefs[0] + 'about' + hrefs[1]
    url3 = hrefs[0] + 'con' + hrefs[1]
    soup = html.getHtmlSoup(url2).select('body')[0].select('center')[0].find_all('tbody')[0]
    l1s = soup.find_all('td')
    soup1 = html.getHtmlSoup(url3).select('body')[0].select('center')[0].find_all('tbody')[0]
    l2s = soup1.find_all('td')

    print str(l1s[0]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[1]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[2]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[3]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[4]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[5]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[6]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[7]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[8]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[9]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[10]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[11]).split('<br/>')[1].rstrip('</td>').strip()
    print str(l1s[12]).split('<br/>')[1].rstrip('</td>').strip()
    print l2s[1].font.string.strip()
    print l2s[4].string.strip()
    print l2s[6].string.strip()
    print l2s[8].string.strip()
    print l2s[12].string.strip()
