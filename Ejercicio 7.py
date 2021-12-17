import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Testmultiplewindows(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/robhmer.linares/WorkSpace/test-lab/chromedriver.exe")
        self.driver.maximize_window()

    def test_multiple_window(self):
        self.driver.get("https://the-internet.herokuapp.com/windows")
        link = self.driver.find_element(By.CSS_SELECTOR, "#content > div > a")
        link.click()

        window_list = self.driver.window_handles
        self.driver.switch_to.window(window_list[1])
        time.sleep(1)

        text_object = self.driver.find_element(By.CSS_SELECTOR, "body > div > h3")
        assert text_object.text == "New Window"
        self.driver.close()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()