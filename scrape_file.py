from bs4 import BeautifulSoup as bs
import datetime
import json


class ScrapeFile:
    def __init__(self, user_day):
        self.__user_day = user_day
        self.__file_date = self.__format_file_date()

    # Formats the date using the user_day
    def __format_file_date(self):
        current_year = datetime.datetime.now().strftime('%Y')  # Gets the current year
        current_month = datetime.datetime.now().strftime('%m')  # Gets the current month
        return f'{current_year}-{current_month}-{self.__user_day}'

    # Reads the HTML file
    def parse_html(self):
        with open(f"local_html/local_file{self.__file_date}.html", encoding="utf-8") as html:
            return bs(html.read(), "html.parser")  # Reads the HTML file and returns a BeautifulSoup object

    # Reads the JSON file
    def parse_json(self):
        with open('countries_json/country_neighbour_dist_file.json') as f:
            return json.load(f)  # Returns the JSON as a list of dictionaries

    # Returns the formatted date
    def get_file_date(self):
        return self.__file_date
