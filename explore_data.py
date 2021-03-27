class ExploreData:
    def __init__(self, country, corona_df, border_df):
        self.__country = country
        self.__corona_df = corona_df
        self.__border_df = border_df

        # print(self.__corona_df)

        # print(self.__corona_df.info())
        # print(self.__border_df.info())

        # print(self.__corona_df.axes)
        # print(self.__border_df.axes)

        # print(self.__corona_df.loc[1])

        # temp = self.__corona_df.loc[self.__corona_df["Country,Other"] == self.__country, ["NewCases", "NewDeaths", "NewRecovered"]]
        # print(temp)
