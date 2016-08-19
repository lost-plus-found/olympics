import urllib2
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys

script = sys.argv[0]
country = str()
for i in sys.argv[1:-1] :
	country += i + ' '
country += sys.argv[-1]

page = open('./.temp', 'r').read()
soup = BeautifulSoup(page, "lxml")
result = soup.find('table')


t = PrettyTable(['Rank','Gold','Silver','Bronze','Total'])
for tr in result.find_all('tr')[1:]:
	coun = tr.find_all('img',{"alt" : country.title()})
	
	if coun :
		#print india
		divs = tr.find_all('div')
		#print divs
		alist = [divs[0].text, divs[2].text, divs[3].text, divs[4].text, divs[5].text]
		t.add_row(alist)
		print t
		f = open('./.tally','w')
		for item in alist:
			f.write(item + '\n')
		break

