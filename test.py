# bot.py
import os
import random
from typing import Any, Text
import discord
from discord import channel
from discord import message
from discord import embeds
from discord import user
from discord import member
from dotenv import load_dotenv
from datetime import datetime
from dotenv.main import with_warn_for_invalid_lines
import requests
from discord.utils import get
from discord.ext import commands
import aiohttp
from discord_together import DiscordTogether



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


#connecting
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#set status 
    activity = discord.Game(name='?help để nhận hỗ trợ', type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)


#wellcome 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send('Chào bạn, rất vui khi bạn vào server của chúng tớ!')


#prefix 1
@client.event
async def on_message(message):
#help prefix    
    if message.content == '?help':
        myembed = discord.Embed (title = 'Peanutss Bot (v1.8)', description = 'Sử dụng `?[lệnh]` để tương tác với bot', color = discord.Color.gold())
        myembed.set_author (name = "Danh Sách Lệnh")
        myembed.add_field (name = "💬 Tương Tác - (10)", value = "`somayman` `hello` `banlaai` `info` `botngu` `botkhon` `time` `coronavn` `corona` `bonk` `bitcoin`", inline=False)
        myembed.add_field (name = "😊 Fun - (11)", value = "`fbi` `daoli` `ongda` `haylam` `hug` `smile` `kill` `cry` `kiss` `highfive` `gianghoa`", inline=False)
        myembed.add_field (name = "🎁 Media - (7)", value = "`meme` `darkmeme` `girl` `cat` `dog` `food` `waifu` ", inline=False)
        myembed.add_field (name = "📺 Giải trí - (8)", value = "`join, connect` `leave, disconnect` `play` `youtube` `chess` `poker` `fishing` `betrayal`", inline=False)
        myembed.add_field (name = "🔞 NSFW - (1)", value = "`hentai`", inline=False)
        myembed.add_field (name = "⚙️ Guilds - (5)", value = "`ping` `help` `status` `avatarsv` `botserver`", inline=False)
        myembed.add_field (name = "☎️ Contact - (3):", value = "`contact` `donate` `invite`", inline=False)
        myembed.set_footer(text=f"Bot sẽ được update liên tục. Cảm ơn mọi người đã ủng hộ ^^")
        
        updated = f"```- Các chức năng mới được Update (BigUpdate): bitcoin, status, avatarsv, chess, fishing, poker, betrayal, gianghoa \n- Lệnh cat đã fix và hoạt động lại bình thường!!```"
        
        await message.channel.send(embed = myembed)
        await message.channel.send(updated)
        
    if message.author == client.user: 
        return

#prefix 2
    peabot_rep = [
        'Tôi năm nay hơn 70 tuổi rồi mà tôi chưa bao giờ gặp cái trường hợp nào mà nó như thế này cả, mà tôi cũng phải phục cái anh này chứ phải tôi tôi đấm cho nó mấy nhát rồi. Anh không thể cứ xin lỗi chị chỉ tay vào mặt và chửi đm chúng mày, thằng ranh con này!!',
        (
            'Ông Đa là ông nào? :>'
        ),
    ]

    if message.content == '?ongda':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 3
    peabot_rep = [
        'Tớ là Peanuts Bot :D, rất vui được gặp bạn ^^',
        (
            'Tôi là tất cả, và không là thứ gì :c'
        ),
    ]

    if message.content == '?banlaai':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 4
    peabot_rep = [
        'Xin chào bạn nhé 🥰 ',
        (
            'Lô con kẹc XD 😈'
        ),
    ]

    if message.content == '?hello':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 5
    peabot_rep = [
        'Chào bạn tớ là Peanuts Bot, được tạo ra bởi Peanutss (hay còn gọi là Andy) . Chúc bạn có trải nghiệm vui vẻ với tớ XD',
        (
            'Chào bạn tớ là Peanuts Bot, được tạo ra bởi Peanutss (hay còn gọi là Andy) . Chúc bạn có trải nghiệm vui vẻ với tớ XD'
        ),
    ]

    if message.content == '?info':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 6
    peabot_rep = [
            'Knock knock FBI đây, yêu cầu bro tắt ngay loli và giơ tay bước chậm về phía chúng tôi',
            (
                'FBI Open The Door... boom ... bạn đã bị bắt vì qwerty bằng loli'
            ),
        ]

    if message.content == '?fbi':
        response = random.choice(peabot_rep)
        await message.channel.send(response)
        await message.channel.send('https://cdn.discordapp.com/emojis/856910717914841108.png?v=1')

#prefix 7
    peabot_rep = [
            'Bee gay - Bee gei - Bee gay - Bee gei - Bee gay - Bee gei - Bee gay - Bee gei - Bee gay - Bee gei',
            (
                'Bee rất gay, Bee thèm Duk Dik'
            ),
        ]

    if message.content == '?beegei':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 8 
    peabot_rep = [
            'Bot không ngu, bạn mới là người ngu :((',
            (
                'Tao tức á :"('
            ),
        ]

    if message.content == '?botngu':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 9
    lknum = random.randint(1,99)
    peabot_rep = 'Con số may mắn hôm nay của bạn là: ' + str(lknum) + ' 🥳' 

    if message.content == '?somayman':
        await message.channel.send(peabot_rep)
        await message.channel.send('Nhớ cầm lấy nó đi đánh đề nhé XD ^^')

#prefix 10
    #peabot_rep = 'Cười gì cười lắm thế bạn =))'
    #if message.content == '=)))' or message.content == '=))' or message.content == ':)))' or message.content == ':))' or message.content == '=))))' or message.content == '=)))))' or message.content == ':))))' or message.content == ':)))))':
        #await message.channel.send(peabot_rep)

#prefix 11 
    peabot_rep = 'Đừng buồn nữa, vui lên. Không tôi xiên bạn đó...'
    if message.content == ':(' or message.content == ':((' or message.content == ':(((' or message.content == '=(' or message.content == '=((' or message.content == '=(((':
        await message.channel.send(peabot_rep)

#prefix 12
    if message.content == '?time':

        now = datetime.now()
        peabot_rep = now.strftime('%I Hours %M Minutes %S Seconds') #lib time


        response = 'Bây giờ là: ' + str(peabot_rep)
        await message.channel.send(response)   

#prefix 13 tạm thời disable 
    #if 'bee' in message.content:
        #response = 'Bạn vừa nhắc đến Bee? Có phải là bạn đó rất thèm đuk đik không?'
        #await message.channel.send(response)

#prefix 14
    if message.content == '?haylam':
        response = 'Hay lắm ||đ!t mọe mài||' 
        await message.channel.send(response)

#prefix 15
    if 'bye' in message.content or 'bai' in message.content or 'Bye' in message.content or 'Bai' in message.content:
        response = 'Bye bye bạn nhé ^^'
        await message.channel.send(response)
        
#prefix 16
    if message.content == '?contact':
        contactembed = discord.Embed (color = discord.Color.dark_grey())
        contactembed.set_author (name = "Liên hệ với Dev tại:")
        contactembed.add_field (name = "Discord Account ^^:", value = 'Peanuts Is Me (Andy)#1703', inline=False)
        contactembed.add_field (name = "Link Facebook ^^:", value = 'https://facebook.com/yt.andymusic', inline=False)
        contactembed.add_field (name = "Link Youtube ^^:", value = 'https://youtube.com/c/andymusicc', inline=False)
        contactembed.add_field (name = "Support Discord Server:", value = 'https://discord.gg/5t85FB4Dsc', inline=False)
        contactembed.add_field (name = "Github:", value = 'https://github.com/anphongdoa5', inline=False)
        await message.channel.send(embed = contactembed)

#prefix 17
    if message.content == '?bonk':
        response = 'https://media.discordapp.net/attachments/737129296816242759/854679699963379712/bonk.png?width=177&height=159'
        await message.channel.send(response)

#prefix 18
    if message.content == '?ping':
        await message.channel.send(f'Pong! Độ trễ của tớ là {round(client.latency * 1000)}ms')

#prefix 19
    if '?play' in message.content:
        peabot_rep = 'Xin lỗi chứ tao chưa biết bật nhạc...'
        response = peabot_rep
        await message.channel.send(response)

#prefix 20
    peabot_rep = [ 
        'Đúng rồi đúng rồi, bot thông minh mà :3',
    (
        'Quá khen, quá khen uwu'
    ),
    ]

    if message.content == '?botkhon':
        response = random.choice(peabot_rep)
        await message.channel.send(response)

#prefix 21
    #peabot_rep = [ 
    #    'Pháp bị loại rồi nhé, còn Đức thì đợi tối nay xem như nào :))',
    #(
    #    'Đức vô địch không nói nhiều'
    #),
    #]

    #if message.content == '?doinaovodich':
        #response = random.choice(peabot_rep)
        #await message.channel.send(response)

#prefix 22
    if message.content == '?meme':
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                memes = await r.json()
                embed = discord.Embed(color = discord.Color.green())
                embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.set_footer(text=f"Meme của mọi nhà")
                await message.channel.send(embed = embed)

#prefix 23
    if message.content == '?darkmeme':
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/dankmemes/new.json?sort=hot") as r:
                darkmemes = await r.json()
                darkembed = discord.Embed(color = discord.Color.red())
                darkembed.set_image(url=darkmemes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                darkembed.set_footer(text=f"Đảk Mêm")
                await message.channel.send(embed = darkembed)

#prefix 24
    if message.content == '?cat':
        async with aiohttp.ClientSession() as cs:
            #api đuồi bầu gắn url trong 1 list, phải tách bằng 1 int chứ không thể tách như thường
            async with cs.get("https://api.thecatapi.com/v1/images/search") as r:
                cats = await r.json()

                catch = cats[0] #trả về dãy như api thường (mất [])
                catlink = catch['url'] #tách data như thường

                catembed = discord.Embed(color = discord.Color.blue())
                catembed.set_image(url=catlink)
                catembed.set_footer(text=f"Mèo méo meo mèo meo")
                await message.channel.send(embed = catembed)


#prefix 25
    if message.content == '?dog':
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                dogs = await r.json()
                dogsembed = discord.Embed(color = discord.Color.gold())
                dogsembed.set_image(url=dogs["message"])
                dogsembed.set_footer(text=f"Cute Dogs :3")
                await message.channel.send(embed = dogsembed)      

#prefix 26
    if message.content == '?food':
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/food/new.json?sort=hot") as r:
                foods = await r.json()
                foodsembed = discord.Embed(color = discord.Color.green())
                foodsembed.set_image(url=foods["data"]["children"][random.randint(0, 25)]["data"]["url"])
                foodsembed.set_footer(text=f'Mlem mlem')
                await message.channel.send(embed = foodsembed)
#prefix 27
    if message.content == '?waifu':
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/waifu") as r:
                waifu = await r.json()
                waifuembed = discord.Embed(color = discord.Color.dark_orange())
                waifuembed.set_image(url=waifu["url"])
                waifuembed.set_footer(text=f"Who is your waifu? ❤️")
                await message.channel.send(embed = waifuembed)

#prefix 28
    if message.content == '?hentai':
        if message.channel.is_nsfw():
            list = ['waifu', 'neko', 'blowjob']
            choice = random.choice(list)
            link = "https://api.waifu.pics/nsfw/"
            fullurl = link + choice 
            async with aiohttp.ClientSession() as cs:
                async with cs.get(fullurl) as r:
                    nsfw = await r.json()
                    nsfwembed = discord.Embed(color = discord.Color.dark_red())
                    nsfwembed.set_image(url=nsfw["url"])
                    nsfwembed.set_footer(text=f"⚠️| Not Safe For Work!!")
                    await message.channel.send(embed = nsfwembed)
        else:
            await message.channel.send("❗| Lệnh chỉ dùng được trong phòng NSFW !!")        


        
#prefix 29
    lines = open('list_girl.txt').read().splitlines()
    link = random.choice(lines)

    if message.content == '?girl':
        girlembed = discord.Embed(color = discord.Color.from_rgb(255,105,180))
        girlembed.set_image(url=link)
        girlembed.set_footer(text=f"Mỗi bức ảnh, một niềm vui ❤️")
        await message.channel.send(embed = girlembed)

#prefix 30
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
        'Thế bạn nói xem vì sao mình phải trả lời bạn - Peanutss Chen'
    ]
    response = random.choice(peabot_rep)
    if message.content == '?daoli':
        await message.channel.send(response)

#prefix 31
    if message.content == '?donate':    
        donateembed = discord.Embed (title = 'Playerduo Link:', color = discord.Color.orange())
        donateembed.set_author (name = "Donate ủng hộ Dev ly cà phê tại đây:")
        donateembed.add_field (name = "https://playerduo.com/peanutss", value = "Cảm ơn bạn rất nhiều <3", inline=False)
        await message.channel.send(embed = donateembed)

#prefix 32
    togetherControl = DiscordTogether(client)
    if message.content == '?youtube':
        if (message.author.voice):   #kiểm tra người trong voice 
            voice = message.author.voice.channel

            #tạo url youtube together
            link = await togetherControl.create_link(message.author.voice.channel.id, 'youtube')
            await message.channel.send(f'Nhấn vào link để xem Youtube: {link} ')
            await message.channel.send('Lưu Ý: Chức năng chỉ hoạt động trên các thiết bị PC - Laptop, không hỗ trợ cho các thiết bị điện thoại!!')
            
        else:
            await message.channel.send('❌| Bạn phải vào kênh voice trước!!')

#prefix 33
    if message.content == '?coronavn':
        response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/vietnam')
        data = response.json()
        cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        peabot_rep = f"TÌNH HÌNH COVID 19 TẠI VIỆT NAM:\n☣  Số Người Nhiễm: {cases} người\n💀  Số Người Tử Vong: {deaths} người\n✅  Số Người Bình Phục: {recovered} người"
        await message.channel.send(peabot_rep)
        
        
#prefix 34
    if message.content == '?corona':
        response = requests.get('http://coronavirus-19-api.herokuapp.com/countries/world')
        data = response.json()

        cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        peabot_rep = f"TÌNH HÌNH COVID 19 TRÊN THẾ GIỚI:\n☣  Số Người Nhiễm: {cases} người\n💀  Số Người Tử Vong: {deaths} người\n✅  Số Người Bình Phục: {recovered} người"
        await message.channel.send(peabot_rep)
        
        
#prefix 35
    if message.content == '?invite':
        inviteembed = discord.Embed (color = discord.Color.green())
        inviteembed.set_author (name = "Link Invite Peanutss Bot")
        inviteembed.add_field (name = "Link:", value = 'https://discord.com/oauth2/authorize?client_id=728462830407254088&permissions=34631477334&scope=bot', inline=False)
        await message.channel.send(embed = inviteembed)
        
#prefix 36 (chùm lệnh tương tác) 6 lệnh
    if '?hug' in message.content:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/hug") as r:
                hug = await r.json()
                hugembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
                hugembed.set_image(url=hug["url"])
                hugembed.set_footer(text=f"Ôm ... ❤️")
                await message.channel.send(embed = hugembed)

    if '?cry' in message.content:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/cry") as r:
                cry = await r.json()
                cryembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
                cryembed.set_image(url=cry["url"])
                cryembed.set_footer(text=f"Cry :((")
                await message.channel.send(embed = cryembed)

    if '?kiss' in message.content:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/kiss") as r:
                kiss = await r.json()
                kissembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
                kissembed.set_image(url=kiss["url"])
                kissembed.set_footer(text=f".... ❤️")
                await message.channel.send(embed = kissembed)

    if '?smile' in message.content:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/smile") as r:
                smile = await r.json()
                smileembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
                smileembed.set_image(url=smile["url"])
                await message.channel.send(embed = smileembed)

    if '?highfive' in message.content:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/highfive") as r:
                highfive = await r.json()
                hfembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
                hfembed.set_image(url=highfive["url"])
                hfembed.set_footer(text=f"Highfive :D")
                await message.channel.send(embed = hfembed)

    if '?kill' in message.content:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/kill") as r:
                kill = await r.json()
                killembed = discord.Embed(color = discord.Color.from_rgb(127,255,212))
                killembed.set_image(url=kill["url"])
                killembed.set_footer(text=f"Cho mày chết ....")
                await message.channel.send(embed = killembed)
                
#prefix 37
    if message.content == '?status':
        statembed = discord.Embed(title=f'Thông tin server {message.guild.name} ',description= '', color = discord.Color.from_rgb(147,112,219))
        statembed.set_thumbnail(url=f'{message.guild.icon_url}')

        statembed.add_field(name='Tên Server:', value=f'{message.guild.name}', inline=True)
        statembed.add_field(name='Số Lượng Thành Viên:', value=f'{message.guild.member_count} thành viên', inline=True)
        statembed.add_field(name='Vị Trí Server:', value=f'{message.guild.region}', inline=True)
        statembed.add_field(name='Server Tạo Lúc:', value=f'{message.guild.created_at.strftime("%#d %B %Y, %H:%M")}')

        statembed.add_field(name='Trạng Thái Bot:', value='🟢 Online!!', inline = True)
        statembed.add_field(name='Latency:', value=f'Độ trễ bot: {round(client.latency * 1000)}ms', inline=True)
        statembed.set_footer(text=f'Bởi: {message.author}!', icon_url = f'{message.author.avatar_url}')

        await message.channel.send(embed = statembed)


#prefix 38
    if message.content == '?avatarsv':
        avaembed = discord.Embed(title=f'Avatar của server {message.guild.name}', description='', color = discord.Color.from_rgb(0,201,87))
        avaembed.set_image(url=f'{message.guild.icon_url}')
        avaembed.set_footer(text=f'Bởi: {message.author}!', icon_url = f'{message.author.avatar_url}')
        await message.channel.send(embed = avaembed)
    togetherControl = DiscordTogether(client)

#prefix 39
    if message.content == '?chess':
        if (message.author.voice):   #kiểm tra người trong voice 
            voice = message.author.voice.channel

            #tạo url youtube together
            link = await togetherControl.create_link(message.author.voice.channel.id, 'chess')
            await message.channel.send(f'Nhấn vào link để chơi: {link} ')
            await message.channel.send('Lưu Ý: Chức năng chỉ hoạt động trên các thiết bị PC - Laptop, không hỗ trợ cho các thiết bị điện thoại!!')

        else:
            await message.channel.send('❌| Bạn phải vào kênh voice trước!!')
         
#prefix 40
    if message.content == '?fishing':
        if (message.author.voice):   #kiểm tra người trong voice 
            voice = message.author.voice.channel

            #tạo url youtube together
            link = await togetherControl.create_link(message.author.voice.channel.id, 'fishing')
            await message.channel.send(f'Nhấn vào link để chơi: {link} ')
            await message.channel.send('Lưu Ý: Chức năng chỉ hoạt động trên các thiết bị PC - Laptop, không hỗ trợ cho các thiết bị điện thoại!!')

        else:
            await message.channel.send('❌| Bạn phải vào kênh voice trước!!')
            
#prefix 41
    if message.content == '?poker':
        if (message.author.voice):   #kiểm tra người trong voice 
            voice = message.author.voice.channel

            #tạo url youtube together
            link = await togetherControl.create_link(message.author.voice.channel.id, 'poker')
            await message.channel.send(f'Nhấn vào link để chơi: {link} ')
            await message.channel.send('Lưu Ý: Chức năng chỉ hoạt động trên các thiết bị PC - Laptop, không hỗ trợ cho các thiết bị điện thoại!!')

        else:
            await message.channel.send('❌| Bạn phải vào kênh voice trước!!')
            
            
            
#prefix 41
    if message.content == '?betrayal':
        if (message.author.voice):   #kiểm tra người trong voice 
            voice = message.author.voice.channel

            #tạo url youtube together
            link = await togetherControl.create_link(message.author.voice.channel.id, 'betrayal')
            await message.channel.send(f'Nhấn vào link để chơi: {link} ')
            await message.channel.send('Lưu Ý: Chức năng chỉ hoạt động trên các thiết bị PC - Laptop, không hỗ trợ cho các thiết bị điện thoại!!')

        else:
            await message.channel.send('❌| Bạn phải vào kênh voice trước!!')
            
#prefix 41
    if message.content == '?botserver':
      await message.channel.send(f'Bot đang ở {str(len(client.guilds))} server!!')

#prefix 42
    if message.content == '?allserver':
        activeservers = client.guilds
        for guild in activeservers:
            await message.channel.send(guild.name)
            
    
#voice activitive modules 
#join voice channel
    if message.content == '?connect' or message.content == '?join':   #prefix
        if (message.author.voice):   #kiểm tra người trong voice 
            voice = message.author.voice.channel
            await message.channel.send("Đang kết nối...")
            await voice.connect()
        else:
            await message.channel.send('❌| Bạn phải ở trong kênh voice thì mình mới vào được chứ ^^')

#disconnect voice channel
    if message.content == '?disconnect' or message.content == '?leave':   #prefix
        if (message.author.voice):   #kiểm tra có người trong voice không
            await message.channel.send('Đang ngắt kết nối...')
            await message.guild.voice_client.disconnect() 
        else:
            await message.channel.send('❌| Bạn phải ở trong kênh voice thì mình mới ra được chứ ^^')
            
 #dành cho thằng hotboykeokoe
    if message.content == '?hotboykeokoe':
        keoembed = discord.Embed(title = 'Ai là thằng thiểu năng nào?',color = discord.Color.red())
        keoembed.set_image(url='https://media.discordapp.net/attachments/892723707649339412/900044839217930300/Miles_Selfie.png?width=125&height=144')
        await message.channel.send(embed = keoembed)
        
 #prefix 43
    if message.content == '?gianghoa':
        await message.channel.send('https://images-ext-2.discordapp.net/external/Nv-nYhl8A0vhAqtktbwujG61vGqL1Lz1nuO2NA7rN5w/https/media.discordapp.net/attachments/781481778795118612/895984488906100736/gianghoa.gif?width=351&height=45')

#prefix 44
    if message.content == '?bitcoin':
        api = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = api.json()
        price = data["bpi"]["USD"]["rate"]
     
        await message.channel.send('Tỉ giá Bitcoin hiện tại là: ' + str(price) + ' USD/1 BTC')

#run
client.run(TOKEN)
      
