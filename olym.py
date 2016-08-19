import urllib2
from bs4 import BeautifulSoup
from prettytable import PrettyTable

page = open('./temp.html', 'r').read()
soup = BeautifulSoup(page, "lxml")
result = soup.find('table')


t = PrettyTable(['Rank','Gold','Silver','Bronze','Total'])
for tr in result.find_all('tr')[1:]:
	india = tr.find_all('a',{"href" : "/medals/ind"})
	
	if india :
		#print india
		divs = tr.find_all('div')
		#print divs
		alist = [divs[0].text, divs[2].text, divs[3].text, divs[4].text, divs[5].text]
		t.add_row(alist)
		print t
		break

f = open('./.tally','w')
for item in alist:
	f.write(item + '\n')