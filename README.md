# Message Forwarder to Telegram

A simple Telegram forwarder in Python3 that will automatically post message from another Telegram group/channel to your group/channel


## Setting up
### First:
`APP_ID` and `API_HASH` - Get it from my.telegram.org   
`FROM_CHANNEL` - Channel ID(s) split by space or just one channel ID.   
`TO_CHANNEL` - Channel ID(s) split by space or just one channel ID.   
`SESSION` - The pyrogram will require when you first use it, it will be saved in a .session file  

### Deploy

- Clone the repo:   <code>git clone https://github.com/lithoykai/TelegramForwarder-Python</code></br>
- Make a <code>.env</code> file in the root of the repo, like <a href="https://github.com/lithoykai/TelegramForwarder-Python/blob/main/.env.sample">.env.sample</a> and fill in the values.</br>
- use <code>pip3 install -r requirements.txt</code> to install requirements.</br>
- Use <code>python3 bot.py</code> to start the bot.</br>  


## Credits
> [Pyrogram](https://github.com/pyrogram/pyrogram)
