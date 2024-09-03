# pip install webdriver_manager


# # selenium 4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# option = webdriver.ChromeOptions()
# option.add_argument("start-maximized")


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
# driver.get('https://www.quotex.com/en/demo-trade/')

# oya 

# import undetected_chromedriver as uc
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Set up Chrome options
# options = uc.ChromeOptions()
# options.add_argument("start-maximized")

# # Initialize Chrome WebDriver with undetected_chromedriver and webdriver_manager
# driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Open the specified URL
# driver.get('https://www.quotex.com/en/demo-trade/')

# # Find the element using XPath and click it
# element = driver.find_element(By.XPATH, '//*[@id="top"]/div/nav/ul/li[1]/a')
# element.click()

# # Sleep for 20 seconds
# time.sleep(20)

# # Close the browser
# driver.quit()

# second



import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("start-maximized")

# Initialize Chrome WebDriver with undetected_chromedriver and webdriver_manager
# Use the correct ChromeDriver version compatible with your browser
driver = uc.Chrome(service=Service(ChromeDriverManager(version="127.0.6533.73").install()), options=options)

# Open the specified URL
driver.get('https://www.quotex.com/en/demo-trade/')

# Find the element using XPath and click it
element = driver.find_element(By.XPATH, '//*[@id="top"]/div/nav/ul/li[1]/a')
element.click()

# Sleep for 20 seconds
time.sleep(20)

# Close the browser
driver.quit()
