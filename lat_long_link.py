import csv
import webbrowser
import time
from selenium import webdriver
import pandas as pd


df = pd.read_csv(r"\google_map_business_data.csv")
driver = webdriver.Chrome()

import csv

lod = []  # Assuming 'lod' is defined outside the loop

for i in df.to_dict('records'):
    try:
        my_dict = {}
        my_dict['city'] = i['city']
        my_dict['name'] = i['name']
        my_dict['rating'] = i['rating']
        my_dict['users'] = i['people']
        url = i['url']
        driver.get(url)
        time.sleep(3)
        current_url = driver.current_url

        my_dict['url'] = current_url
        lod.append(my_dict)
    except:
        pass


df = pd.DataFrame(lod)
def do_somrthing(link,count):
    try:
        value = link.split('@')[1]
        return value.split(',')[count]
    except:
        return '-'
df['lat'] = df['url'].apply(lambda x : do_somrthing(x,0))
df['long'] = df['url'].apply(lambda x : do_somrthing(x,1))
df.to_csv('output.csv')
