import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


opener = AppURLopener()
response = opener.open("https://www.worldometers.info/coronavirus/")
