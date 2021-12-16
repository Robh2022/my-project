from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/robhmer.linares/WorkSpace/test-lab/chromedriver.exe")
driver.maximize_window()

try:
    # Ingreso en la URL
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1)

    #Encuentro add element y pulso 20 veces
    add_boton = driver.find_element(By.CSS_SELECTOR, "#content > div > button")
    for i in range(20):
        add_boton.click()

    #Eliminar los 20 botones que aparecen
    for i in range(20):
        delete_boton = driver.find_element(By.CSS_SELECTOR, "#elements > button").click()

finally:
    driver.quit()