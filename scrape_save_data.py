import datetime
import pandas
import re
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class ScrapeAndSaveData:
    def __init__(self, url='https://www.worldometers.info/coronavirus/', current_date=str(datetime.date.today()), current_year=int(datetime.datetime.now().strftime('%Y')), current_month=int(datetime.datetime.now().strftime('%m')), headers=['#', 'Country, Other', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths',
                          'Total Recovered', 'Active Cases', 'Serious, Critical', 'Tot Cases/1M pop', 'Deaths/1M pop',
                          'Total Tests', 'Tests/1M pop', 'Population']):
        self.__url = url
        self.__current_date = current_date
        self.__current_year = current_year
        self.__current_month = current_month
        self.__headers = headers
        self.__user_day = None
        self.__today_date = None
        self.__yesterday_date = None
        self.__yesterday2_date = None

        # Save file locally

        # self.__download_html()

        # Scrape local file

        # self.__user_day = int(input('Enter the day in digits to scrape your local file (e.g. 05): '))
        # self.__today_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date())
        # self.__yesterday_date = str(
        #     datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(
        #         days=1))
        # self.__yesterday2_date = str(
        #     datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(
        #         days=2))
        # soup = self.__parse_html()
        # table_id_list = ['main_table_countries_today', 'main_table_countries_yesterday',
        #                  'main_table_countries_yesterday2']
        # self.__generate_dataframe(soup.find(id=table_id_list[0]), self.__today_date)
        # self.__generate_dataframe(soup.find(id=table_id_list[1]), self.__yesterday_date)
        # self.__generate_dataframe(soup.find(id=table_id_list[2]), self.__yesterday2_date)

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
                self.__today_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date())
                self.__yesterday_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(days=1))
                self.__yesterday2_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(days=2))
                soup = self.__parse_html()
                self.__generate_dataframe(soup.find(id='main_table_countries_today'), self.__today_date)
                self.__generate_dataframe(soup.find(id='main_table_countries_yesterday'), self.__yesterday_date)
                self.__generate_dataframe(soup.find(id='main_table_countries_yesterday2'), self.__yesterday2_date)
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
        with open(f"local_html/local_file{datetime.datetime.now().strftime('%Y')}-{datetime.datetime.now().strftime('%m')}-{self.__user_day}.html", encoding="utf-8") as html:
            return BeautifulSoup(html.read(), "html.parser")

    def __generate_dataframe(self, table_row_list, date):
        data = self.__clean_table_row(table_row_list.find_all('tr'))
        covid_data_frame = pandas.DataFrame(data, columns=self.__headers)
        self.__create_json(covid_data_frame, date)

    def __create_json(self, covid_data_frame, date):
        covid_data_frame.to_json(f'covid_json/covid_data{date}.json', orient='records', lines=True)

    def __clean_table_row(self, table_row_list):
        clean_data = []
        for table_row in table_row_list[1:]:
            temp_table_row = []
            table_entry_list = table_row.find_all('td')
            for table_entry in table_entry_list[:-4]:
                temp_table_row.append(self.__clean_table_entry(table_entry.text))
            temp_table_row.pop(7)
            clean_data.append(temp_table_row)
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

    def get_today_date(self):
        return self.__today_date

    def get_yesterday_date(self):
        return self.__yesterday_date

    def get_yesterday2_date(self):
        return self.__yesterday2_date
