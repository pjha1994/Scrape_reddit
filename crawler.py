import re
import time
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import os
import httplib2

final_list = set()
def make_soup(s):
   match=re.compile('https://|http://|www.|.com|.in|.org|gov.in')
   if re.search(match,s):
     http = httplib2.Http()
     status, response = http.request(s)
     page = BeautifulSoup(response,"html.parser")
     return page
   else:
     return None

def get_list_of_urls(url):
	base = url
	match=re.compile('https://|http://|www.|.com|.in|.org|gov.in')
	match = re.compile(url)
	soup = make_soup(url)
	l = set()
	try:
		for a in soup.find_all('a'):
	    		try:
				if re.search(match,a['href']) and a['href']!=url:
					l.add(str(a['href']))
	    		except:
				continue
	except:
		pass
	return l

def get_all_the_urls(list_of_urls):
	list_of_urls = list(list_of_urls)
	for url in list_of_urls:
		size1 = len(list_of_urls)
		print('size1 : '+str(size1))
		s  = get_list_of_urls(url)
		for i in s:
			list_of_urls.append(i)
			print(len(list_of_urls))
		print('size2 : '+str(len(list_of_urls)))
		if(size1==len(list_of_urls)):
			return list_of_urls

def get_all_the_urls1(list_of_urls,depth):
	if depth == 2:
		return 
	else:   
		depth = depth  + 1
                print(depth)
		for i in list_of_urls:
			s = get_list_of_urls(i)
			get_all_the_urls1(s,depth)
			for j in s:
				final_list.add(j)
		
		



base = set()
base.add('https://www.reddit.com/')
t = time.time()
print(t)
get_all_the_urls1(base,0)
print('it took ' + str(time.time()-t))
#print(type(urls))
f = open('links.txt','w')
for  url in final_list:
	print(url)
	f.write(url)
	f.write('\n')
   

#a = set()
#a.add('a')
#a.add('b')
#a.add('c')

#b = set()
#b.add('1')
#b.add('2')
#b.add('3')

#k = a.union(b)
#print(k)
#print(len(k))


