#find an automatic way to import dynamically
#import importlib

scrapers_array = [
    {'module': 'kat_scraper', 'class': 'KatScraper'},
    {'module': 'bs_scraper', 'class': 'BSScraper'},
]


#module = importlib.import_module('kat_scraper')
#module = __import__('kat_scraper')

from operator import itemgetter

from kat_scraper import KatScraper
from bs_scraper import BSScraper 
from scraper import Scraper

class ScrapAll():
 
    def get_torrents(self, search):
        scraper = BSScraper()
        torrents = []
        for scraper in scrapers_array:
            scraper_object = eval(scraper['class'])()
            torrents.append(scraper_object.get_torrents(search))
        return Scraper.sort(sum(torrents, []), 'seed')
