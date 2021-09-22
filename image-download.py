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


#iterate over 5 posts





count = 5
while(count>0):
    # select the post dialog box
    time.sleep(2)
    dialog = driver.find_elements_by_css_selector('[role="presentation"]')
    major = dialog[1]

    #selects the photo div
    photo = driver.find_elements_by_class_name("_9AhH0")
    if len(photo)>0:
        downloadable = photo[0]
        content = downloadable.screenshot_as_png
#writes the image in a file
        fname=""
        with open('./images/{}.png'.format(count), 'wb') as f:
                f.write[content]


    count-=1

    #selects the next button and  clicks it
    next = driver.find_elements_by_class_name("coreSpriteRightPaginationArrow")
    if len(next)>0:
        next[0].click()
        time.sleep(10)
    else:
        break;