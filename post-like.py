#We import selenium and time modules
import selenium
from selenium import webdriver
import time

#we make an instance of chromedriver and path the path of chromedriver
driver = webdriver.Chrome("chromedriver.exe")

#open the required website to be opened by the driver
url = "https://instagram.com"
driver.get(url)
#we wait to write down our username and password(If required)
time.sleep(20)

username="codeforcause"
driver.get("https://instagram.com/{}".format(username))

#gives the user's name
pagename = driver.find_elements_by_class_name("_7UhW9")
print(pagename)

#select the first post and click it
post = driver.find_elements_by_class_name("_9AhH0")
post[0].click()

#select the post dialog box which has the like button
dialog = driver.find_elements_by_css_selector('[role="presentation"]')

#iterate over 5 posts
count = 5
while(count>0):

  if len(dialog)<=2:
        major = dialog[1]
        #selects the like button and clicks it
        likes = driver.find_elements_by_css_selector('[aria-label="Like"]')
        if len(likes)>0:
            likes[0].click()
        count-=1

        #selects the next button and  clicks it
        next = driver.find_elements_by_class_name("coreSpriteRightPaginationArrow")
        if len(next)>0:
            next[0].click()
            time.sleep(1)