import cv2
import numpy as np

image_name = 'image_cube_cardboard_41.png'

# Read the image
image = cv2.imread(image_name)  # Replace with your image path

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform Canny edge detection
edges = cv2.Canny(gray, 50, 120, apertureSize=3)

# Save the edges image
cv2.imwrite(f'edges_{image_name}', edges)

# Use Hough Line Transform to find lines
# Parameters here are in the following order:
# 1. The input image.
# 2. The resolution of the accumulator in pixels (rho).
# 3. The resolution of the accumulator in radians (theta).
# 4. The threshold, which means minimum vote it should get to be considered as a line.
lines = cv2.HoughLines(edges, 1, np.pi / 180, 130)

# Draw the lines on the original image
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Save the image with lines
cv2.imwrite(f'lines_{image_name}', image)
