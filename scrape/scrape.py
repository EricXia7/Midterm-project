import os
import shutil
import csv
import requests
from bs4 import BeautifulSoup


def findname(table):
    '''
      Scrape hotel name as a string
    '''
    h_name= table.find('div',{'class': 'fcab3ed991 a23c043802'}).text
    return h_name


def findprice(table):
    '''
      Scrape hotel price as a float
    '''
    return


def findscore(table):
    """
      Scrape hotel rating score as a string
    """
    return


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




