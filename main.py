import discord, asyncio, os, nacl, random
from discord.ext import commands

intents=discord.Intents.default()
intents.members=True
game = discord.Game("대통령 선거")
bot = commands.Bot(command_prefix="$", status = discord.Status.online, activity=game,intents = intents)
client = discord.Client()

@bot.event
async def on_ready():
    global russian_idx
    russian_idx = 0
    global russian_open
    russian_open = False
    global russian_start
    russian_start = False
    global russian_list
    russian_list = []
    print("Activated")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "아가")
    await member.add_roles(role)
@bot.command()
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("너는 음성채널에 안들어가있다 애송이")
@bot.command()
async def airman(ctx):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",source="./bgm/airman.mp3"))

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
        await ctx.channel.send(file = discord.File(r"library/temp.txt"))
    else:
        await ctx.channel.send("그딴건 없다 애송이")



@bot.command()
async def 러시작(ctx):
    global russian_open
    global russian_list
    global russian_start
    if russian_open:
        await ctx.channel.send("게임은 이미 시작되었다고 베이비")
        return
    russian_open = True
    await ctx.channel.send("25초 후에 대통령 선거를 시작하겠다!")
    await asyncio.sleep(25)
    if not(russian_open):
        return
    if len(russian_list) < 2:
        await ctx.channel.send("참가자 부족.")
        russian_open = False
        russian_list = []
        russian_start = False
        russian_open = False
        return
    russian_start = True
    await ctx.channel.send(file=discord.File(r"images/matjjang.png"))
    await ctx.channel.send("게임 시작.\n너에게 사이퍼(맞짱)을 신청한다 " + russian_list[russian_idx].mention + "!")
@bot.command()
async def 러종료(ctx):
    global russian_start
    global russian_open
    global russian_idx
    global russian_list
    russian_list = []
    russian_start = False
    russian_open = False
    russian_idx = 0
    await ctx.channel.send("게임이 종료되었다")
@bot.command()
async def 러참가(ctx):
    global russian_start
    global russian_open
    global russian_list
    if russian_start:
        await ctx.channel.send("새끼가 뒷북을?")
        return
    if not(russian_open):
        await ctx.channel.send("게임은 시작되지 않았다.")
        return
    if ctx.author in russian_list:
        await ctx.channel.send("넌 이미 참가중이다.")
        return
    russian_list.append(ctx.author)
    await ctx.channel.send(ctx.author.mention + " 게임참가")
@bot.command()
async def 러당겨(ctx):
    global russian_start
    global russian_open
    global russian_idx
    global russian_list
    if not(russian_open):
        await ctx.channel.send("게임은 시작되지 않았다.")
        return
    if not(russian_start):
        await ctx.channel.send("참가자들을 받는중이다.")
        return
    if ctx.author == russian_list[russian_idx]:
        if random.randrange(1,67) < 12:
            await ctx.channel.send("ㅅㄱㅃㅇ")
            role = discord.utils.get(ctx.guild.roles, name = "입마개")
            await ctx.author.add_roles(role)
            russian_list = []
            russian_start = False
            russian_open = False
            russian_idx = 0
        else:
            russian_idx = (russian_idx+1)%len(russian_list)
            await ctx.channel.send("다음 사이퍼(맞짱) 상대는 " + russian_list[russian_idx].mention + " 다!")
    


@bot.command()
async def spam(ctx,*args):
    msg = ""
    for i in range(len(args) - 1):
        msg += args[i] + " "
    number = int(args[len(args)-1])
    if number > 10:
        number = 10
    for i in range(number):
        await ctx.channel.send(f"{msg.rstrip()}")

@bot.command()
async def molu(ctx):
    await ctx.channel.send(file=discord.File(r"images/몰루.gif"))

@bot.command()
async def backdrillon(ctx):
    await ctx.channel.send(file=discord.File(r"images/BackDrillKickOn.PNG"))

@bot.command()
async def backdrilloff(ctx):
    await ctx.channel.send(file=discord.File(r"images/BackDrillKickOff.png"))


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    if message.author.bot:
        return None
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
    
    # if(str(message.author).split("#")[1] == "0778"):
    #     if("골드" in message.content):
    #         await message.channel.send(file=discord.File(r"images/notgold.png"))
    #     if(message.content.endswith("?")):
    #         await message.channel.send(file=discord.File(r"images/maldeggu.jpeg"))
    #         await message.channel.send("실버가... 말대꾸?")
    if(username=="심규민"):
        await message.channel.send("억까와의 타협은 없다.")
    

TOKEN = os.environ["BOT_TOKEN"];
bot.run(TOKEN)