from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from send_email import send_email

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
# options.add_argument('--headless')
# options.add_argument('--ignore-certificate-errors')

URL=os.getenv("OFFERS_URL")
# URL=os.getenv("TEST_OFFERS_URL")

browser = webdriver.Chrome(chrome_options=options)
browser.get(URL)

time.sleep(2)

accept_button = browser.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(1)

change_warinings = browser.find_elements_by_class_name("criteriaChangeWarning")

if len(change_warinings) == 0:
    print("ZNALEZIONO")
    browser.find_element_by_class_name("offer-title__link").click()

    time.sleep(1)
    current_url = browser.current_url
    print(current_url)
    send_email(offer_url=current_url, title="FABIA", receiver_mail=os.getenv("MAIL_RECEIVER"))

# print(len(change_warinings))
# source = browser.page_source

browser.quit()