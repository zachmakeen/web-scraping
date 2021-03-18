import pandas
import urllib
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime


class ScrapeData:
    def __init__(self):
        self.__url = "https://www.worldometers.info/coronavirus/"
        self.__headers = ['#', 'Country, Other', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths',
                          'Total Recovered', 'Active Cases', 'Serious, Critical', 'Tot Cases/1M pop', 'Deaths/1M pop',
                          'Total Tests', 'Tests/1M pop', 'Population']
        self.__soup = self.__parse_html(18)
        self.__table_id_list = ['main_table_countries_today', 'main_table_countries_yesterday',
                                'main_table_countries_yesterday2']
        self.__today_data_frame = self.__generate_dataframe(self.__soup.find(id=self.__table_id_list[0]).find_all('tr'))
        # self.__yesterday_data_frame = self.__generate_dataframe(self.__soup.find(id=self.__table_id_list[1]).find_all('tr'))
        # self.__yesterday2_data_frame = self.__generate_dataframe(self.__soup.find(id=self.__table_id_list[2]).find_all('tr'))

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

    def __parse_html(self, date):
        with open(f"local_html/local_file{datetime.now().strftime('%Y')}-{datetime.now().strftime('%m')}-{date}.html",
                  encoding="utf-8") as html:
            return BeautifulSoup(html.read(), "html.parser")

    def __generate_dataframe(self, table_row_list):
        data = self.__clean_table_row(table_row_list)
        covid_data_frame = pandas.DataFrame(data, columns=self.__headers)
        print(covid_data_frame)
        return covid_data_frame

    def __clean_table_row(self, table_row_list):
        clean_data = []
        for table_row in table_row_list[1:]:
            table_entry_list = table_row.find_all('td')
            temp_table_row = []
            for table_entry in table_entry_list[:-4]:
                temp_table_row.append(self.__clean_table_entry(table_entry.text))
            temp_table_row.pop(7)
            clean_data.append(temp_table_row)
        return clean_data[8:-8]

    def __clean_table_entry(self, table_entry):
        table_entry = re.sub('\n|\+|\s\s+|,', '', table_entry)
        if table_entry == '':
            return None
        elif re.match('\d.\d', table_entry):
            return float(table_entry)
        elif re.match('\d', table_entry):
            return int(table_entry)
        else:
            return table_entry
