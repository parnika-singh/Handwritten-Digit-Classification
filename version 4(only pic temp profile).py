from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Temp\ChromeProfile")  # Use your Chrome profile path
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--remote-debugging-port=9222")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# Open WhatsApp Web
baseurl = "https://web.whatsapp.com"
driver.get(baseurl)

# Wait for manual login (adjust this based on how long it takes to log in)
time.sleep(20)

# Read contacts from Excel file (ensure the file has 'Phone' and 'Name' columns)
contacts_df = pd.read_excel("demo.xlsx")
phone_numbers = contacts_df['Phone'].tolist()
names = contacts_df['Name'].tolist()

# Path to the JPG file you want to send
image_path = r"C:\Users\dell\Desktop\send auto whatsapp mssg\929097.jpg"

# Send images to contacts
for phonenum, name in zip(phone_numbers, names):
    try:
        # Open WhatsApp chat for the given phone number
        driver.get(baseurl + "/send?phone=" + str(phonenum))
        time.sleep(15)  # Wait for the chat to load

        # Click the attachment (clip) icon
        attach_button = driver.find_element(By.XPATH, "//div[@title='Attach']")
        attach_button.click()
        time.sleep(2)

        # Upload the JPG image
        image_input = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
        image_input.send_keys(image_path)

        time.sleep(5)  # Wait for the image to upload

        # Press Enter to send the image
        send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
        send_button.click()

        time.sleep(8)  # Wait before sending to the next contact

    except Exception as e:
        print(f"Failed to send image to {phonenum}: {e}")

# Close the browser
driver.quit()
