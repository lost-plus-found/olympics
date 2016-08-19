import urllib2
from bs4 import BeautifulSoup
from prettytable import PrettyTable

page = open('./.temp', 'r').read()
soup = BeautifulSoup(page, "lxml")
result = soup.find('table')
f = open('./.tally','r').read()

t = PrettyTable(['Rank','Gold','Silver','Bronze','Total'])
for tr in result.find_all('tr')[1:]:
	india = tr.find_all('a',{"href" : "/medals/ind"})
	
	if india :
		#print india
		divs = tr.find_all('div')
		#print divs
		alist = [divs[0].text, divs[2].text, divs[3].text, divs[4].text, divs[5].text]

		if alist[0] != f.split('\n')[0]:		
			t.add_row(alist)
			print "India has own a medal"
			print t
			fl = open('./.tally','w')
			for item in alist:
				fl.write(item + '\n')
			print "Hey!, I'll remind you as soon as India wins another medal!"

		break


