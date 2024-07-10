import pandas as pd
import pywhatkit as kit
import pyautogui
import time
import re

# Function to validate and format phone number
def validate_number(phone_number):
    # Remove any non-digit characters except '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Ensure the number starts with '+'
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    
    # Remove any trailing zeros after the country code
    phone_number = phone_number.rstrip('0')
    
    # Validate length (assuming international format)
    if len(phone_number) < 10 or len(phone_number) > 15:
        return None
    
    return phone_number

# Step 1: Read the Excel file and specify the sheet name
excel_file = 'data bhart.xlsx'
sheet_name = 'FACULTIES'  # Replace with your sheet name
contacts_df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Assuming the Excel column is named 'CONTACT DETAILS' for phone numbers
contacts = contacts_df['CONTACT DETAILS']

# Step 2: Read the pre-saved text file with the message
text_file = 'message.txt'
with open(text_file, 'r', encoding='utf-8') as file:
    message = file.read()

# Step 3: Send WhatsApp messages with delay and retry mechanism
for phone_number in contacts:
    phone_number = str(phone_number)
    
    # Validate and format the phone number
    phone_number = validate_number(phone_number)
    if not phone_number:
        print(f"Invalid phone number: {phone_number}")
        continue
    
    # Try sending the message up to 3 times
    sent = False
    for attempt in range(3):
        try:
            # Increase wait_time to ensure the message is sent
            kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=False)
            time.sleep(20)  # Wait for the message to be sent
            pyautogui.hotkey('ctrl', 'w')  # Close the browser tab
            print(f"Message sent to {phone_number}")
            sent = True
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed to send message to {phone_number}: {e}")
            time.sleep(10)  # Wait 10 seconds before retrying

    if not sent:
        print(f"Failed to send message to {phone_number} after 3 attempts")

    # Add a delay between sending messages to avoid throttling
    time.sleep(15)  # Wait 15 seconds before sending the next message
