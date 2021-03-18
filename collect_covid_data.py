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
        table = self.__soup.find(id="main_table_countries_today") # locating the table in the html
        datalist = []
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            tempCol = []
            for data in cols[:-4]:
                tempCol.append(self.__clean_String(data.text))
            tempCol.pop(7)
            datalist.append(tempCol)
            return datalist[8:-8]  # Getting rid of the first lines and the last ones that are not useful

    # This method takes as input a string and then cleans it from the unnecessary characters.
    def __clean_String(self, strData):
        tempStr = ''
        tempStr = re.sub('\n|\+|\s\s+|,', '', strData)
        if tempStr == '':
            return None
        elif re.match('\d.\d', tempStr):  # the string contains a float digit, it casts it and returns the value
            return float(tempStr)
        elif re.match('\d', tempStr):  # the string contains a int digit, it casts it and returns the value
            return int(tempStr)
        else:
            return tempStr  # returns the string if it is ok
