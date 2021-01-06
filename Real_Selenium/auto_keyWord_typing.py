from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("Real_Selenium/chromedriver")


# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(executable_path="chromedriver", options=options)
driver.get("https://www.youtube.com/")


sleep(3)

""" 
xpath -> //*[@id="search"] 대신, //input[@id="search"] 을 넣자.
혹은, search = driver.find_element_by_name("search_query")도 가능.
"""

search = driver.find_element_by_xpath('//input[@id="search"]')
search.send_keys("생활 코딩")
sleep(1)

search.send_keys(Keys.ENTER)