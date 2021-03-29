import matplotlib.pyplot as plt


class PlotData:
    def __init__(self, country, neighbour, df):
        self.__country = country
        self.__neighbour = neighbour
        self.__df = df

    # Plots the evolution for the country in question for the past 6 days
    def evolution_six_days(self):
        self.__df.plot(kind='bar', x='Date', color=['green', 'red', 'blue'], width=0.8, rot=0)
        plt.title(f'6-days key indicators evolution {self.__country}')
        plt.show()

    # Plots the evolution for the country in question along with its neighbour for the past 6 days
    def two_countries_evouluton_six_days(self):
        self.__df.plot(kind='bar', x='Date', color=['blue', 'red'], width=0.8, rot=0)
        plt.title(f'6-days New Cases comparison - {self.__country} with neighbour {self.__neighbour}')
        plt.show()

    # Plots the difference between the Deaths/1M pop for the first 3 days for country in question and 2 of its neighbour
    def neigbours_deaths_perPop(self):
        self.__df.plot(kind='bar', x='Date', color=['blue', 'red', 'green', 'cyan'], width=0.8, rot=0)
        plt.title(f'6-days Deaths/1M pop comparison - {self.__country} with 3 neighbour')
        plt.show()