#make a csv file of all stock tickers found on finwiz.com
#this makes it easier to make lists that access all ticker symbols
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import csv
import pandas as pd
from pandas import DataFrame, read_csv


#Save all of the ticker symbols onto an array and then save to a csv file
def make_tickers_csv():
    ticker_list = []
    page_number = 1
    page_numbers = []

    #make a number array to make iteration easier in the future
    for i in range(373):
        page_numbers.append(page_number)
        page_number += 20

    #iterate through the websites using beautifulsoup and urllib
    #this for loop creates the ticker array
    for number in page_numbers:
        #opens a certain page of tickers depending on the munber given in the number array
        url = 'https://finviz.com/screener.ashx?v=120&r={}'.format(number)
        url_opened = urlopen(url)
        soup = BeautifulSoup(url_opened, 'html.parser')

        #finds all of the tickers' links on the page
        #then deletes unnecessary information and adds it to the list 
        for a in soup.find_all('a', class_ = 'screener-link-primary'):
            link_old = a.get('href')
            link_new = link_old[13:].replace('&ty=c&p=d&b=1','')
            ticker_list.append(link_new)
        print(number)

    #turns the array into a csv with one column and rows that are tickers
    with open("All_Tickers_col.csv", 'w') as resultFile:
        wr = csv.writer(resultFile, dialect = 'excel')
        wr.writerow(['ticker'])
        for val in ticker_list:
            wr.writerow([val])


#turns the ticker csv into a list
def tickers_to_list():
    a = []
    df = pd.read_csv('All_Tickers_col.csv')
    a = df['ticker'].tolist()


