from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Chrome(r"C:\D Drive\Program\chromedriver.exe")

s = Service(r"C:\D Drive\Program\chromedriver.exe")
# driver = webdriver.Chrome()
driver.get('https://news.abplive.com/')

driver.maximize_window()
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
print(" site title : " + driver.title)
wait = WebDriverWait(driver, 5)
#wait.until(visibility_of_element_located(xpath, "//a[text()='HOME']")).click()
sleep(5)
wait.until(visibility_of_element_located(xpath, "(//div[@class='uk-grid-collapse uk-grid'])[1]")).click()