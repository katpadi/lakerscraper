#!/usr/bin/python
"""
Extracting using BeautifulSoup and requests

Assumption:
http://doc.scrapy.org/en/latest/topics/ubuntu.html#topics-ubuntu

How to run:
  scrapy runspider myspider.py
"""
from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
#import csv
import requests
from bs4 import BeautifulSoup

SITE_BASE_URL = "http://www.nba.com/schedules/intl.html?RID=26&cName=Philippines#"

def get_source():
  team = 'LAL'
  response = requests.get(SITE_BASE_URL + team)
  if response.status_code == 200:
    soup = BeautifulSoup(response.text)
    element = soup.find(id="games-scrollermodule")
    if element:
      return element
    return None
  else:
    raise Exception("Div not found.")

def get_sched():
  tbl = get_source()
  for row in tbl.findAll("tr"):
    cols = row.findAll("td")
    # matchup
    visitor = cols[0].find("span", {"class":"visitor"}).text
    home = cols[0].find("span", {"class":"home"}).text
    # channel
    broadcaster = cols[1].find("span").text
    print ("matchup: {} vs. {} channel: {}".format(visitor,home,broadcaster))

if __name__ == '__main__':
  import argparse
  #output_file = open('sched.csv', 'w')
  get_sched()
