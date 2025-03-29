import pywhatkit
import time

phn_no = "+919678972713"
msg = "Hello, this is a test message from WhatsApp Automation!"
hrs = 20
min = 10

for i in range(10):
    pywhatkit.sendwhatmsg(phn_no, msg, hrs, min + i)
    time.sleep(5)  # Wait for 5 seconds before sending the next message
