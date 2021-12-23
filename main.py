import discord, asyncio, os
from discord.ext import commands

TOKEN = "OTIzNDI2MjgyNjczNDIyMzU2.YcP1vg.1Rxu1_Z8oAmu2hCdT-uhd8fp7DY"

game = discord.Game("짬씨처리")
bot = commands.Bot(command_prefix="$", status = discord.Status.online, activity=game)
client = discord.Client()

@bot.event
async def on_ready():
    print("Activated")



@bot.command()
async def airman(ctx):
    user = ctx.message.author
    voice_channel=user.voice.voice_channel
    channel=None

    if voice_channel != None:
        channel = voice_channel.name
        vc = await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player("bgm/airman.mp3")
        player.start
        while not player.is_done():
            await asyncio.sleep(1)
        player.stop()
        await vc.disconnect()
    else:
        await client.say("보이스 채널에 먼저 들어가세요~")

@bot.command()
async def leave(ctx):
    if(ctx.guild.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.channel.send("난 음성채팅에 안들어와있다 애송이")
        

@bot.command()
async def list(ctx):
    embed = discord.Embed(title = ":blue_book: 김휘준 작가님의 소설들", description = "개쩐다", color=0x00FFE1)
    embed.add_field(name="비행기에서 생긴 일", value = "비행기에서 서영탁과 장진우에게 일어난 일.",inline = True)
    embed.set_footer(text = "Copyright 김휘준")
    await ctx.channel.send(embed = embed)
    def check(message):
        return message.author
    try:
        answer = await bot.wait_for("message",timeout=10.0,check=check)
    except asyncio.TimeoutError:
        await ctx.channel.send("넌 방금 나에게 세가지 잘못을 저질렀다!")
    if(answer.content == "1"):
        await ctx.channel.send(file = discord.File(r"C:\Users\Ian\Desktop\실버가... 말대꾸\library\temp.txt"))
    else:
        await ctx.channel.send("그딴건 없다 애송이")
        

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    if message.author.bot:
        return None
    if(username == "hartzling"):
        if("골드" in message.content):
            await message.channel.send(file=discord.File(r"C:\Users\Ian\Desktop\실버가... 말대꾸\images\notgold.png"))
        if(message.content.endswith("?")):
            await message.channel.send(file=discord.File(r"C:\Users\Ian\Desktop\실버가... 말대꾸\images\maldeggu.jpeg"))
            await message.channel.send("실버가... 말대꾸?")
    if(username=="심규민"):
        await message.channel.send("억까와의 타협은 없다.")
    if("섹스" in user_message):
        await message.add_reaction("\N{White Right Pointing Backhand Index}")
        await message.add_reaction("\N{OK Hand Sign}")
    if("개추" in user_message):
        await message.add_reaction("\N{Thumbs Up Sign}")
    if("비추" in user_message):
        await message.add_reaction("\N{Thumbs Down Sign}")
    if("응애" in user_message):
        await message.add_reaction("\N{Baby}")
    if("흠" in user_message):
        await message.add_reaction("\N{Thinking Face}")


bot.run(TOKEN)