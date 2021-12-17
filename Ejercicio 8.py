import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestTabla(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/robhmer.linares/WorkSpace/test-lab/chromedriver.exe")
        self.driver.maximize_window()

    def test_tablas_due(self):
        self.driver.get("https://the-internet.herokuapp.com/tables")
        filas = self.driver.find_elements(By.CSS_SELECTOR, "#table1 > tbody > tr")

        max_due = 0
        max_name = ""

        #Recorro la lista y determino quien tiene la due mayor
        for fila in filas:
            info_lista = fila.text.split()
            name = info_lista[0]
            due = float(info_lista[3][1:])

            if due > max_due:
                max_due = due
                max_name = name

        print(max_name + "\n" + str(max_due))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()