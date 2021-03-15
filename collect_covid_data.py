import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime


class CollectData:
    def __init__(self):
        self.__url = "https://www.worldometers.info/coronavirus/"
        self.__download_html()
        # self.__soup = self.__parse_html()
        # self.__store_data()

    def __download_html(self):
        try:
            request = Request(self.__url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(request)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            with open("local_html/" + f"local_file{datetime.date.today()}.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())
        except urllib.error.HTTPError as error:
            print(error)

    def __parse_html(self):
        with open("html-pages/2021-03-15.html", encoding="utf-8") as html:
            return BeautifulSoup(html.read(), "html.parser")

    def __store_data(self):
        table = self.__soup.find(id="main_table_countries_today")

# Path: <div class="tab_content" id="nav-tabContent">
#           <div class="tab-pane active" id="nav-today" role="tabpanel" arialabelledby="nav-today-tab">
#               <div class="main_table_countries_div">
#                   <table id="main_table_countries_today_wrapper" class="table table_bordered table_hover main)table_countries database no_footer" style="width: 100%; margin-top: 0px !important;">
#                       <tbody>
#           <div class="tab-pane active" id="nav-yesterday" role="tabpanel" arialabelledby="nav-yesterday-tab">
#           <div class="tab-pane active" id="nav-yesterday2" role="tabpanel" arialabelledby="nav-yesterday2-tab">
