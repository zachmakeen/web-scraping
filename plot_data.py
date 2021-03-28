import matplotlib.pyplot as plt


class PlotData:
    def __init__(self, country, df):
        self.__country = country
        self.__df = df

    def evolution_six_days(self):
        self.__df.plot(kind='bar', x='Date', color=['green', 'red', 'blue'], width=0.8, rot=0)
        plt.title(f'6-days key indicators evolution {self.__country}')
        plt.show()


