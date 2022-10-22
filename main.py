import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from urllib.parse import unquote
import random
import json

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}


def get_source_html(url):

    driver = webdriver.Chrome(
        executable_path="driver_path"
    )
    
    driver.maximize_window()
    
    try:
        driver.get(url=url)
        time.sleep(3)
        
        while True:
            find_more_element = driver.find_element_by_class_name("catalog-button-showMore")
            
            if driver.find_elements_by_class_name("hasmore-text"):
                with open("lesson12/source-page.html", "w") as file:
                    file.write(driver.page_source)
                    
                break
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_more_element).perform()
                time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()