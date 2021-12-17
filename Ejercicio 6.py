import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAlert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/robhmer.linares/WorkSpace/test-lab/chromedriver.exe")
        self.driver.maximize_window()

    def test_js_alert(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alert_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
        alert_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        result = self.driver.find_element(By.ID, "result")
        result_text = result.text
        assert result_text == "You successfully clicked an alert"
        
    def test_js_confirm_accept(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alert_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        alert_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        result = self.driver.find_element(By.ID, "result")
        confirm_text = result.text
        assert confirm_text == "You clicked: Ok"

    def test_js_confirm_cancel(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alert_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        alert_button.click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        result = self.driver.find_element(By.ID, "result")
        cancel_text = result.text
        assert cancel_text == "You clicked: Cancel"

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()