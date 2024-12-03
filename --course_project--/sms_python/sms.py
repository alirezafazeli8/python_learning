from env import *
from twilio.rest import Client
from plyer import notification

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_=to_phone_number,
#     body="""
#            مشترک گرامی ۸۰ در از بسته خود را مصرف کرده اید !
#     """,
#     to=my_phone_number,
# )


# print(message.sid)

notification.notify(
    title="SMS Sender : ",
    message="Your Message Has Bend Sent",
    timeout=5,
    toast=True,
    app_icon="./icon.ico",
)
