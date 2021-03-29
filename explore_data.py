from functools import reduce
import pandas as pd


# This class get the dataframes containing all the needed data and the country to analyze.
# Once with the information different methods are used to create a new dataframe containing
# only the required data to fulfill the requirement from explore_analyze_data

class ExploreData:
    # The constructor takes a string(country), and two data frames (corona and border)
    # so it can be used in the construction of each data frame.
    def __init__(self, country, corona_df, border_df):
        self.__country = country
        self.__corona_df = corona_df
        self.__border_df = border_df
        self.__country_neighbour = self.get_farther_neighbour()
        self.__many_neighbours = self.get_many_neighbours()

    # The get_six_days_evolution method creates a data frame of the country containing the
    # date, new cases, new deaths and new recovered for the past 6 days.
    def get_six_days_evolution(self):
        return self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country, ["Date", "NewCases", "NewDeaths", "NewRecovered"]]

    # The get_farther_neighbour method is a helper method that retrieves the country with
    # farthest border. The return type is String.
    def get_farther_neighbour(self):
        # getting the country with the longest border
        neighbours_countries = self.get_neighbour_countries()
        # returning the name of the country with the longest border
        return (neighbours_countries.loc[
            neighbours_countries['Distance'] == neighbours_countries['Distance'].max(), ["Neighbour"]]).iloc[0][
            'Neighbour']

    # The get_neighbour_countries method is a helper method that retrieves all the countries and distances
    # that the main country has border with.
    def get_neighbour_countries(self):
        return self.__border_df.loc[
            self.__border_df["Country,Other"] == self.__country, ["Neighbour", "Distance"]]

    # The get_many_neighbours method returns the first 3 neighbour countries with the longest distance.
    def get_many_neighbours(self):
        neighbours_countries = self.get_neighbour_countries().sort_values(by='Distance', ascending=False)

        return neighbours_countries.loc[
            neighbours_countries['Distance'] == neighbours_countries['Distance'], ["Neighbour"]].head(3).values

    # This get_neighbour method returns the private variable.
    def get_neighbour(self):
        return self.__country_neighbour

    # The get_six_days_newCases method creates a new data frame merging
    # two dataframes, one for the main country and another for the neighbour with farthest border.
    def get_six_days_newCases(self):
        main_country_df = self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country, ["Date", "NewCases"]]
        df1 = main_country_df.rename({"NewCases": f'Newcases-{self.__country}'}, axis='columns')

        neighbour_country_df = self.__corona_df.loc[
            self.__corona_df["Country,Other"] == self.__country_neighbour, ["Date", "NewCases"]]
        df2 = neighbour_country_df.rename({'NewCases': f'Newcases-{self.__country_neighbour}'}, axis='columns')

        return pd.merge(df1, df2)

    # The get_six_days_Deaths method uses help of get_many_countries method and creates a new data frame merging
    # the Deaths/1M pop for the main country and the other 3.
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
