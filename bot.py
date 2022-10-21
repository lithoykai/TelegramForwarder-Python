from pyrogram import Client
from decouple import config
from pyrogram import filters

print("Starting system...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")


FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotUser = Client('BiroZord', APP_ID, API_HASH, workers= 6) #your user is necessary to receive messages
    #if you want use yout bot to send message: 
    # Bot = Client('Bot',APP_ID, API_HASH, bot_token= "" ) 
    # Bot.start()

except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotUser.on_message(filters.chat(FROM) & filters.incoming)
async def work(message):

    for i in TO:
        
        await BotUser.send_message(i, message.text) #if you want use your user to send message
        # await Bot.send_message(i, message.text) #if you want use the bot to send message

print("Bot has started.")
BotUser.run()
