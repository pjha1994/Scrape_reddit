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

f = open('links.txt','r')
for i in f:
	soup = make_soup(i)
	for img in soup.find_all('img'):
		print(img['src'])
