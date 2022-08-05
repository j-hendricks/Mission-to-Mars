# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    #initiate browser
    # execute all 3 functions
    # add outputs to dictionary
    #end broswer

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    news_title, news_paragraph = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    browser.quit()

    return data



def mars_news(browser):

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html = browser.html
    news_soup = soup(html, 'html.parser')
    slide_elem = news_soup.select_one('div.list_text')

    try: 
        slide_elem.find('div', class_='content_title')

        news_title = slide_elem.find('div', class_='content_title').get_text()
        
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None
    
    return news_title, news_p

def featured_image(browser):

    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
    
    except AttributeError:
        return None

    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

def mars_facts():

    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None
    
    df.columns=['Description', 'Mars','Earth']
    df.set_index('Description', inplace=True)
    
    return df.to_html(classes="table table-striped")

def mars_hemispheres(browser):

    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # img_div = img_soup.find('div', class_= "collapsible results")
    # imgs = img_soup.find_all('a', class_="itemLink product-item")
    # link_div = img_soup.find_all('div', class_="description")
    imgs = img_soup.find_all('h3')
    imgs = imgs[:-1]

    for img in imgs:
        hemispheres = {}
        browser.links.find_by_partial_text(img.text).click()
        html = browser.html
        img_soup = soup(html, 'html.parser')
        img_link = url + img_soup.find('img',class_="wide-image").get("src")
        img_title = img_soup.find('h2',class_="title").text
        hemispheres['img_url'] = img_link
        hemispheres['title'] = img_title
        hemisphere_image_urls.append(hemispheres)
        browser.back()

    browser.quit()

    print(hemisphere_image_urls)

    return hemisphere_image_urls


if __name__ == '__main__':

    print(scrape_all())



