import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import re


class ScrapeData:
    def __init__(self):
        self.__url = "https://www.worldometers.info/coronavirus/"
        self.__console_interaction()
        self.__soup = ''
        #self.__store_data()

    def __console_interaction(self):
        print('Type "help" to see more commands')
        command = ''
        while True:
            command = input('> ').lower()
            if command == 'help':
                print("""
                download data - to download html to a local file
                scrape data - to scrape from a local file
                quit - to end the program
                """)
            elif command == 'download data':
                self.__download_html()
            elif command == 'scrape data':
                inDate = input('enter the day')
                self.__soup = self.__parse_html(inDate)
            elif command == 'store':
                self.__store_data()
            elif command == 'quit':
                break
            else:
                print('Sorry, that is not a valid command.')

    def __download_html(self):
        try:
            request = Request(self.__url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(request)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            with open("local_html/" + f"local_file{datetime.date.today()}.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())
        except urllib.error.HTTPError as error:
            print(error)

    def __parse_html(self,inDate):
        with open(f"local_html/local_file2021-03-{inDate}.html", encoding="utf-8") as html:
            return BeautifulSoup(html.read(), "html.parser")

    def __store_data(self):
        table = self.__soup.find(id="main_table_countries_today")
        #countries = table.findAll('a', class_="mt_a")
        #treven = table.find_all('td')
        #print(len(countries))
        datalist = []
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            temlist = []
            for data in cols[:-4]:
                h = data.text
                h= re.sub('\n|\+|\s\s+|,', '', h)
                if h == '':
                    h = None
                elif re.match('\d.\d',h):
                    h = float(h)
                elif re.match('\d',h):
                    h = int(h)
                temlist.append(h)
            temlist.pop(7)
            datalist.append(temlist)

        for i in datalist[8:-8]:
            print(i)
