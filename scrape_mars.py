from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
import time



def scrape():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    # Run the function below:
        mars_dict = {
        "Title": title,
        "Paragraph": paragraphs,
        "Featured Image": featured_image_url(browser),
        "Mars Weather": mars_weather(),
        "Facts": facts_html_table,
        "Hemisphere Images": hemisphereImages(browser) }

        browser.quit()
    return mars_dict

def mars_news():
    #read html file into jupyter
    filepath = os.path.join('nasa.html')
    with open(filepath) as file:
        html = file.read()


    # ## Step 1 - Scraping
    # 
    # ### NASA Mars News


    #make a beautiful soup object
    mars = bs(html, 'lxml')

    #collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later


    # Extract title text
    title = mars.title.text


    # Print all paragraph texts
    paragraphs = mars.find_all('p')
    for paragraph in paragraphs:
        print(paragraphs)

    return title, paragraphs


def mars_image(browser):
    # ### PL Mars Space Images - Featured Image


    #Visit the url for JPL Featured Space Image here.
    #Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    #Make sure to find the image url to the full size .jpg image.
    #Make sure to save a complete url string for this image.


    get_ipython().system(' which chromedriver')

    # executable_path = {'executable_path': '~/usr/local/bin/chromedriver'}
    executable_path = {'executable_path': '/'}
    browser = Browser('chrome', **executable_path, headless = False)


    images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images)

    html = browser.html
    # print(html)
    soup = bs(html, "html.parser")

    #look through the website to get the featured image

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')

    #reset link to the new page with the featured image
    html = browser.html
    soup = bs(html, "html.parser")

    image_path = soup.find('figure', class_='lede').a['href']

    featured_image_url = "https://www.jpl.nasa.gov" + image_path

    return featured_image_url

def mars_weather():
    # ### Mars Weather

    #get mars weather twitter
    twitter_response = requests.get("https://twitter.com/marswxreport?lang=en")
    twitter_soup = bs(twitter_response.text, 'html.parser')

    mars_weather_pull = twitter_soup.find_all('div', class_="js-tweet-text-container")


    mars_weather = mars_weather_pull[0].text

    # ### Mars Facts

    #Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    #Use Pandas to convert the data to a HTML table string.

    facts = "https://space-facts.com/mars/"


    table = pd.read_html(facts)

    table[0]


    mars_facts = table[0]
    mars_facts.columns = ["Parameter", "Values"]
    mars_facts.set_index(["Parameter"])


    facts_html = mars_facts.to_html()
    facts_html_table = facts_html.replace("\n", "")
    return facts_html_table


def hemispheres(broswer):
    # ### Mars Hemispheres


    #Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    #You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    #Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    #Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless = False)

    hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres)


    html_hemispheres = browser.html

    soup = bs(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphereImages = []

    hemispheres_main = 'https://astrogeology.usgs.gov'


    for i in items: 
        title = i.find('h3').text

        partialimg = i.find('a', class_='itemLink product-item')['href']
    
        browser.visit(hemispheres_main + partialimg)

        partialimg_html = browser.html
        
        soup = bs(partialimg, 'html.parser')
        
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
        hemisphereImages.append({"title" : title, "img_url" : img_url})
        return hemisphereImages

