import datetime
import re
import urllib
from urllib.request import Request, urlopen
from add_data_to_database import CreateDatabase
from bs4 import BeautifulSoup


class ScrapeAndSaveData:
    def __init__(self, url='https://www.worldometers.info/coronavirus/', current_date=str(datetime.date.today()), current_year=int(datetime.datetime.now().strftime('%Y')), current_month=int(datetime.datetime.now().strftime('%m'))):
        self.__url = url
        self.__current_date = current_date
        self.__current_year = current_year
        self.__current_month = current_month
        self.__user_day = None

        # Save file locally

        # self.__download_html()

        # Scrape local file

        self.__user_day = int(input('Enter the day in digits to scrape your local file (e.g. 05): '))
        today_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date())
        yesterday_date = str(
            datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(
                days=1))
        yesterday2_date = str(
            datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(
                days=2))
        soup = self.__parse_html()
        today_data = self.__generate_data_list(soup.find(id='main_table_countries_today'))
        yesterday_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday'))
        yesterday2_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday2'))
        today_table = CreateDatabase(today_date)
        yesterday_table = CreateDatabase(yesterday_date)
        yesterday2_table = CreateDatabase(yesterday2_date)
        today_table.store_data(today_data)
        yesterday_table.store_data(yesterday_data)
        yesterday2_table.store_data(yesterday2_data)

    def console_interaction(self):
        print("""
save data - to download html to a local file
scrape data - to scrape from a local file
quit - to end the program
                """)
        while True:
            command = input('> ').lower()
            if command == 'save data':
                self.__download_html()
            elif command == 'scrape data':
                self.__user_day = int(input('Enter the day in digits to scrape your local file (e.g. 05): '))
                today_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date())
                yesterday_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(days=1))
                yesterday2_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(days=2))
                soup = self.__parse_html()
                today_data = self.__generate_data_list(soup.find(id='main_table_countries_today'))
                yesterday_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday'))
                yesterday2_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday2'))
                today_table = CreateDatabase(today_date)
                yesterday_table = CreateDatabase(yesterday_date)
                yesterday2_table = CreateDatabase(yesterday2_date)
                today_table.store_data(today_data)
                yesterday_table.store_data(yesterday_data)
                yesterday2_table.store_data(yesterday2_data)
            elif command == 'quit':
                break
            else:
                print('Sorry, that is not a valid command.')

    def __download_html(self):
        try:
            request = Request(self.__url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(request).read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            with open("local_html/" + f"local_file{self.__current_date}.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())
        except urllib.error.HTTPError as error:
            print(error)

    def __parse_html(self):
        print(f"local_html/local_file{self.__current_year}-{datetime.datetime.now().strftime('%m')}-{self.__user_day}.html")
        with open(f"local_html/local_file{self.__current_year}-{datetime.datetime.now().strftime('%m')}-{self.__user_day}.html", encoding="utf-8") as html:
            return BeautifulSoup(html.read(), "html.parser")

    def __generate_data_list(self, table_row_list):
        data = self.__clean_table_row(table_row_list.find_all('tr'))
        return data

    def __clean_table_row(self, table_row_list):
        clean_data = []
        for table_row in table_row_list[1:]:
            temp_table_row = []
            table_entry_list = table_row.find_all('td')
            for table_entry in table_entry_list:
                temp_table_row.append(self.__clean_table_entry(table_entry.text))
            temp_table_row.pop(7)
            clean_data.append(tuple(temp_table_row))
        return clean_data[8:-8]

    def __clean_table_entry(self, table_entry):
        table_entry = re.sub(r'\n|\+|\s{2,}|,', '', table_entry)
        if table_entry == '':
            return None
        elif type(table_entry) is float:
            return float(table_entry)
        elif type(table_entry) is int:
            return int(table_entry)
        else:
            return table_entry
