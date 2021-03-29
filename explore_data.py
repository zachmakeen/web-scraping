import re

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from functools import reduce
import pandas as pd


class ExploreData:
    def __init__(self, country, corona_df, border_df):
        self.__country = country
        self.__corona_df = corona_df
        self.__border_df = border_df
        self.__country_neighbour = self.get_farther_neighbour()
        self.__many_neighbours = self.get_many_neighbours()

    def get_six_days_evolution(self):
        return self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country, ["Date", "NewCases", "NewDeaths", "NewRecovered"]]

    def get_farther_neighbour(self):
        # getting the country with the longest border
        neighbours_countries = self.get_neighbour_countries()

        # Getting the name of the country with the longest border
        return (neighbours_countries.loc[
            neighbours_countries['Distance'] == neighbours_countries['Distance'].max(), ["Neighbour"]]).iloc[0][
            'Neighbour']

    def get_neighbour_countries(self):
        return self.__border_df.loc[
            self.__border_df["Country,Other"] == self.__country, ["Neighbour", "Distance"]]

    def get_many_neighbours(self):
        neighbours_countries = self.get_neighbour_countries().sort_values(by='Distance', ascending=False)

        return neighbours_countries.loc[
            neighbours_countries['Distance'] == neighbours_countries['Distance'], ["Neighbour"]].head(3).values

    def get_neighbour(self):
        return self.__country_neighbour

    def get_six_days_newCases(self):
        main_country_df = self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country, ["Date", "NewCases"]]
        df1 = main_country_df.rename({"NewCases": f'Newcases-{self.__country}'}, axis='columns')

        neighbour_country_df = self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country_neighbour, ["Date", "NewCases"]]
        df2 = neighbour_country_df.rename({'NewCases': f'Newcases-{self.__country_neighbour}'}, axis='columns')

        return pd.merge(df1, df2)

    def get_six_days_Deaths(self):
        neighbours_countries = self.get_many_neighbours()
        data_frames = []
        main_country_df = self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country, ["Date", "Deaths/1M pop"]]
        df1 = main_country_df.rename({"Deaths/1M pop": f'Deaths/1M pop-{self.__country}'}, axis='columns')
        data_frames.append(df1)


        for i in neighbours_countries:
            country_df = self.__corona_df.loc[
                self.__corona_df["Country,Other"] == i[0], ["Date", "Deaths/1M pop"]]
            temp_df = country_df.rename({"Deaths/1M pop": f'Deaths/1M pop-{i[0]}'}, axis='columns')
            data_frames.append(temp_df)

        return reduce(lambda left, right: pd.merge(left, right, on=['Date'], how='outer'), data_frames)
