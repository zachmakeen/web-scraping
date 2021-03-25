import datetime
import re
import urllib
import json
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

        # self.__user_day = int(input('Enter the day in digits to scrape your local file (e.g. 05): '))
        # today_date = str(datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date())
        # yesterday_date = str(
        #     datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(
        #         days=1))
        # yesterday2_date = str(
        #     datetime.datetime(self.__current_year, self.__current_month, self.__user_day).date() - datetime.timedelta(
        #         days=2))
        # soup = self.__parse_html()
        # today_data = self.__generate_data_list(soup.find(id='main_table_countries_today'), today_date)
        # yesterday_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday'), yesterday_date)
        # yesterday2_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday2'), yesterday2_date)
        # all_data = today_data + yesterday_data + yesterday2_data
        # db_obj = CreateDatabase()
        # db_obj.store_data(all_data, 'corona_table')
        self.__parse_json()

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
                today_data = self.__generate_data_list(soup.find(id='main_table_countries_today'), today_date)
                yesterday_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday'), yesterday_date)
                yesterday2_data = self.__generate_data_list(soup.find(id='main_table_countries_yesterday2'), yesterday2_date)
                all_data = today_data + yesterday_data + yesterday2_data
                # connecting to database
                db_obj = CreateDatabase()
                db_obj.store_data(all_data, 'corona_table')
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

    def __parse_json(self):
        with open('countries_json/country_neighbour_dist_file.json') as f:
            data = json.load(f)
            temp_list = []
            for i in data:
                countries = list(i.values())[0]
                num_countries = (len(list(countries.keys())))
                for j in range(num_countries):
                    temp_tuple = [list(i.keys())[0], list(countries.keys())[j], list(countries.values())[j]]
                    temp_list.append(tuple(temp_tuple))
            print(temp_list)
            return temp_list

    def __generate_data_list(self, table_row_list, date):
        data = self.__clean_table_row(table_row_list.find_all('tr'), date)
        return data

    def __clean_table_row(self, table_row_list, date):
        clean_data = []
        for table_row in table_row_list[1:]:
            temp_table_row = [date]
            table_entry_list = table_row.find_all('td')
            for table_entry in table_entry_list:
                temp_table_row.append(self.__clean_table_entry(table_entry.text))
            clean_data.append(tuple(temp_table_row))
        return clean_data[8:-8]

    def __clean_table_entry(self, table_entry):
        table_entry = re.sub(r'\n|\+|\s{2,}|,|N/A', '', table_entry)
        if table_entry == '':
            return None
        elif re.match(r'^\d+$', table_entry):
            return int(table_entry)
        else:
            return table_entry
