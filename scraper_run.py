from xml.dom.minidom import getDOMImplementation
import glassdoor_scraper as gds 
#import scraper as gds


#This line will open a new chrome window and start the scraping.
df = gds.get_jobs("software engineer", 5, False, 15)

df
