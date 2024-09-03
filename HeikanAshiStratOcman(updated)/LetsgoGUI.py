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
time.sleep(1.5)

# Press Enter again
pyautogui.press("enter")

print("Actions completed.")
