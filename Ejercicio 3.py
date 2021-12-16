from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/robhmer.linares/WorkSpace/test-lab/chromedriver.exe")

try:
    # Ingreso en la URL
    driver.get("https://www3.animeflv.net/")
    time.sleep(1)

    # Encuentro y acepto las cookies de la Web
    link = driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.sc-ifAKCX.ljEJIv")
    link.click()
    time.sleep(1)

    # Se busca el elemento one piece y se ingresa en el
    link = driver.find_element(By.CSS_SELECTOR, "a[href*='one-piece']")
    link.click()
    time.sleep(1)

    # Verifico que el último capítulo es el 1003
    episodio = driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a > p")
    driver.execute_script("window.scrollTo(0,800)")
    ultimo_episodio = int(episodio.text.split()[1])
    assert ultimo_episodio == 1003
    time.sleep(2)

finally:
    driver.quit()