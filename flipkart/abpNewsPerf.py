from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManage().install())
wait = WebDriverWait(driver, 20)
driver.get('https://www.abplive.com/')
sleep(3)
driver.maximize_window()
sleep(4)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='stickhead']/div/div/div/div/div[1]/span[1]/a/font/font"))).click()
sleep(2)

