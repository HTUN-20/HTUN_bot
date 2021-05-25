import discord
import random
import asyncio
import os

intents = discord.Intents.default()
intents.members = True
guild_a = random.randrange(0xc0ac, 0xc3f7)
guild_b = random.randrange(0xb77c, 0xb9c7)
guild_str = ''.join([chr(guild_a), chr(guild_b)])
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    channel = client.get_channel(845259246123614231)
    global guild_str
    random_word()
    while guild_str == member.guild.name:
        random_word()
    await member.guild.edit(name=guild_str)
    await channel.send("server name: %s " % (member.guild.name))
    return



# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status=discord.Status.online)
    print("================")
    return



# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    global guild_str
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('반가워!')

    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

    if message.content.startswith('안할래'):
        channel = message.channel
        await channel.send('그래 하지마!')

    if message.content.startswith('!change'):
        random_word()
        while guild_str == message.guild.name:
            random_word()
            print("again")
        await message.guild.edit(name=guild_str)
        await message.channel.send('server name changed!')
        await message.channel.send("now, server name: %s "%(message.guild.name))
    return

# 랜덤 단어
def random_word():
    global guild_str
    global guild_b
    global guild_a
    guild_a = random.randrange(0xc0ac, 0xc3f7)
    guild_b = random.randrange(0xb77c, 0xb9c7)
    guild_str = ''.join([chr(guild_a), chr(guild_b)])
    return

client.run(os.environ['token'])