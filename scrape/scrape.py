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
    data = []  
    h_names =[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    for i in range(10): 

        url = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaLACiAEBmAExuAEHyAEP2AEB6AEB-AECiAIBqAIDuAKnzYuaBsACAdICJGRlYTQ0OTAxLTJjYjEtNGQ5Yi1iZWIyLTFkYzNhNjY4YWVmZtgCBeACAQ&sid=97ce27f6e33910f88c17fb7c197ba18b&aid=304142&tmpl=searchresults&ac_click_type=b&ac_position=0&checkin_month='+month+'&checkin_monthday=21&checkin_year='+year+'&checkout_month='+month+'&checkout_monthday=27&checkout_year='+year+'&class_interval=1&dest_id=20126394&dest_type=city&dtdisc=0&efdco=1&from_sf=1&group_adults=2&group_children=0&iata=AUS&inac=0&index_postcard=0&label_click=undef&lang=en-us&no_rooms=1&offset='+str(i*25)+'&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&soz=1&src=index&src_elem=sb&srpvid=06a07270f9440067&ss=Austin%2C+Texas%2C+United+States&ss_all=0&ss_raw=austin&ssb=empty&sshis=0&ssne=New+York&ssne_untouched=New+York&lang_click=other&cdl=zh-cn&lang_changed=1'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        tables = soup.find_all('div', {'class': 'a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942'})
        for table in tables:
            h_name = findname(table)
            h_price = findprice(table)
            h_score = findscore(table)
            h_dis = finddis(table)
            if(h_name not in h_names and len(h_score)>0 and len(h_dis)>0):
                data.append([h_name,h_price,float(h_score),float(h_dis)])
                h_names.append(h_name)
    return data




if __name__ == '__main__':
    header = ['name','price','score','dis']
    filepath = 'out/'


    if not os.path.exists('out/'):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath,ignore_errors=True)
        os.mkdir(filepath)

    for month in [1,11,12]:
        year = '2022'
        if(month==1):
            year='2023'
        data = crawl_booking_data(year,str(month))


        with open (filepath+year+str(month)+'.csv','w',encoding='utf-8',newline='') as fp:
            writer =csv.writer(fp)
            writer.writerow(header)
            writer.writerows(data)