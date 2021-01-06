from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

KEYWORD = "buy domain"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")
search_bar = driver.find_element_by_class_name("gLFyf")

search_bar.send_keys(KEYWORD)

search_bar.send_keys(Keys.ENTER)

shitty_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))

search_results = driver.find_elements_by_class_name("g")

for index, search_result in enumerate(search_results):
    
    class_name = search_result.get_attribute("class")
    
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")


driver.quit()