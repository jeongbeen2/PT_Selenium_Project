from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.command import Command
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://learning.hanyang.ac.kr/courses/11565/external_tools/1")


id_bar = driver.find_element_by_id("uid")

id_bar.send_keys("id")
time.sleep(2)

pw_bar = driver.find_element_by_id("upw")

pw_bar.send_keys("password")
time.sleep(2)

pw_bar.send_keys(Keys.ENTER)
time.sleep(3)
login_btn = driver.find_element_by_id("login_btn")
login_btn.click()
# pw_bar.send_keys(Keys.ENTER)


title = driver.find_elements_by_class_name("xnslh-section-title")

second_title = title[1]

second_title.click()

# driver.quit()
