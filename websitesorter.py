#Website subdomain sorter
import re
dict = {}

counts = ["900,google.com","60,mail.yahoo.com","10,mobile.sports.yahoo.com","40,sports.yahoo.com","300,yahoo.com","10,stackoverflow.com","20,overflow.com","5,com.com",
"2,en.wikipedia.org","1,m.wikipedia.org","1,mobile.sports","1,google.co.uk"]

def subdomain(dict,i):
    items = i.split(",")
    for i in items:
        if items[1] in dict:
            ("print in")
        else:
            dict.append(i)
    print(dict)
    


for i in counts:
    subdomain(dict,i)



    