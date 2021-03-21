from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from settings import getConfig
from send_email import send_email


def runSearch():
    conf = getConfig()

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--incognito')
    chromeOptions.add_argument('--headless')

    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(conf["offersUrl"])

    time.sleep(2)

    accept_button = browser.find_element_by_id(
        "onetrust-accept-btn-handler").click()
    time.sleep(1)

    change_warinings = browser.find_elements_by_class_name(
        "criteriaChangeWarning")

    offers = browser.find_elements_by_class_name(
        "offer-title__link")

    if len(change_warinings) == 0 and len(offers) > 0:

        offers[0].click()

        time.sleep(1)
        current_url = browser.current_url

        print("ZNALEZIONO")
        print(current_url)
        send_email(
            offer_url=current_url,
            title="OTOMOTO-SEARCH",
            receiver_email=conf["receiverEmail"],
            sender_email=conf["senderEmail"],
            sender_password=conf["senderPassword"])

    browser.quit()


if __name__ == '__main__':
    runSearch()
