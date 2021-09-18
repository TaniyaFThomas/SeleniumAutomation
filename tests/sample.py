import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ITTroubleshooterSearchTest(unittest.TestCase):
    def setUp(self):
        print("Inside setup")
        caps = {'browserName': os.getenv('firefox', 'firefox')}
        print("Caps:", caps)
        self.browser = webdriver.Remote(
            command_executor='http://127.0.0.1:4446/wd/hub',
            desired_capabilities=caps
        )

    def test_ITTroubleshooter_search_for(self):
        browser = self.browser
        print("Browser:", browser)
        browser.get('https://www.google.com/')
        print("After get")
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('ittroubleshooter.in')
        search_box.send_keys(Keys.RETURN)
        browser.get('https://ittroubleshooter.in/')
        time.sleep(3)  # simulate long running test

    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()