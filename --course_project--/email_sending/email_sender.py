import smtplib
from email.message import EmailMessage

user_password = input("Enter Gmail SMTP Password : ")

if user_password == "":
    exit()

email = EmailMessage()
email["from"] = "Seyed Alireza Fazeli Abeloui"
email["to"] = ["alirezafazeliTech@outlook.com", "as7010570@gmail.com"]
email["subject"] = "Message From Python"

email.set_content("Hello This Is a Test Message From Python !")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user="alirezafazeli34@gmail.com", password=user_password)
    smtp.send_message(email)
