import datetime

from save_file import SaveFile
from scrape_file import ScrapeFile
from clean_data import CleanData
from database_management import ManageDatabase


class ScrapeSaveData:
    def __init__(self):
        self.__user_day = None  # Used to store the day of the file that the user desires to scrape

    # Allows the user to interact with the modules in order to save or scrape data
    def interact(self):
        # Prints the list of available commands
        print('''
help - to see the list of available commands
save - to save html locally
scrape - to scrape local html file
back - to go analyze data or exit the program
        ''')
        while True:
            command = input('> ').lower()
            if command == 'help':
                print('''
help - to see the list of available commands
save - to save html locally
scrape - to scrape local html file
back - to go analyze data or exit the program
                ''')
            elif command == 'save':
                # Saves HTML file locally
                save_object = SaveFile()
                save_object.save_html()
            elif command == 'scrape':
                # Scrapes file specified by date entered by user
                while True:
                    try:
                        self.__user_day = int(input('Enter day here: '))
                    except ValueError:
                        print('Sorry, that is not a valid date')
                        continue
                    else:
                        break
                scrape_object = ScrapeFile(self.__user_day)
                html_soup = scrape_object.parse_html()  # Reads HTML code and creates BeautifulSoup object
                json_list = scrape_object.parse_json()  # Reads JSON and stores into a list of dictionaries

                # Cleans HTML code and JSON list and returns list of tuples
                clean_object = CleanData(html_soup, json_list)
                user_date = datetime.datetime.strptime(scrape_object.get_file_date(), '%Y-%m-%d').date()  # Creates a date object using __user_day
                today_data = clean_object.generate_covid_list('main_table_countries_today', str(user_date))  # generates list using covid data from the user_date
                yesterday_data = clean_object.generate_covid_list('main_table_countries_yesterday',
                                                                  str(user_date - datetime.timedelta(days=1)))  # generates list using covid data from yesterday in relation to the user_date
                yesterday2_data = clean_object.generate_covid_list('main_table_countries_yesterday2',
                                                                   str(user_date - datetime.timedelta(days=2)))  # generates list using covid data from before yesterday in relation to the user_date
                country_border_data = clean_object.generate_border_list()

                # Creates database with covid and border data
                db_object = ManageDatabase()
                db_object.add_covid_records(today_data + yesterday_data + yesterday2_data)  # Adds covid data from the 3 days into corona_table
                db_object.add_border_records(country_border_data)  # Adds border details about each country into country_borders_table
            elif command == 'back':
                break
            else:
                print('Sorry, that is not a valid command.')
