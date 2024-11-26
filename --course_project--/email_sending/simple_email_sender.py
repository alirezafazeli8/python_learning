import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Satan"
email["to"] = [
    "alirezafazeli34@gmail.com",
    "alirezafazeliTech@outlook.com",
    "as7010570@gmail.com",
]
email["subject"] = "Sata have message for you"

email.set_content(
    """
                  
                  <h1> درود خدا بر شما باد <h1/>
                  <img src="./assets/SMTP-Gif.gif">
                  
                  """,
    subtype="html",
)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test@gmail.com", "pass")
    smtp.send_message(email)
