from bs4 import BeautifulSoup
import requests
import ssl
import smtplib

port = 587 # For SSL
smtp_server = "smtp.gmail.com"  # web server to send through
password = ""

sender_email = ""
receiver_email = ""

# sites of interest in a dictionary...

computer_parts = {
  "monitor_base": "https://www.viewsonic.com/parts/pl-00009513.html",
  "monitor_arm": "https://www.viewsonic.com/parts/c-00013429.html"
}

part_availability = {
  "monitor_base": "",
  "monitor_arm": ""
}

for part, link in computer_parts.items():

    site = requests.get(link)

    soup = BeautifulSoup(site.text, features="html.parser")

    availability = soup.find("div", {"class": "col-12 product-info"})

    part_availability[part] = availability

message_info = "Monitor Base has availability: " + str(part_availability["monitor_base"]) + \
                    ". Monitor arm has availability: " + str(part_availability["monitor_base"])

message = """\
Subject: Part Availability

This message is sent from Python. and so is this """ + message_info

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



