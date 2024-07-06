import pyautogui
import time

print("You have 5 seconds to move your mouse to the search box...")
time.sleep(5)
search_box_coords = pyautogui.position()
print(f"Search box coordinates: {search_box_coords}")

print("You have 5 seconds to move your mouse to the message box...")
time.sleep(5)
message_box_coords = pyautogui.position()
print(f"Message box coordinates: {message_box_coords}")
