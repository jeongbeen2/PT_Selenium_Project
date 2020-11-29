from selenium import webdriver

# driver = webdriver.Chrome("Real_Selenium/chromedriver")

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path="Real_Selenium/chromedriver", options=options)
driver.get("http://zzzscore.com/1to50/")
driver.implicitly_wait(300)

# 전역변수

""" element와 elements 차이? -> findAll처럼, 모든 element를 가져와서 리스트화 시킨다. """

num = 1


def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        print(btn.text, end="\t")
        if btn.text == str(num):
            btn.click()
            num += 1
            return


while num <= 50:
    clickBtn()