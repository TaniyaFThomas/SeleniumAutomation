from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\taniya.thomas\\Downloads\\chromedriver_win32_94\\chromedriver")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)
driver.find_element_by_name("q").send_keys("test")
driver.close()