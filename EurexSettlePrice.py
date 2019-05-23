# -*- coding: utf-8 -*-
 
import requests
from bs4 import BeautifulSoup
import unicodecsv

file = open('EurexSettle.csv', 'wb')
csvCursor = unicodecsv.writer(file,encoding='utf-8-sig')
Header = [u'Contract', u'Product', u'SettlePrice', u'SettleDate']

Data = []
url = "http://www.eurexchange.com/exchange-en/products/idx/dax/DAX--Futures/17206"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FDAX = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text   
Data.append(CT)
Data.append('FDAX')
Data.append(FDAX)
Data.append(LT)
csvCursor.writerow(Header)
csvCursor.writerow(Data)


Data = []   
url = "http://www.eurexchange.com/exchange-en/products/idx/stx/blc/EURO-STOXX-50--Index-Futures/18954"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FESX = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text          
Data.append(CT)
Data.append('FESX')
Data.append(FESX)
Data.append(LT)
csvCursor.writerow(Data)   
 

Data = []    
url = "http://www.eurexchange.com/exchange-en/products/idx/stx/esf/EURO-STOXX--Banks-Futures/17494"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FESB = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text
Data.append(CT)
Data.append('FESB')
Data.append(FESB)
Data.append(LT)
csvCursor.writerow(Data) 

   
Data = []    
url = "http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Buxl--Futures/15202"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FGBX = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text   
Data.append(CT)
Data.append('FGBX')
Data.append(FGBX)
Data.append(LT)
csvCursor.writerow(Data) 


Data = []   
url = "http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Bund-Futures/14770"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FGBL = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text   
Data.append(CT)
Data.append('FGBL')
Data.append(FGBL)
Data.append(LT)
csvCursor.writerow(Data) 


Data = []  
url = "http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Bobl-Futures/15644"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FGBM = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text
Data.append(CT)
Data.append('FGBM')
Data.append(FGBM)
Data.append(LT)
csvCursor.writerow(Data) 


Data = []      
url = "http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Schatz-Futures/16134"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FGBS = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text
Data.append(CT)
Data.append('FGBS')
Data.append(FGBS)
Data.append(LT)
csvCursor.writerow(Data) 


Data = [] 
url = "http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Long-Term-Euro-BTP-Futures/16138"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FBTP = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text
Data.append(CT)
Data.append('FBTP')
Data.append(FBTP)
Data.append(LT)
csvCursor.writerow(Data) 
   
 
Data = [] 
url = "http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-OAT-Futures/154590"
html = requests.get(url)
html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'lxml')
CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
table = sp.find("table", {"class" : "dataTable"})
rows = sp.find_all('table')[0].tbody.findAll('tr')
for row in rows:
    FOAT = row.find_all('td')[11].text
for row in rows:
    LT = row.find_all('td')[15].text
Data.append(CT)
Data.append('FOAT')
Data.append(FOAT)
Data.append(LT)
csvCursor.writerow(Data) 

output.close()

