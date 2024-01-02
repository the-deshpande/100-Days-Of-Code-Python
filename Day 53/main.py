from zillow import ScrapeWebsite
from sheet import Sheet

google_form = 'https://forms.gle/W35Mrd635ZXyqZ1H7'
zillow = 'https://appbrewery.github.io/Zillow-Clone/'

scraper = ScrapeWebsite(zillow)
sheet = Sheet()
for entry in scraper.property_details:
    sheet.fill_the_form(google_form, entry)

