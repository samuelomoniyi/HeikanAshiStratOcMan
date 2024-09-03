import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to download the image using pyautogui
def download_image():
    time.sleep(5)  # Wait for the window to be ready
    pyautogui.moveTo(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)
    pyautogui.rightClick()
    pyautogui.moveRel(0, 10)
    pyautogui.click()
    time.sleep(2)
    pyautogui.typewrite("download.png")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("left")
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(2)
    print("Image downloaded.")

# Function to analyze the image and determine the last candle's color
def analyze_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at {image_path}")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    red_lower = np.array([245, 88, 71])
    red_upper = np.array([255, 108, 91])
    green_lower = np.array([4, 165, 79])
    green_upper = np.array([24, 185, 99])

    mask_red = cv2.inRange(image_rgb, red_lower, red_upper)
    mask_green = cv2.inRange(image_rgb, green_lower, green_upper)

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    last_candle_color = "green" if contours_green and (not contours_red or cv2.boundingRect(contours_green[-1])[0] > cv2.boundingRect(contours_red[-1])[0]) else "red"
    
    plt.figure(figsize=(10, 8))
    plt.imshow(image_rgb)
    plt.title("Specific Green and Red Candles Detected")
    plt.show()

    print(f"Detected {len(contours_green)} green candles and {len(contours_red)} red candles.")
    print(f"Last Candle Color: {last_candle_color}")

    return last_candle_color

# Function to perform the click action based on the candle color
def click_button_based_on_color(driver, color):
    if color == "green":
        call_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/div[1]/div/div[6]/div[1]/button')
        call_button.click()
    else:
        put_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/div[1]/div/div[6]/div[4]/button')
        put_button.click()
    time.sleep(3)

# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("start-maximized")

# Initialize Chrome WebDriver
driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the specified URL
driver.get('https://www.quotex.com/en/demo-trade/')

# Find the element using XPath and click it (login or initial navigation)
element = driver.find_element(By.XPATH, '//*[@id="top"]/div/nav/ul/li[1]/a')
element.click()
time.sleep(20)

# Main loop to run every 50 seconds
while True:
    download_image()  # Download the image
    last_candle_color = analyze_image('C:/Users/DELIGHT PHOTOS/Downloads/download.png')  # Analyze the image
    click_button_based_on_color(driver, last_candle_color)  # Click based on color

    time.sleep(50)  # Wait for 50 seconds before the next iteration

# Quit the driver after the loop ends (if you ever break out of the loop)
driver.quit()
