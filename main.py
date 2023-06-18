import json

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://magistr.edu.uz/"
driver.get(url)
driver.maximize_window()
time.sleep(1)

# Scroll down the page
for _ in range(4):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.07)
time.sleep(3)
# Click on the select dropdown
select = driver.find_element(By.XPATH,
                             '/html/body/div/div/div/div[2]/section[4]/div/div[1]/div[2]/div/div[1]/div/div[1]/span/span')
select.click()
time.sleep(1)
all_data = []
result = []
try:
    for i in range(1, 120):
        # Get the university name
        university_xpath = f'/html/body/div/div/div/div[2]/section[4]/div/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/ul/li[{i}]'
        university = driver.find_element(By.XPATH, university_xpath).text
        # print(university)

        # Click on the university
        click_to_university = driver.find_element(By.XPATH, university_xpath)
        click_to_university.click()
        time.sleep(1)

        # Click on the language dropdown
        language = driver.find_element(By.XPATH,
                                       '/html/body/div/div/div/div[2]/section[4]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/span')
        language.click()
        time.sleep(1)

        # Select the language (assuming the first option is "uzb")
        uzb = driver.find_element(By.XPATH,
                                  '/html/body/div/div/div/div[2]/section[4]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li')
        uzb.click()
        time.sleep(0.5)

        # Click on the filter button
        filter_button = driver.find_element(By.XPATH,
                                            '/html/body/div/div/div/div[2]/section[4]/div/div[1]/div[2]/button')
        filter_button.click()
        time.sleep(0.01)
        arr = []
        try:
            for k in range(1, 100):
                for h in range(1, 4):
                    time.sleep(0.01)
                    data = driver.find_element(By.XPATH,
                                               f'/html/body/div/div/div/div[2]/section[4]/div/div[2]/div/div[3]/table/tbody/tr[{k}]/td[{h}]').text
                    # print(data)
                    time.sleep(0.01)
                    all_data.append(data)
        except:
            # print(all_data)

            time.sleep(0.1)
            select = driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[2]/section[4]/div/div[1]/div[2]/div/div[1]/div/div[1]/span/span')
            select.click()
            time.sleep(2)
        for k in range(0, len(all_data), 3):
            item = {
                'university': university,
                'name': all_data[k],
                'grand': int(all_data[k + 1]),
                'kontrakt': int(all_data[k + 2])
            }
            result.append(item)
            print(item)
    # with open('data.json', 'w') as json_file:
    #     json.dump(result, json_file, indent=4)
    #
    # print("JSON data saved to 'data.json' file.")
except Exception as e:
    print(e)
    with open('jsons/magistratura_latest.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

    print("JSON data saved to 'data.json' file.")

# Close the webdriver
