#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
from bs4 import BeautifulSoup
import time 

url = urllib.request.urlopen('https://gol.gg/players/list/season-S9/split-Summer/tournament-ALL/position-ALL/week-ALL/').read()

bs = BeautifulSoup(url,"html.parser")

table = bs.find("table", {"class": "table_list playerslist tablesaw trhover"})

a = list()
rowsTbody  = table.find_all('td')
for row1 in rowsTbody:
     a.append(row1.get_text()) 
        
import sqlite3
sql = sqlite3.connect('db.sqlite3')
cur = sql.cursor()


c = list()
cont = 0
cont2 = 1
for y in a:
    c.append(y)
    cont = cont + 1
    if cont == 23:
        c.append(cont2)
        cont2 = cont2 + 1
        print(c)
        print('-----------------------')
        cur.execute("INSERT INTO portafolio_players VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", c)
        sql.commit()
        for q in range(0,24):
            del(c[-1])
        
        cont = 0
sql.close()

