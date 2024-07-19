import pyautogui
import time
import schedule
from datetime import datetime, timedelta

def send_whatsapp_message(contact_name, message):
    # Open WhatsApp Desktop app
    pyautogui.hotkey('win', 's')  # Open Windows search
    time.sleep(1)
    pyautogui.write('WhatsApp')  # Search for WhatsApp
    time.sleep(1)
    pyautogui.press('enter')  # Open WhatsApp Desktop
    time.sleep(5)  # Wait for WhatsApp to open

    # Select the contact
    pyautogui.hotkey('ctrl', 'f')  # Focus search box in WhatsApp
    time.sleep(1)
    pyautogui.write(contact_name)  # Type the contact's name
    time.sleep(2)
    pyautogui.press('down')  # Press down arrow to select the contact
    time.sleep(1)
    pyautogui.press('enter')  # Confirm the selection
    time.sleep(1)

    # Type and send the message
    pyautogui.write(message)  # Type the message
    time.sleep(1)
    pyautogui.press('enter')  # Send the message
    pyautogui.hotkey('alt', 'f4')  # close whatsapp

def schedule_message(contact_name, message, scheduled_time):
    # Calculate the delay
    now = datetime.now()
    target_time = datetime.strptime(scheduled_time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
    if target_time < now:
        target_time += timedelta(days=1)
    delay = (target_time - now).total_seconds()
    
    print(f"Message scheduled to be sent to {contact_name} at {scheduled_time}")
    time.sleep(delay)
    send_whatsapp_message(contact_name, message)

if __name__ == "__main__":
    contact_name = "Namw"  # Replace with the contact's name as it appears in WhatsApp
    message = "Hello, this is an automated message."
    scheduled_time = "22:48"  # Time in HH:MM format, 24-hour clock

    schedule_message(contact_name, message, scheduled_time)


# def schedule_message(contact_name, message, scheduled_time):
#     # Schedule the message to be sent at the specified time
#     schedule.every().day.at(scheduled_time).do(send_whatsapp_message, contact_name=contact_name, message=message)
#     print(f"Message scheduled to be sent to {contact_name} at {scheduled_time}")

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     contact_name = "Name"  # Replace with the contact's name as it appears in WhatsApp
#     message = "Hello, this is an automated scheduled message for 22:17."
#     scheduled_time = "22:17"  # Time in HH:MM format, 24-hour clock

#     schedule_message(contact_name, message, scheduled_time)