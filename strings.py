from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import os

os.system('pip install --upgrade pip')
os.system('pip install telethon')

start_text = "Telebot Clone"
print(start_text)

print("Get APP ID and APP HASH from 'my.telegram.org'")

APP_ID = int(input("Enter APP ID :- "))
API_HASH = input("Enter API HASH :- ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as tb:
    print("\nBelow is your STRING_SESSION\n")
    print(tb.session.save())
    print("")
    print("This can be found in your saved messages in telegram too.")
    tele = tb.send_message("me", f"`{tb.session.save()}`")
    tele.reply("The above is the `STRING_SESSION`.\nDon't share this with anyone.")
