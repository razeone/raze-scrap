import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH= f"{os.environ['CHROMEDRIVER_PATH']}chromedriver"

print(DRIVER_PATH)
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://aristeguinoticias.com/")
print(driver.title)
driver.quit()
