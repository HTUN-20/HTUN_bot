import discord
import random
import os

intents = discord.Intents.default()
intents.members = True
guild_a = random.randrange(0xc0ac, 0xc3f7)
guild_b = random.randrange(0xb77c, 0xb9c7)
guild_str = ''.join([chr(guild_a), chr(guild_b)])
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    global guild_str
    random_word()
    while guild_str == member.guild.name:
        random_word()
    await member.guild.edit(name=guild_str)
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

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status=discord.Status.online)
    print("================")
    return

@client.event
async def on_message(message):
    if message.content.startswith('!change'):
        random_word()
        while guild_str == message.guild.name:
            random_word()
        await message.guild.edit(name=guild_str)
        await message.channel.send('server name changed!')
        await message.channel.send("now, server name: %s "%(message.guild.name))
    return


client.run(os.environ['token'])