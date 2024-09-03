# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the image using OpenCV
# image_path = 'download.png'
# image = cv2.imread(image_path)

# # Check if the image is loaded successfully
# if image is None:
#     raise ValueError(f"Image not found at {image_path}")

# # Convert the image to RGB format
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Define the RGB ranges for green and red candles
# # Assuming a small range to account for color variations due to anti-aliasing or compression
# red_lower = np.array([245, 88, 71])
# red_upper = np.array([255, 108, 91])

# green_lower = np.array([4, 165, 79])
# green_upper = np.array([24, 185, 99])

# # Create masks for red and green candles
# mask_red = cv2.inRange(image_rgb, red_lower, red_upper)
# mask_green = cv2.inRange(image_rgb, green_lower, green_upper)

# # Find contours for the red and green candles
# contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Draw rectangles for the red candles
# for contour in contours_red:
#     x, y, w, h = cv2.boundingRect(contour)
#     cv2.rectangle(image_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Blue rectangle for clarity

# # Draw rectangles for the green candles
# for contour in contours_green:
#     x, y, w, h = cv2.boundingRect(contour)
#     cv2.rectangle(image_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green rectangle

# # Display the image with highlighted green and red candles
# plt.figure(figsize=(10, 8))
# plt.imshow(image_rgb)
# plt.title("Specific Green and Red Candles Detected")
# plt.show()

# # Count the number of detected green and red candles
# num_red_candles = len(contours_red)
# num_green_candles = len(contours_green)

# # Determine the last candle's color
# last_candle_color = "green" if contours_green and (not contours_red or cv2.boundingRect(contours_green[-1])[0] > cv2.boundingRect(contours_red[-1])[0]) else "red"

# # Print the results
# print(f"Detected {num_green_candles} green candles and {num_red_candles} red candles.")
# print(f"Last Candle Color: {last_candle_color}")

# not going well



import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV
image_path = 'download.png'
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