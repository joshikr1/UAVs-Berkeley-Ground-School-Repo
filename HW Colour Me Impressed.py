import cv2
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
filename = DATA_DIR / "orange.webp"
img = cv2.imread(filename)

if img is None:
    raise FileNotFoundError(f"Couldn't read {filename}")

orangeLowerBound = (6, 100, 20)
orangeUpperBound = (25, 255, 255)

blueLowerBound = (97, 25, 90)
blueUpperBound = (130, 255, 255)

greenLowerBound = (35, 40, 18)
greenUpperBound = (85, 255, 255)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, orangeLowerBound, orangeUpperBound)
colourOnly = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("Orange Portion of Orange.webp", colourOnly)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, blueLowerBound, blueUpperBound)
colourOnly = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("Blue Portion of Orange.webp", colourOnly)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, greenLowerBound, greenUpperBound)
colourOnly = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("Green Portion of Orange.webp", colourOnly)