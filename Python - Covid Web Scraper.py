# Covid site scraper
# Take the covid status page and scrape the data to be distributed

import requests
import pandas as pd
from urllib.request import HTTPDigestAuthHandler, urlopen
from bs4 import BeautifulSoup
import csv 

state = "NSW".lower()
url = (f"https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19/current-status/contact-tracing#{state}")
print(url)

html = urlopen(url).read()
bs = BeautifulSoup(html,features='html.parser')
div = bs.find("div", {"id:""nsw_iev_table_container_165512"})
table = bs.findAll(lambda tag: tag.name=='table') 
rows = table.findAll(lambda tag: tag.name=='tr')

data_frame= []
for tr in rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    data_frame.append(row)
    
table = pd.DataFrame(data_frame, columns=['Date','Place','Suburb','Arrival Time','Departure Time'])
print(table)
table.to_csv((f'covid-list-{state}.csv'),index=False)