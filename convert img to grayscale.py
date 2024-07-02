from PIL import Image
import matplotlib.pyplot as plt

# Open an image file
img = Image.open('one.jpg')

# Resize the image to 20x20 pixels
img_resized = img.resize((20, 20))

# Convert the resized image to grayscale
img_gray = img_resized.convert("L")

# Print image properties to confirm changes
print("Image format:", img_gray.format)
print("Image size:", img_gray.size)
print("Image mode:", img_gray.mode)

# Display the original image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")

# Display the resized grayscale image
plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap='gray')
plt.title("20x20 Grayscale Image")

plt.show()

pix_val = list(img_gray.getdata())
print(type(pix_val))

