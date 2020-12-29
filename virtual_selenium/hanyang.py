import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://learning.hanyang.ac.kr/courses/11565/external_tools/3")

# Login #
id_bar = driver.find_element_by_id("uid")
pw_bar = driver.find_element_by_id("upw")
id_bar.send_keys("id")
pw_bar.send_keys("pw")
pw_bar.send_keys(Keys.ENTER)
Alert(driver).accept()

# Video Scrap #
movies = driver.find_elements_by_class_name("movie")
print(movies)

weeks = driver.find_elements_by_class_name("xns-subsection-container")
for index, week in enumerate(weeks):
    print(index)

driver.quit()

