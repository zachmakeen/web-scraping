from database_api import DatabaseAPI
import pandas as pd


class ExtractData:
    def __init__(self):
        self.__connection = self.__create_connection()
        self.__corona_df = self.__extract_corona_records()
        self.__border_df = self.__extract_border_records()

    # Creates a new connection to the database
    def __create_connection(self):
        db_api = DatabaseAPI('covid_corona_db_MAKE_RIVA')
        return db_api.create_connection()

    # Extracts the records from the corona_table
    def __extract_corona_records(self):
        return pd.read_sql('SELECT * FROM corona_table', con=self.__connection)

    # Extracts the records from the country_borders_table
    def __extract_border_records(self):
        return pd.read_sql('SELECT * FROM country_borders_table', con=self.__connection)

    # Returns the corona dataframe
    def get_corona_df(self):
        return self.__corona_df

    # Returns the border dataframe
    def get_border_df(self):
        return self.__border_df
