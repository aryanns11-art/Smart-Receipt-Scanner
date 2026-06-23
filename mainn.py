import easyocr
import cv2
import os

reader = easyocr.Reader(['en'])

image_path = input("Enter receipt image path: ").strip()

if not os.path.exists(image_path):
    print("Image file not found!")
    exit()

image = cv2.imread(image_path)

if image is None:
    print("Unable to load image!")
    exit()

print("\nScanning receipt...\n")

results = reader.readtext(image)

print("=" * 40)
print("Extracted Text")
print("=" * 40)

for result in results:
    text = result[1]
    print(text)

print("=" * 40)
print("\nScan Complete!")