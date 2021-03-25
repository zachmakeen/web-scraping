import datetime

from save_file import SaveFile
from scrape_file import ScrapeFile
from clean_data import CleanData
from database_management import ManageDatabase


class ScrapeSaveData:
    def __init__(self):
        self.__user_day = None

        # Save HTML locally
        save_object = SaveFile()
        save_object.save_html()

        # Scrape file specified by date entered by user
        self.__user_day = 15
        scrape_object = ScrapeFile(self.__user_day)
        html_soup = scrape_object.parse_html()
        json_list = scrape_object.parse_json()

        # Clean html code and json list of dictionaries and returns list of tuples
        clean_object = CleanData(html_soup, json_list)
        user_date = datetime.datetime.strptime(scrape_object.get_file_date(), '%Y-%m-%d').date()
        today_data = clean_object.generate_covid_list('main_table_countries_today', str(user_date))
        yesterday_data = clean_object.generate_covid_list('main_table_countries_yesterday', str(user_date - datetime.timedelta(days=1)))
        yesterday2_data = clean_object.generate_covid_list('main_table_countries_yesterday2', str(user_date - datetime.timedelta(days=2)))
        country_border_data = clean_object.generate_border_list()
        # country_name_data = clean_object.generate_country_list()

        # Create database with all the data
        db_object = ManageDatabase()
        db_object.add_covid_records(today_data + yesterday_data + yesterday2_data)
        db_object.add_border_records(country_border_data)
