from bs4 import BeautifulSoup as bs
import datetime
import urllib
from urllib.request import Request, urlopen


class SaveFile:
    def __init__(self, url='https://www.worldometers.info/coronavirus/'):
        self.__url = url

    # Reads HTML code directly from the set url and creates a BeautifulSoup object
    def save_html(self):
        try:
            request = Request(self.__url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(request).read().decode("utf-8")  # Gets HTML code
            soup = bs(html, "html.parser")  # Creates BeautifulSoup object
            with open("local_html/" + f"local_file{str(datetime.date.today())}.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())  # Creates new file with the current date and writes HTML to that file
        except urllib.error.HTTPError as error:
            print(error)
