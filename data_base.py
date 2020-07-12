"""

DATA base and its essential tables creations

"""
import sqlite3


db=sqlite3.connect('Bank.db')
c=db.cursor()

# execute 1st and comment it after word and proceed to 2nd
#---------------creating frst Registration table----------------------------------------------

'''
c.execute("create table regis(UNAME text,UPASS text,UCN text)")

'''

# execute 2st and comment it after word and proceed to 3nd
#---------------creating acccount opening table-----------------------------------------------

c.execute("create table account(ac_no Interger,f_name Text,city Text,amount Interger)")

db.commit()
db.close()
