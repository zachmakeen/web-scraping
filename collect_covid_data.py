import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class CollectData:
    def __init__(self):
        # self.url = "https://www.worldometers.info/coronavirus/"
        self.url = open("website/Coronavirus Update (Live)_ 120,669,548 Cases and 2,669,118 Deaths from COVID-19 Virus Pandemic - Worldometer.html", encoding="utf8")
        self.__store_html()
        # self.soup = self.__parse_html()
        # self.store_data()

    def __parse_html(self):
        try:
            request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(request)
            html = page.read().decode("utf-8")
            return BeautifulSoup(self.url, "html.parser")
            #return BeautifulSoup(html, "html.parser")
        except urllib.error.HTTPError as error:
            print(error)



    def store_data(self):
        htmllist = self.soup.find_all("tr", style="")
        print(htmllist)

# Path: <div class="tab_content" id="nav-tabContent">
#           <div class="tab-pane active" id="nav-today" role="tabpanel" arialabelledby="nav-today-tab">
#               <div class="main_table_countries_div">
#                   <table id="main_table_countries_today_wrapper" class="table table_bordered table_hover main)table_countries database no_footer" style="width: 100%; margin-top: 0px !important;">
#                       <tbody>
#           <div class="tab-pane active" id="nav-yesterday" role="tabpanel" arialabelledby="nav-yesterday-tab">
#           <div class="tab-pane active" id="nav-yesterday2" role="tabpanel" arialabelledby="nav-yesterday2-tab">
