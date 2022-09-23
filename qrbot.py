#!python3.10


import discord
from dotenv import dotenv_values

# import sys
# import json
import qrcode

config = dotenv_values('config.env')
bot_token = config['BOT_TOKEN']


# 

class MyClient(discord.Client):
    # async def generate_qr(txt):
    #     qrcode = "je t'envoie le qr code pour :" + txt
    #     return qrcode

    async def on_ready(self):
        print('Logged on as', self.user)
        
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('/qr'):
            print(message.content)
            txt = message.content.split('/qr ')[1]
            print(txt)
            # qrcode = await self.generate_qr(txt)
            qrcode_img = qrcode.make(txt)
            type(qrcode_img)
            qrcode_img.save('qrcode_generated.png')
            await message.channel.send(file=discord.File('qrcode_generated.png'))



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(bot_token)