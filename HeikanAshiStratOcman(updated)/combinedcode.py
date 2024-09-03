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
driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the specified URL
driver.get('https://www.quotex.com/en/demo-trade/')

# Find the element using XPath and click it
element = driver.find_element(By.XPATH, '//*[@id="top"]/div/nav/ul/li[1]/a')
element.click()

# Sleep for 20 seconds
time.sleep(20)

# it shows no module named distuils pip install --upgrade setuptools


while True:

    import pyautogui
    import time

    # Allow some time to switch to the desired window
    time.sleep(5)

    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate the center of the screen
    center_x, center_y = screen_width / 2, screen_height / 2

    # Move the mouse to the center of the screen
    pyautogui.moveTo(center_x, center_y)

    # Perform a right-click at the center
    pyautogui.rightClick()

    # Move the mouse slightly downward
    pyautogui.moveRel(0, 10)  # Moves the mouse 10 pixels down

    # Perform a left-click at the new position
    pyautogui.click()

    # Add a delay to ensure the application is ready for input
    time.sleep(2)

    # Type "download.png" and press Enter
    pyautogui.typewrite("download.png")
    pyautogui.press("enter")

    # Add a delay to ensure the application has processed the previous input
    time.sleep(2)

    # Press the left arrow key
    pyautogui.press("left")

    # Add a delay to ensure the application has processed the previous input
    time.sleep(2)

    # Press Enter again
    pyautogui.press("enter")

    print("Actions completed.")

    time.sleep(5)



    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the image using OpenCV
    image_path = 'C:/Users/DELIGHT PHOTOS/Downloads/download.png'
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        raise ValueError(f"Image not found at {image_path}")

    # Convert the image to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the RGB ranges for green and red candles
    # Adjusted slightly to cover a broader range
    red_lower = np.array([240, 80, 70])
    red_upper = np.array([255, 115, 100])

    green_lower = np.array([10, 160, 70])
    green_upper = np.array([30, 190, 100])

    # Create masks for red and green candles
    mask_red = cv2.inRange(image_rgb, red_lower, red_upper)
    mask_green = cv2.inRange(image_rgb, green_lower, green_upper)

    # Find contours for the red and green candles
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours to avoid noise
    contours_red = [c for c in contours_red if cv2.contourArea(c) > 50]
    contours_green = [c for c in contours_green if cv2.contourArea(c) > 50]

    # Draw rectangles for the red candles
    for contour in contours_red:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Blue rectangle for clarity

    # Draw rectangles for the green candles
    for contour in contours_green:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green rectangle

    # Display the image with highlighted green and red candles
    plt.figure(figsize=(10, 8))
    plt.imshow(image_rgb)
    plt.title("Specific Green and Red Candles Detected")
    plt.show()

    # Count the number of detected green and red candles
    num_red_candles = len(contours_red)
    num_green_candles = len(contours_green)

    # Determine the last candle's color based on X position
    if contours_green and contours_red:
        last_green = max(cv2.boundingRect(c)[0] for c in contours_green)
        last_red = max(cv2.boundingRect(c)[0] for c in contours_red)
        last_candle_color = "green" if last_green > last_red else "red"
    elif contours_green:
        last_candle_color = "green"
    elif contours_red:
        last_candle_color = "red"
    else:
        last_candle_color = "unknown"

    # Print the results
    print(f"Detected {num_green_candles} green candles and {num_red_candles} red candles.")
    print(f"Last Candle Color: {last_candle_color}")

    # this sees very accurate 


    if last_candle_color=="green":
        call_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/div[1]/div/div[6]/div[1]/button')
        call_button.click()
        time.sleep(3)
    else:
        put_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/div[1]/div/div[6]/div[4]/button')
        put_button.click()
        time.sleep(3)
    
    time.sleep(50)



time.sleep(10)

driver.quit()

