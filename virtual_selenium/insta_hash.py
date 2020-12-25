import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

main_hashtag = "dog"

driver.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")
header = driver.find_element_by_tag_name("header")
hashtags = header.find_element_by_class_name("AC7dP")

print(hashtags.text)

time.sleep(3)
driver.quit()