''' to do: remove the &nbps; probably using html tidy

http://countergram.com/open-source/pytidylib/docs/index.html
http://www.voidspace.org.uk/python/articles/urllib2.shtml

the basic tech works now, but I need to 

1) figure out the database model
2) and how to automate the pulling of all the stocks, probably using a database lookup
3) After the call to split, how do I store the data to sqlite3, I need to walk through the 
list returned by .split(), there are some tricky parts here.
4) Need to figure out how to store the date info from pse to TEXT format of SQLite3, this will 
impact the way I mine the data.



'''

import urllib2
import re

url = "http://www.pse.com.ph/html/MarketInformation/historicalprices.jsp?securitySymbol=jfc"
response = urllib2.urlopen(url)
html = response.read()

p = re.compile(r'<.*?>')
clean_data = p.sub('',html)

q = re.compile(r'&nbsp;')
clean_data2 = q.sub('',clean_data)

'''print clean_data2.split()'''

getout = false
counter = 0
while not getout:
	if clean_data2[counter] = "value":
		
	else:
		
		
		
		
	

