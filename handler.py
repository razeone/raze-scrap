from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH='/opt/chrome/chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://aristeguinoticias.com/")
print(driver.title)
driver.quit()