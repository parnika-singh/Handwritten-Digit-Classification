from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Set up Chrome options to use your specific profile
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\dell\AppData\Local\Google\Chrome\User Data")  # Path to Chrome user data
options.add_argument(r'--profile-directory=Profile 6')  # The specific profile directory

# Additional options to avoid the issue
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")  # Helps with memory issues
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("window-size=1200x600")  # Set window size

# Initialize the Chrome driver with the existing profile
driver = webdriver.Chrome(options=options)

# Open WhatsApp Web
baseurl = "https://web.whatsapp.com"
driver.get(baseurl)

# Wait for manual login (adjust this based on how long it takes to log in)
time.sleep(20)

# Read contacts from Excel file (ensure the file has 'Phone' and 'Name' columns)
contacts_df = pd.read_excel("demo1.xlsm")
phone_numbers = contacts_df['Phone'].tolist()
names = contacts_df['Name'].tolist()

# Predefined message template with placeholder for name
message_template = """
Dear *{name}*, Thank you for confirming your details for the *10th Edition of Samkalp's Vyakhyanmala* via the Google Form. We are pleased to cordially invite you to this highly anticipated event at *Akashvani Bhawan, New Delhi*, on *September 28th and 29th, 2024 (Saturday and Sunday)* at 09.30 am. Please remember to bring your *Aadhaar Card* as well as *e-card* on phone for entry, which will be facilitated through *Gate No. 2 & 3* of Akashvani Bhawan.

Location :  (https://maps.app.goo.gl/5wcqu9jcvMyRSpBJ9)

Thank you and regards, Samkalp Team

Madhu Prabhakar  (9811341607), Nalini Sachdeva (9717411222), Raju Chauhan (8588963296)
"""

# Send messages to contacts
for phonenum, name in zip(phone_numbers, names):
    try:
        # Personalize the message for each contact
        personalized_message = message_template.format(name=name)

        # Open WhatsApp chat for the given phone number
        driver.get(baseurl + "/send?phone=" + str(phonenum))
        time.sleep(20)  # Wait for the chat to load

        # Find the message input field and send the message
        content = driver.switch_to.active_element
        content.clear()
        content.send_keys(personalized_message)
        content.send_keys(Keys.RETURN)  # Press Enter to send the message

        time.sleep(10)  # Wait before sending to the next contact

    except Exception as e:
        print(f"Failed to send message to {phonenum}: {e}")

# Close the browser
driver.quit()
