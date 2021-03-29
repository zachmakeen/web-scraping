import matplotlib.pyplot as plt


class PlotData:
    def __init__(self, country, neighbour, df):
        self.__country = country
        self.__neighbour = neighbour
        self.__df = df

    def evolution_six_days(self):
        self.__df.plot(kind='bar', x='Date', color=['green', 'red', 'blue'], width=0.8, rot=0)
        plt.title(f'6-days key indicators evolution {self.__country}')
        plt.show()

    def two_countries_evouluton_six_days(self):
        self.__df.plot(kind='bar', x='Date', color=['blue', 'red'], width=0.8, rot=0)
        plt.title(f'6-days New Cases comparison - {self.__country} with neighbour {self.__neighbour}')
        plt.show()

    def neigbours_deaths_perPop(self):
        self.__df.plot(kind='bar', x='Date', color=['blue', 'red', 'green', 'cyan'], width=0.8, rot=0)
        plt.title(f'6-days Deaths/1M pop comparison - {self.__country} with 3 neighbour')
        plt.show()