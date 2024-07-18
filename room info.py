import pandas as pd
import pywhatkit as kit
import pyautogui
import time
import re

# Function to validate and format phone number
def validate_number(phone_number):
    phone_number = re.sub(r'[^\d+]', '', phone_number)  # Remove non-digit characters except '+'
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number  # Ensure the number starts with '+'
    #phone_number = phone_number.rstrip('0')
    if len(phone_number) < 10 or len(phone_number) > 15:
        return None  # Return None for invalid numbers
    return phone_number

# Step 1: Read the Excel file and specify the sheet name
excel_file = 'with.xlsx'
sheet_name = 'Sheet1'  # Replace with your sheet name
contacts_df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Assuming the Excel columns are named 'NAME', 'CONTACT DETAILS', 'LINK', 'DHARAMSHALA ALLOTED', and 'ROOM NO. ALOTTED'
contacts = contacts_df[['NAME', 'CONTACT DETAILS', 'LINK', 'DHARAMSHALA ALLOTED', 'ROOM NO. ALOTTED']]

# The message template with placeholders
message_template = """
Accommodation & Transportation 
12th, 13th & 14th July 2024

Namaskar {name} Ji,
Samkalp family is looking forward to welcome you at Ayodhya, sharing the Accommodation information with you. 

• Your Accommodation is at {dharam} and Room No. is {room}
{link}

Breakfast/Lunch will be served at Chhoti Chawani 10 am onwards.

Those who are coming by Road (i.e. by car/cab) can reach directly to Chhoti Chawani (Parking is available only at Chhoti Chawani).
Address and location is 
https://maps.app.goo.gl/RmZqfCfNUeyUYyBC8

You can reach out at any time for any kind of support to
1. Nalini Sachdeva 
9717411222
2. Madhu Prabhakar 
9811341607
3. Ankur Agrawal 
9873694016
"""

# Step 3: Send WhatsApp messages with delay and retry mechanism
for index, contact in contacts.iterrows():
    name = str(contact['NAME'])
    dharamshala = contact['DHARAMSHALA ALLOTED']
    room = str(contact['ROOM NO. ALOTTED'])
    link = contact['LINK']
    phone_number = str(contact['CONTACT DETAILS'])
    
    # Validate and format the phone number
    phone_number = validate_number(phone_number)
    if not phone_number:
        print(f"Invalid phone number: {phone_number}")
        continue
    
    # Replace the placeholders with actual values
    message = message_template.replace('{name}', name)
    message = message.replace('{dharam}', dharamshala)
    message = message.replace('{room}', room)
    message = message.replace('{link}', link)
    
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
