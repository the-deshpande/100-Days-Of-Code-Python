from bs4 import BeautifulSoup
import requests


class ScrapeWebsite(BeautifulSoup):
    def __init__(self, url):
        response = requests.get(url)
        super().__init__(response.text, 'html.parser')
        self.property_details = []
        self.get_list()

    def get_list(self):
        property_zillow = self.select('.List-c11n-8-84-3-photo-cards>li')

        self.property_details = [{
            'address': prop.select_one('address').text.strip(),
            'link': prop.select_one('a').get('href'),
            'price': prop.select_one('.PropertyCardWrapper').text.strip().split('+')[0].split('/')[0]
        } for prop in property_zillow]
