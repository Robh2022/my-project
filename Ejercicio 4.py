from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/robhmer.linares/WorkSpace/test-lab/chromedriver.exe")
driver.maximize_window()

try:
    # Ingreso en la URL
    driver.get("https://www.eltiempo.es/madrid.html")
    time.sleep(1)

    # Encuentro y acepto las cookies de la Web
    link = driver.find_element(By.CSS_SELECTOR,"#didomi-notice-agree-button")
    link.click()
    time.sleep(1)

    #Validación de la temperatura actual
    texto_temperatura = driver.find_element(By.CSS_SELECTOR, ".c-tib-text")
    #Con el :-1 elimino el º que está al final del texto para evitar errores
    temperatura = int(texto_temperatura.text[:-1])
    assert 0 < temperatura < 60, "rango incorrecto"
    time.sleep(1)

    #En caso de algún fallo sacar captura de pantalla y mostrar el error
except  Exception:
    driver.save_screenshot("temp/screenshot.png")
    raise

finally:
    driver.quit()