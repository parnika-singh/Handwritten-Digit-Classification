import pandas as pd
import pywhatkit as kit
import pyautogui
import time
import re

# Step 1: Read the Excel file and specify the sheet name
excel_file = 'data bhart.xlsx'
sheet_name = 'SAMKALP BHARAT'  # Replace with your sheet name
contacts_df = pd.read_excel(excel_file, sheet_name=sheet_name, dtype={'CONTACT DETAILS': str})

# Assuming the Excel columns are named 'NAME' and 'CONTACT DETAILS'
contacts = contacts_df[['NAME', 'CONTACT DETAILS']]

# Step 2: Read the pre-saved text file with a placeholder for the name
text_file = 'message.txt'
with open(text_file, 'r', encoding='utf-8') as file:
    message_template = file.read()

# Function to validate and format phone number
def validate_phone_number(phone_number):
    # Remove any spaces, dashes, or parentheses
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Check if the phone number starts with a '+'
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    # Validate the phone number (basic validation for length)
    if len(phone_number) < 10 or len(phone_number) > 15:
        return None
    
    return phone_number

# Step 3: Send WhatsApp messages with delay and retry mechanism
for index, contact in contacts.iterrows():
    name = contact['NAME']
    phone_number = contact['CONTACT DETAILS']
    
    # Validate and format the phone number
    phone_number = validate_phone_number(phone_number)
    if not phone_number:
        print(f"Invalid phone number for {name}: {contact['CONTACT DETAILS']}")
        continue
    
    # Replace the placeholder with the actual name
    message = message_template.replace('{name}', name)
    
    # Try sending the message up to 3 times
    sent = False
    for attempt in range(3):
        try:
            print(f"Attempt {attempt + 1} to send message to {name} ({phone_number})")
            kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=False)
            time.sleep(20)  # Wait for the message to be sent
            pyautogui.hotkey('ctrl', 'w')  # Close the browser tab
            print(f"Message sent to {name} ({phone_number})")
            sent = True
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed to send message to {name} ({phone_number}): {e}")
            time.sleep(5)  # Wait 5 seconds before retrying

    if not sent:
        print(f"Failed to send message to {name} ({phone_number}) after 3 attempts")

    # Add a delay between sending messages to avoid throttling
    time.sleep(15)  # Wait 15 seconds before sending the next message
