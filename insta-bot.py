from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
import sys
from random import randint

from credentials import *
from config import *

__author__ = 'Annie Wu'
__version__ = '1.1.0'
__maintainer__ = 'JuHunC'
__email__ = 'joohun484@gmail.com'
__status__ = 'Dev'

logging.basicConfig(
    format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

# Do this so we don't get DevTools and Default Adapter failure
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initialize chrome driver and set chrome as our browser
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# If selenium can't find an element, it waits 5 sec to let things load and tries again
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(1)

# Get the login elements and type in your credentials
username = browser.find_element_by_name('username')
username.send_keys(USERNAME)
password = browser.find_element_by_name('password')
password.send_keys(PASSWORD)

sleep(1)

# Click the login button
browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()

# If login information is incorrect, program will stop running
try:
    if browser.find_element_by_xpath("//*[@id='slfErrorAlert']"):
        browser.close()
        sys.exit('Error: Login information is incorrect')
    else:
        pass
except:
    pass

sleep(1)

logger.info(f'Logged in to {USERNAME}')

# Save your login info? Not now
try:
    browser.find_element_by_xpath(
        "//*[@id='react-root']/div/div/section/main/div/div/div/div/button").click()
except Exception:
    pass

sleep(1)

# Turn on notifications? Not now
try:
    browser.find_element_by_xpath(
        "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
except Exception:
    pass

sleep(1)

# Keep track of how many you like and comment
likes = 0
comments = 0

# Index for tags in hashtag list
tag_index = 0

for hashtag in hashtag_list:
    browser.get(
        f'https://www.instagram.com/explore/tags/{hashtag_list[tag_index]}/')
    logger.info(f'Exploring #{hashtag}')
    sleep(1)

    # Click first thumbnail to open
    first_thumbnail = browser.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]")
    first_thumbnail.click()

    # Go through x number of photos per hashtag
    for post in range(1, number_of_posts):

        if enable_like:
            # Check if the post is already liked
            # If not, then like, comment, and go to next post
            try:
                browser.find_element_by_xpath("//*[@aria-label='좋아요 취소']")
                logger.info("Already liked this post")
            except Exception:
                # Like
                browser.find_element_by_xpath("//*[@aria-label='좋아요']").click()
                logger.info("Liked")
                likes += 1

        if enable_comment:
            # Random chance of commenting
            do_i_comment = randint(1, chance_to_comment)
            if do_i_comment == 1:
                try:
                    # Comment
                    browser.find_element_by_xpath("//form").click()
                    comment = browser.find_element_by_xpath("//textarea")

                    sleep(wait_to_comment)

                    rand_comment_index = randint(0, len(comments_list))
                    comment.send_keys(comments_list[rand_comment_index])
                    comment.send_keys(Keys.ENTER)
                    logger.info(
                        f"Commented '{comments_list[rand_comment_index]}'")
                    comments += 1

                except Exception:
                    # Continue to next post if comments section is limited or turned off
                    continue

        # Go to next post
        sleep(wait_between_posts)
        browser.find_element_by_link_text('다음').click()
        logger.info('Getting next post')
        sleep(wait_between_posts)

    # Go to the next index in hashtags_list
    tag_index += 1

if enable_like:
    logger.info(f'Liked {likes} posts')
if enable_comment:
    logger.info(f'Commented on {comments} posts')