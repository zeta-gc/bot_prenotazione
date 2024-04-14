from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()


import datetime

import schedule
import time

credentials = {
    "lunedi":[[], ["test", "test"]],
    "martedi":[[]],
    "mercoledi":[[]],
    "giovedi":[[]],
    "venerdi":[[]],


}

def prenota(email, psw):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://ginnipal.it/CusCosenza/')
        current_date = datetime.datetime.now()
        date_1_day_after= current_date + datetime.timedelta(days=1)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edEmail")))
        select_element = driver.find_element(By.ID, "edEmail")
        select_element.send_keys(email)
        select_element = driver.find_element(By.ID, "edPassword")
        select_element.send_keys(psw)
        select_element = driver.find_element(By.ID, "bLogin")
        select_element.click()

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bPrenotazione")))
        select_element = driver.find_element(By.ID, "bPrenotazione")
        select_element.click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bDettagli-1")))
        select_element = driver.find_element(By.ID, "bDettagli-1")
        select_element.click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edDataPrenotata")))
        select_element = driver.find_element(By.ID, "edDataPrenotata")
        select_element.send_keys(date_1_day_after.date().strftime("%d/%m/%Y"))

        select_element = driver.find_element(By.ID, "edOrarioPrenotato")
        select_element.click()
        select_element = driver.find_element(By.XPATH,  "//*[contains(text(),'14:00 - 16:00')]").click()
        select_element = driver.find_element(By.ID, "bProcedi").click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bConferma"))).click()
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def prenota_per_giorno(giorno):
    for credenziali in credentials[giorno]:
        if len(credenziali) == 2:
            prenota(credenziali[0], credenziali[1])


schedule.every().sunday.at("00:00").do(prenota_per_giorno, "lunedi")
schedule.every().monday.at("00:00").do(prenota_per_giorno, "martedi")
schedule.every().tuesday.at("00:00").do(prenota_per_giorno, "mercoledi")
schedule.every().wednesday.at("00:00").do(prenota_per_giorno, "giovedi")
schedule.every().thursday.at("00:00").do(prenota_per_giorno, "venerdi")


print("Bot started")
while True:
    schedule.run_pending()
    time.sleep(10)  