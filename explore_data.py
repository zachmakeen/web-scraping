import re

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


class ExploreData:
    def __init__(self, country, corona_df, border_df):
        self.__country = country
        self.__corona_df = corona_df
        self.__border_df = border_df

        print(self.__corona_df)

        # print(self.__corona_df.info())
        # print(self.__border_df.info())

        # print(self.__corona_df.axes)
        # print(self.__border_df.axes)

        # print(self.__corona_df.loc[1])

    def get_six_days_evolution(self):
        return self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country, ["Date", "NewCases", "NewDeaths", "NewRecovered"]]

    def get_six_days_neighbours(self):
        # getting the country with the longest border
        neighbours_countries = self.__border_df.loc[
            self.__border_df["Country,Other"] == self.__country, ["Country,Other", "Neighbour", "Distance"]]

        final= neighbours_countries.loc[neighbours_countries['Distance'] == neighbours_countries['Distance'].max(), ["Neighbour"]]
        print(final)


