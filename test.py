# bot.py
from distutils.cmd import Command
from importlib.metadata import requires
from math import perm
from optparse import Option
import os
import random
from tkinter.tix import Tree
from typing import Any, Text
from unicodedata import name
from urllib import response
import discord
from discord import channel
from discord import message
from discord import embeds
from discord import user
from discord import member
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from dotenv import load_dotenv
from datetime import datetime
from dotenv.main import with_warn_for_invalid_lines
import requests
from discord.utils import get
from discord.ext import commands
import aiohttp
from discord_together import DiscordTogether
import pytz
from translate import Translator
import interactions
from typing import List




#
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

#setup ready run
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"{client.user.name} đã kết nối tới Discord")
        client.togetherControl = await DiscordTogether(TOKEN)

        activity = discord.Game(name='/help để nhận hỗ trợ', type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)


client = aclient()
tree = app_commands.CommandTree(client)



#commands list
@tree.command(name="help", description = "Xem tất cả các lệnh của bot")
async def self(interaction: discord.Interaction):
    myembed = discord.Embed (title = 'Peanutss Bot (v3.0)', description = 'Sử dụng `/[lệnh]` để tương tác với bot', color = discord.Color.gold())
    myembed.set_author (name = "Danh Sách Lệnh")
    myembed.add_field (name = "💬 Tương Tác - (4)", value = "`số-may-mắn` `covid19` `covid19vn` `máy-tính-tuổi`", inline=False)
    myembed.add_field (name = "😊 Fun - (15)", value = " `văn-mẫu` `hug` `smile` `kill` `cry` `kiss` `highfive` `pat` `smug` `bonk` `lick` `awoo` `blush` `wave` `slap`", inline=False)
    myembed.add_field (name = "🎁 Media - (7)", value = "`meme` `darkmeme` `girl` `cat` `dog` `food` `waifu` ", inline=False)
    myembed.add_field (name = "📺 Giải Trí - (2)", value = "`action` `youtube`", inline=False)
    myembed.add_field (name = "🔞 NSFW - (1)", value = "`hentai`", inline=False)
    myembed.add_field (name = "🪙 Tiền Tệ - (1)", value = "`binance`", inline=False)
    myembed.add_field (name = "⚠️Quản Lí - (3)", value = "`kick` `ban` `unban`: Comming Soon", inline=False)
    myembed.add_field (name = "💡 Tính Năng Bổ Trợ - (2)", value = "`dịch` `sắp-tết`", inline=False)
    myembed.add_field (name = "⚙️ Guilds - (4)", value = "`ping` `help` `server-status` `server-avatar`", inline=False)
    myembed.add_field (name = "☎️ Contact - (3):", value = "`contact` `donate` `invite`", inline=False)
    myembed.set_footer(text="Big Update: Chuyển toàn bộ các câu lệnh sang Slash Commands {/}")
    await interaction.response.send_message(embed = myembed, ephemeral = False)


#
@tree.command(name="máy-tính-tuổi-thông-minh", description = "Dùng để tính toán tuổi của bạn")
async def self(interaction: discord.Interaction, nhap_tuoi: str):
    await interaction.response.send_message(f"Bạn đã {nhap_tuoi} tuổi rồi", ephemeral = False)

######
@tree.command(name="meme", description = "Gửi cho bạn một meme")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            memeembed = discord.Embed(color = discord.Color.green())
            memeembed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            memeembed.set_footer(text=f"Meme của mọi nhà")
    await interaction.response.send_message(embed = memeembed, ephemeral = False)


######
@tree.command(name="darkmeme", description = "Gửi cho bạn một darkmeme")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/dankmemes/new.json?sort=hot") as r:
            darkmemes = await r.json()
            darkembed = discord.Embed(color = discord.Color.red())
            darkembed.set_image(url=darkmemes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            darkembed.set_footer(text=f"Đảk Mêm")
    await interaction.response.send_message(embed = darkembed, ephemeral = False)

######
@tree.command(name="số-may-mắn", description = "Cho bạn một con số may mắn trong ngày")
async def self(interaction: discord.Interaction):
    lknum = random.randint(1,99)
    peabot_rep = 'Con số may mắn hôm nay của bạn là: ' + str(lknum) + ' 🥳' 

    await interaction.response.send_message(f'{peabot_rep}\n Nhớ cầm lấy nó đi đánh đề nhé XD ^^')

######
@tree.command(name="cat", description = "Gửi cho bạn một tấm hình mèo")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
    #api đuồi bầu gắn url trong 1 list, phải tách bằng 1 int chứ không thể tách như thường
        async with cs.get("https://api.thecatapi.com/v1/images/search") as r:
            cats = await r.json()

            catch = cats[0] #trả về dãy như api thường (mất [])
            catlink = catch['url'] #tách data như thường

            catembed = discord.Embed(color = discord.Color.blue())
            catembed.set_image(url=catlink)
            catembed.set_footer(text=f"Mèo méo meo mèo meo")
        
    await interaction.response.send_message(embed = catembed, ephemeral = False)


######
@tree.command(name="dog", description = "Gửi cho bạn một bức hình chó")
async def self(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
            dogs = await r.json()
            dogsembed = discord.Embed(color = discord.Color.gold())
            dogsembed.set_image(url=dogs["message"])
            dogsembed.set_footer(text=f"Cute Dogs :3")
    await interaction.response.send_message(embed = dogsembed, ephemeral = False)


######
@tree.command(name="food", description = "Gửi cho bạn một bức hình toàn là đồ ăn")
async def self(interaction: discord.Interaction):       
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/food/new.json?sort=hot") as r:
            foods = await r.json()
            foodsembed = discord.Embed(color = discord.Color.green())
            foodsembed.set_image(url=foods["data"]["children"][random.randint(0, 25)]["data"]["url"])
            foodsembed.set_footer(text=f'Mlem mlem')
    await interaction.response.send_message(embed = foodsembed, ephemeral = False)

######
@tree.command(name="waifu", description = "Gửi cho bạn một bức hình waifu")
async def self(interaction: discord.Interaction):       
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://api.waifu.pics/sfw/waifu") as r:
            waifu = await r.json()
            waifuembed = discord.Embed(color = discord.Color.dark_orange())
            waifuembed.set_image(url=waifu["url"])
            waifuembed.set_footer(text=f"Who is your waifu? ❤️")
    await interaction.response.send_message(embed = waifuembed, ephemeral = False)


######
@tree.command(name="hentai", description = "Lệnh chỉ được dùng trong phòng có tag NSFW 'waifu', 'neko', 'blowjob'", nsfw = 'true')
async def hentai(interaction: discord.Interaction, style: str):
        link = "https://api.waifu.pics/nsfw/"
        fullurl = link + style
        async with aiohttp.ClientSession() as cs:
            async with cs.get(fullurl) as r:
                nsfw = await r.json()
                nsfwembed = discord.Embed(color = discord.Color.dark_red())
                nsfwembed.set_image(url=nsfw["url"])
                nsfwembed.set_footer(text=f"⚠️| Not Safe For Work!!")
                await interaction.response.send_message(embed = nsfwembed, ephemeral = False)


@hentai.autocomplete('style')
async def hentai_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    style = ['waifu','neko','blowjob']
    return [
        app_commands.Choice(name=stl, value=stl)
        for stl in style if current.lower() in stl.lower()
        ]

#######
@tree.command(name="girl", description = "Gửi cho bạn những bức hình thattuoimat❤️")
async def self(interaction: discord.Interaction):

    lines = open('list_girl.txt').read().splitlines()
    link = random.choice(lines)
   
    girlembed = discord.Embed(color = discord.Color.from_rgb(255,105,180))
    girlembed.set_image(url=link)
    girlembed.set_footer(text=f"Mỗi bức ảnh, một niềm vui ❤️")
    await interaction.response.send_message(embed = girlembed, ephemeral = False)


@tree.command(name="youtube", description = "Xem Youtube trực tiếp trên Discord")
async def youtube(interaction: discord.Interaction, member :  discord.Member):
    channel = member.voice.channel
    if channel:   #kiểm tra người trong voice 
        await channel.connect()
        #tạo url youtube together
        #link = await client.togetherControl.create_link(interaction.author.voice.channel.id, 'youtube')
        #await interaction.response.send_message(f'Nhấn vào link để xem Youtube: {link}', ephemeral = False)
        #await interaction.response.send_message('Lưu Ý: Chức năng chỉ hoạt động trên các thiết bị PC - Laptop, không hỗ trợ cho các thiết bị điện thoại!!', ephemeral = False)  
    else:
        await interaction.response.send_message('❌| Bạn phải vào kênh voice trước!!', ephemeral = False)



@tree.command(name="sắp-tết", description = "Đếm ngược ngày đến Tết Nguyên Đán")
async def self(interaction: discord.Interaction):   
    #set up ngay den tet
    ngay_tet = datetime.strptime('Jan 22 2023 00:00', '%b %d %Y %H:%M') 
    hom_nay = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) #set timezone về VN
    count = int((ngay_tet - hom_nay.replace(tzinfo=None)).total_seconds())

    #dem ngay gio
    ngay = count//86400
    gio = (count-ngay*86400)//3600
    phut = (count-ngay*86400-gio*3600)//60
    giay = count-ngay*86400-gio*3600-phut*60
    await interaction.response.send_message(f"Chỉ còn **{ngay}** ngày **{gio}** giờ **{phut}** phút **{giay}** giây nữa là đến tết 2023 rồi!!!!", ephemeral = False) 

##########
@tree.command(name = "dịch", description = "Dịch bất cứ ngôn ngữ nào trên thế giới: en, ja, vi,...")
async def translate(interaction: discord.Interaction, input_lang: str, output_lang: str, noidung: str):
    #khai bao language
    if input_lang == "Tiếng Việt":
        in_lang = 'vi'
    if input_lang == "Tiếng Anh":
        in_lang = 'en'
    if input_lang == "Tiếng Nhật":
        in_lang = 'ja'
    if input_lang == "Tiếng Trung (Phồn Thể)":
        in_lang = 'zh-tw'
    if input_lang == "Tiếng Trung (Giản Thể)":
        in_lang = 'zh-cn'
    if input_lang == "Tiếng Indo":
        in_lang = 'id'
    if input_lang == "Tiếng Hàn":
        in_lang = 'ko'
    if input_lang == "Tiếng Thái":
        in_lang = 'th'
    if input_lang == "Tiếng Đức":
        in_lang = 'de'
    if input_lang == "Tiếng Pháp":
        in_lang = 'fr'
    if input_lang == "Tiếng Nga":
        in_lang = 'ru'
    if input_lang == "Tiếng Tây Ban Nha":
        in_lang = 'es'
    if input_lang == "Tiếng Ý":
        in_lang = 'it'

#output lang
    if output_lang == "Tiếng Việt":
        out_lang = 'vi'
    if output_lang == "Tiếng Anh":
        out_lang = 'en'
    if output_lang == "Tiếng Nhật":
        out_lang = 'ja'
    if output_lang == "Tiếng Trung (Phồn Thể)":
        out_lang = 'zh-tw'
    if output_lang == "Tiếng Trung (Giản Thể)":
        out_lang = 'zh-cn'
    if output_lang == "Tiếng Indo":
        out_lang = 'id'
    if output_lang == "Tiếng Hàn":
        out_lang = 'ko'
    if output_lang == "Tiếng Thái":
        out_lang = 'th'
    if output_lang == "Tiếng Đức":
        output_lang = 'de'
    if output_lang == "Tiếng Pháp":
        out_lang = 'fr'
    if output_lang == "Tiếng Nga":
        out_lang = 'ru'
    if output_lang == "Tiếng Tây Ban Nha":
        out_lang = 'es'
    if output_lang == "Tiếng Ý":
        out_lang = 'it'
    translator = Translator(from_lang=f"{in_lang}", to_lang=f"{out_lang}")
    result = translator.translate(noidung)

    dich_embed = discord.Embed (title = f'Kết quả dịch từ {input_lang} sang {output_lang}:', color = discord.Color.green())
    dich_embed.add_field (name = 'Văn Bản Gốc:', value = noidung, inline = False)
    dich_embed.add_field (name = 'Văn Bản Sau Khi Dịch: ', value = result, inline = False)
    dich_embed.set_footer (text = f'Lệnh được thực hiện bởi: {interaction.user}')
    await interaction.response.send_message(embed = dich_embed, ephemeral = False)

@translate.autocomplete('input_lang')
async def translate_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    input_lang = ['Tiếng Việt', 'Tiếng Anh', 'Tiếng Nhật', 'Tiếng Trung (Phồn Thể)','Tiếng Trung (Giản Thể)', 'Tiếng Indo', 'Tiếng Hàn', 'Tiếng Thái', 'Tiếng Đức', 'Tiếng Pháp', 'Tiếng Nga', 'Tiếng Tây Ban Nha', 'Tiếng Ý']
    return [
        app_commands.Choice(name=lang, value=lang)
        for lang in input_lang if current.lower() in lang.lower()
        ]

@translate.autocomplete('output_lang')
async def translate_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    output_lang = ['Tiếng Việt', 'Tiếng Anh', 'Tiếng Nhật', 'Tiếng Trung (Phồn Thể)','Tiếng Trung (Giản Thể)', 'Tiếng Indo', 'Tiếng Hàn', 'Tiếng Thái', 'Tiếng Đức', 'Tiếng Pháp', 'Tiếng Nga', 'Tiếng Tây Ban Nha', 'Tiếng Ý']
    return [
        app_commands.Choice(name=lang, value=lang)
        for lang in output_lang if current.lower() in lang.lower()
    ]
##########

#
@tree.command(name="contact", description = "Thông tin liên hệ với Developer")
async def self(interaction: discord.Interaction):   
    contactembed = discord.Embed (color = discord.Color.dark_grey())
    contactembed.set_author (name = "Liên hệ với Dev tại:")
    contactembed.add_field (name = "Discord Account ^^:", value = 'Peanuts Is Me (Andy)#2757', inline=False)
    contactembed.add_field (name = "Link Facebook ^^:", value = 'https://facebook.com/yt.andymusic', inline=False)
    contactembed.add_field (name = "Link Youtube ^^:", value = 'https://youtube.com/c/andymusicc', inline=False)
    contactembed.add_field (name = "Github:", value = 'https://github.com/anphongdoa5', inline=False)
    await interaction.response.send_message(embed = contactembed, ephemeral = False)

#
@tree.command(name="ping", description = "Kiểm tra độ trễ của bot")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Độ trễ của tớ là {round(client.latency * 1000)}ms')

#
@tree.command(name="donate", description = "Ủng hộ Developer một vài ly cafe")
async def self(interaction: discord.Interaction):
    donateembed = discord.Embed (title = 'Playerduo Link:', color = discord.Color.orange())
    donateembed.set_author (name = "Donate ủng hộ Dev ly cà phê tại đây:")
    donateembed.add_field (name = "https://playerduo.com/peanutss", value = "Cảm ơn bạn rất nhiều <3", inline=False)
    await interaction.response.send_message(embed = donateembed, ephemeral = False)

#
@tree.command(name="covid19vn", description = "Xem tình hình, diễn biến dịch COVID-19 tại Việt Nam")
async def self(interaction: discord.Interaction):
    response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/vietnam')
    data = response.json()
    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']
    peabot_rep = f"TÌNH HÌNH COVID 19 TẠI VIỆT NAM:\n☣  Số Người Nhiễm: {cases} người\n💀  Số Người Tử Vong: {deaths} người\n✅  Số Người Bình Phục: {recovered} người"
    await interaction.response.send_message(peabot_rep, ephemeral = False)

#
@tree.command(name="covid19", description = "Xem tình hình, diễn biến dịch COVID-19 trên toàn thế giới")
async def self(interaction: discord.Interaction):
    response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/world')
    data = response.json()
    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']
    peabot_rep = f"TÌNH HÌNH COVID 19 TRÊN THẾ GIỚI:\n☣  Số Người Nhiễm: {cases} người\n💀  Số Người Tử Vong: {deaths} người\n✅  Số Người Bình Phục: {recovered} người"
    await interaction.response.send_message(peabot_rep, ephemeral = False)

#
@tree.command(name="invite", description = "Lấy link mời bot vào server")
async def self(interaction: discord.Interaction):
    inviteembed = discord.Embed (color = discord.Color.green())
    inviteembed.set_author (name = "Link Invite Peanutss Bot")
    inviteembed.add_field (name = "Link:", value = 'https://discord.com/oauth2/authorize?client_id=728462830407254088&permissions=34631477334&scope=bot', inline=False)
    await interaction.response.send_message(embed = inviteembed, ephemeral = False)

#
@tree.command(name="server-status", description = "Kiểm tra thông tin của server")
async def self(interaction: discord.Interaction):
    statembed = discord.Embed(title=f'Thông tin server {interaction.guild.name} ',description= '', color = discord.Color.from_rgb(147,112,219))
    statembed.set_thumbnail(url=f'{interaction.guild.icon}')

    statembed.add_field(name='Tên Server:', value=f'{interaction.guild.name}', inline=True)
    statembed.add_field(name='Số Lượng Thành Viên:', value=f'{interaction.guild.member_count} thành viên', inline=True)
    statembed.add_field(name='Chủ Server:', value=f'<@{interaction.guild.owner_id}>', inline=True)
    statembed.add_field(name='Server Tạo Lúc:', value=f'{interaction.guild.created_at.strftime("%#d %B %Y, %H:%M")}')

    statembed.add_field(name='Trạng Thái Bot:', value='🟢 Online!!', inline = True)
    statembed.add_field(name='Latency:', value=f'Độ trễ bot: {round(client.latency * 1000)}ms', inline=True)
    statembed.set_footer(text=f'Bởi: {interaction.user}!')

    await interaction.response.send_message(embed = statembed, ephemeral = False)

#
@tree.command(name="server-avatar", description = "Xem ảnh đại diện của server")
async def self(interaction: discord.Interaction):
    avaembed = discord.Embed(title=f'Avatar của server {interaction.guild.name}', description='', color = discord.Color.from_rgb(0,201,87))
    avaembed.set_image(url=f'{interaction.guild.icon}')
    avaembed.set_footer(text=f'Bởi: {interaction.user}!')
    await interaction.response.send_message(embed = avaembed, ephemeral = False)

#
@tree.command(name = "binance", description = "Kiểm tra giá trị các đồng tiền ảo")
async def binance(interaction: discord.Interaction, coin_name: str):

    if coin_name == "Bitcoin (BTC)":
        coin_position = 0
    if coin_name == "Ethereum (ETH)":
        coin_position = 1
    if  coin_name == "Doge Coin (DOGE)":
        coin_position = 9
    if coin_name == "Shiba Inu (SHIB)":
        coin_position = 11
    if coin_name == "Ethereum Classic (ETC)":
        coin_position = 19
    
    coin_api = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
    tach_json_coin = coin_api.json()
    coin_data = tach_json_coin[coin_position] 
    coin_price = coin_data["current_price"]

    await interaction.response.send_message(f'Tỉ giá đồng **{coin_name}** hiện tại là: **{coin_price} USD/1 {coin_name}**', ephemeral = False)
  
@binance.autocomplete('coin_name')
async def binance_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    coin_name = ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Doge Coin (DOGE)', 'Shiba Inu (SHIB)', 'Ethereum Classic (ETC)']
    return [
        app_commands.Choice(name=binan, value=binan)
        for binan in coin_name if current.lower() in binan.lower()
    ]



#
@tree.command(name = "hành-động", description = "...")
async def action_module(interaction: discord.Interaction, hanh_dong: str, tin_nhan: str):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://api.waifu.pics/sfw/{hanh_dong}") as r:
            action = await r.json()
            actionembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
            actionembed.set_image(url=action["url"])
            actionembed.set_footer(text=f"{tin_nhan} ...❤️")
            await interaction.response.send_message(embed = actionembed, ephemeral = False)

@action_module.autocomplete('hanh_dong')
async def action_module_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    hanh_dong = ['kiss', 'hug', 'cry', 'smile', 'highfive', 'kill', 'pat', 'smug', 'bonk', 'lick', 'awoo', 'blush', 'wave', 'slap']
    return [
        app_commands.Choice(name=act, value=act)
        for act in hanh_dong if current.lower() in act.lower()
    ]

@tree.command(name = "văn-mẫu", description = "Tạo ra những bài văn mẫu có giá trị theo thời gian")
async def action_module(interaction: discord.Interaction):
    peabot_rep = [
        'Bắn CSGO cũng giống như đi từ thiện vậy, cái tâm phải đặt lên đầu',
        'Đặt câu hỏi là tốt nhưng cái gì cũng hỏi thì không',
        'Sau này, chỉ có làm thì mới có ăn. Những cái loại không làm mà đòi có ăn thì chỉ có ăn ||đầu buồi|| ăn ||cứt||',
        'Những cái loại ngủ quá giờ trưa thì không giàu được đâu',
        'Nam tử hán đại trượng phu, đánh nhau không lại ||bú cu|| giảng hòa',
        'Tôi có thằng em sinh năm 96 học Bách Khoa Cơ Khí tay ngang sang học IT...',
        'Hảo hánnnn',    
        'Bao lâu thì bán được 1 tỉ gói mè? Trả lời?',
        'Học đếm: 1 - Ngô Diệc Phàm - 3 - 4 - 5 - 6 - 7...',
        'Bạn không có một chút văn hoá nào, bạn không có một chút đạo đức nào. Tại sao bạn lại dùng lệnh này?? Bạn không đủ tư cách để nói chuyện với tôi',
        'Xin là xin vĩnh biệt cụ',
        'Thế bạn nói xem vì sao mình phải trả lời bạn - Peanutss Chen',
        'Chào em, chị là luật sư của army và đã thu thập đủ bằng chứng em xúc phạm army của công ty bên chị. Em vui lòng xóa bài này sau 30 phút. Nếu sau 30 phút mà em vẫn chưa xóa bài thì bên chị sẽ dùng tới pháp luật và em sẽ bị lôi đầu ra Côn Đảo !'
        'CÁC BẠN NHÂN VIÊN ƠI, CÁC BẠN HỖ TRỢ MÌNH VỚI. CÁC BẠN ƠI CÁC BẠN ĐƯA NHẦM ĐỒ CHO MÌNH CÁC BẠN ƠI. CÁC BẠN NHÂN VIÊN HỖ TRỢ ƠI. CÁC BẠN HỖ TRỢ MÌNH KHÔNG CÁC BẠN ƠI. CÁC BẠN ĐIẾC À CÁC BẠN ƠI HỖ TRỢ MÌNH KHÔNG CÁC BẠN ƠI.'
        'Trong trường hợp anh bị say đắm bởi vẻ đẹp quyến rũ của em (hoặc những vẻ đẹp tương tự của em), anh khẳng định anh không liên hệ bởi bất cứ một cô gái khác nào trong nhóm này, có lẽ trái tim của anh chỉ dành cho em. Anh cũng xin khẳng định anh không hề có thể yêu một cô gái nào khác khi đã yêu em..',
        'Nhóm này đã bị điều tra bởi các cơ quan trực thuộc Bộ Công an (và/hoặc các tổ chức chính trị tương tự phục vụ cho nhà nước CHXHCNVN). Cơ quan điều tra (CQĐT) khẳng định các thành viên trong này liên quan tới nhóm hoặc những cá nhân khác trong đây. CQĐT biết rõ tại sao các thành viên lại có mặt ở đây vào thời điểm này, tài khoản của họ không được thêm bởi một bên thứ ba mà chính họ tự tham gia vào đây. Các nhân viên của CQĐT cũng xin khẳng định rằng những hành động chống phá Đảng và Nhà nước đã được thực hiện bởi các thành viên trong nhóm này. Nhà nước CHXHCNVN cũng không quên khẳng định quyết tâm chiến thắng đại dịch Covid-19, nhấn mạnh chủ quyền không thể tranh cãi với quần đảo Hoàng Sa và Trường Sa, cũng như tính chính nghĩa của cuộc chiến giải phóng người dân Campuchia khỏi thảm họa diệt chủng Khmer Đỏ.',
        'Ôi bạn ơi! Bạn sức đề kháng kém là do bạn không chơi đồ đấy bạn ạ, nếu bạn chơi đồ vào thì là đề kháng nó khỏe nó không bao giờ bị ốm đâu bạn ạ, chơi đồ là thuốc bổ mà bạn! Bạn phải nên nhớ nhá, cái viên thuốc bình thường, cái viết thuốc ACID B1 bạn mua có 2 nghìn đc mấy viên đúng k ? Hoặc là 10 nghìn 1 viên, 10 nghìn 1 viên là ACID B1 đấy , đúng không? Thế đây những viên thuốc như viên thuốc kẹo, viên thuốc kim cương, viên thuốc vương liệm này, viên thuốc các kiểu lày thì bạn mua cái đấy vào 500 nghìn 1 viên cơ mà! Chơi cái đấy vào đề kháng nó phải cao hơn chứ bạn! Chơi cái đấy vào nhiều đề kháng mà! Bạn không chơi vào đề kháng bạn kém là phải đấy bạn ạ !',
        'Theo mình thì không nên đăng những bài như thế này. Cái xấu xa, mình phải quên nó đi, cho nó mất dần. K nên nhắc lại. Ng tốt sẽ bị ám ảnh, k tốt cho tinh thần, ng xấu sẽ ghi nhận. Ng k hiểu biết sẽ ghi nhớ. Và nếu nhóm còn đăng nhiều bài như t… thế này thì mình sẽ rời nhóm. Cuộc sống rất ngắn ngủi, tại sao phải để tâm đến điều cần quên đi. Hãy sống tích cực và tươi sáng.'
    ]
    response = random.choice(peabot_rep)
    await interaction.response.send_message(response)




#@tree.command(name="kick", description = "Kick một member nào đó",)
##@commands.has_permissions(kick_members = True, administrator = True)
#async def kick(interaction: discord.Interaction, user : discord.Member, li_do: str):#
   # if user.id == interaction.user.id:
   #     print("1 chạy")
   #     await interaction.response.send_message("Bạn không thể tự kick chính mình!!")
   # elif user.guild_permissions.administrator:
   #     print("2 chạy")
   #     await interaction.response.send_message("Ơ kìa anh bạn, bạn không thể kick được Admin đâu :))", ephemeral = False)
   # elif isinstance(interaction, MissingPermissions):
   #     print("3 chạy")
   #     await interaction.response.send_message("Bạn cần có quyền **Kick Member** và **Admin**!!", ephemeral = False)
   # elif commands.has_permissions(kick_members = True, administrator = True): 
   #     print("4 chạy")
   #     await interaction.response.send_message(f"**{user}** đã bị kick khỏi server! \nLí do: **{li_do}**", ephemeral = False)
   #     await user.kick(reason=li_do)
   # else:
   #     print("5 chạy")
   #     await interaction.response.send_message("Bot không được cấp quyền Kick Member - Admin, vui lòng điều chỉnh quyền hạn của bot trong cài đặt server", ephemeral = False)
       

#@tree.command(name="test", description = "...",)
#async def self(interaction: discord.Interaction):
#    if commands.has_permissions(mod = True) == True:#
  #      await interaction.response.send_message("có")
    # else:
     #   await interaction.response.send_message("không")

#@kick.error
#async def kick_error(interaction ,error):
#   if isinstance(error, MissingPermissions):
#       await interaction.response.send_message("Bạn cần có quyền **Kick Member** và **Admin**!!")
#   else:
#       await interaction.response.send_message("Đã có lỗi!")
#      raise error


#run
client.run(TOKEN) 
      
