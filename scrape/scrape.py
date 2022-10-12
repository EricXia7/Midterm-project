import os
import shutil
import csv
import requests
from bs4 import BeautifulSoup


def findname(table):
    '''
      Scrape hotels names as a string
    '''
    h_name= table.find('div',{'class': 'fcab3ed991 a23c043802'}).text
    return h_name


def findprice(table):
    '''
      Scrape hotel price as a float
    '''
    elt= table.find('div',{'data-testid': 'price-and-discounted-price'})
    if(elt==None): 
        tmp= str(table)[str(table).find('$'):]
        h_price=tmp[:tmp.find('<')]
    else:
        h_price = elt.text
    return float(h_price.replace(' ', ' ').replace('$','').replace(',',''))


def findscore(table):
    """
      Scrape hotel rating score as a string
    """
    elt = table.find('div',{'class': "b5cd09854e d10a6220b4"})
    if(elt==None):
        h_score = ''
    else:
        h_score = elt.text
    return h_score


def finddis(table):
    '''
      Scrape the distance of hotels from city centre as a string
    '''

    return


def crawl_booking_data(year,month):
    '''
    scrape the information from booking.com then return a list of hotel information 
    The list element for hotels is['name','price','score','dis']
    '''
    return




