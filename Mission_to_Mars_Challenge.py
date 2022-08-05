# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
img_url_rel


# In[13]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Facts

# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars','Earth']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html()


# In[16]:


browser.quit()


# In[17]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[18]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[19]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[20]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[21]:


slide_elem.find('div', class_='content_title')


# In[22]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[23]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[24]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[25]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[26]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url



df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[30]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


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

# for img in imgs:
#     if img.find('h3') != None:
#         browser.links.find_by_partial_text(img.find('h3').text).click()
        
       
    
# for i in hemisphere_image_urls:
#     print(i)
    
#     print(img.get('href'))

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()


