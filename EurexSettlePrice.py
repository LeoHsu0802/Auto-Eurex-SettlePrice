# -*- coding: utf-8 -*-
 
import requests
from bs4 import BeautifulSoup
import unicodecsv

file = open('EurexSettle.csv', 'wb')
csvCursor = unicodecsv.writer(file,encoding='utf-8-sig')
Header = [u'Contract', u'Product', u'SettlePrice', u'SettleDate']

def EurexSettle(url,Name):
    Data = []
    html = requests.get(url)
    html.encoding="utf-8"
    sp = BeautifulSoup(html.text, 'lxml')
    CT = sp.find('select', {'id':'maturityDate'}).findAll('option')[0].text
    rows = sp.find_all('table')[0].tbody.findAll('tr')
    for row in rows:
        SettlePrice = row.find_all('td')[11].text
    for row in rows:
        LT = row.find_all('td')[15].text   
    Data.append(CT)
    Data.append(Name)
    Data.append(SettlePrice)
    Data.append(LT)
    csvCursor.writerow(Header)
    csvCursor.writerow(Data)
    
EurexSettle ("http://www.eurexchange.com/exchange-en/products/idx/dax/DAX--Futures/17206",'FDAX')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/idx/stx/blc/EURO-STOXX-50--Index-Futures/18954",'FESX')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/idx/stx/esf/EURO-STOXX--Banks-Futures/17494",'FESB')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Buxl--Futures/15202",'FGBX')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Bund-Futures/14770",'FGBL')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Bobl-Futures/15644",'FGBM')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-Schatz-Futures/16134",'FGBS')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Long-Term-Euro-BTP-Futures/16138",'FBTP')
EurexSettle ("http://www.eurexchange.com/exchange-en/products/int/fix/government-bonds/Euro-OAT-Futures/154590",'FOAT')

output.close()

