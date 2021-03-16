import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime


class ScrapeData:
    def __init__(self):
        self.__url = "https://www.worldometers.info/coronavirus/"
        self.__console_interaction()
        self.__soup = ''
        # self.__store_data()

    def __console_interaction(self):
        print('Type "help" to see more commands')
        command = ''
        while True:
            command = input('> ').lower()
            if command == 'help':
                print('''
                download data - to download html to a local file
                scrape data - to scrape from a local file
                quit - to end the program
                ''')
            elif command == 'download data':
                self.__download_html()
            elif command == 'scrape data':
                self.__soup = self.__parse_html()
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

    def __parse_html(self):
        with open("local_html/local_file2021-03-15.html", encoding="utf-8") as html:
            return BeautifulSoup(html.read(), "html.parser")

    def __store_data(self):
        table = self.__soup.find(id="main_table_countries_today")
        print(table)