import discord,random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('.bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith(".şifre_oluştur"):
        uzunluk = int(str(message.content)[14:])
        await message.channel.send(gen_pass(uzunluk))
    else:
        await message.channel.send(message.content)

client.run("ENTER YOUR TOKEN HERE")
