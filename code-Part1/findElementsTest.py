from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
get_title = driver.title
print(get_title)
sleep(10)

try:
    driver.switch_to.frame("webklipper-publisher-widget-container-notification-frame")
    sleep(10)
    print("Switched")
    driver.find_element(By.XPATH, f"//a[@id='webklipper-publisher-widget-container-notification-close-div']").click()
    sleep(3)
    print("closed")
except Exception as e:
    print("Failed on closing pop up", e)








