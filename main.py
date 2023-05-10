import time
import json
import discord
from sys import stderr 
from json import dumps 
from colorama import Fore, Style
import subprocess
import requests
import time
from os import system
from discord import Webhook, RequestsWebhookAdapter, Embed

import requests
from threading import Thread
from os import system
from time import sleep

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import pyfiglet
import time,os,sys
import random
import threading

from time import sleep
from colorama import Fore
from pystyle import Colors, Colorate

import time
import subprocess
import os
from os import system
import sys
from hashlib import sha256
import hashlib

import sys,time,random

from datetime import datetime


format_one = 0
format_two = 0
format_tre = 0

loop_types = 1

def receive_color():
    global format_one, format_two, format_tre, loop_types

    for types1, types2, types3, number in zip([1, 0], [0, 1], ['+', '-'], [255, 0]):
        if (loop_types == types1):
            if (format_one != number):
                exec(f'format_one {types3}= 15', globals())

            if (format_one == number):
                if (format_two != number):
                    exec(f'format_two {types3}= 15', globals())

            if (format_two == number):
                if (format_tre != number):
                    exec(f'format_tre {types3}= 15', globals())

            if (format_tre == number):
                loop_types = types2

    return f"\033[38;2;{format_one};{format_two};{format_tre}m"


os.system(f'cls & mode 95,15 & title DisconnectZc#2000')

def now():
    now = datetime.now()
    nownow = now.strftime("%H:%M:%S")
    return nownow

h = open('message.txt','r',encoding='utf-8')
mes = h.read()

banner = r"""           
Discord : https://discord.gg/gFNB9PAU2V
               
    """[1:] 
Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, enter=True)

def rb(text):
    return (Colors.blue_to_purple,text)







with open('config.json') as f:
    config = json.load(f)
    TOKEN = config.get('token')
    chaid1 = config.get('channel_id1')
    chaid2 = config.get('channel_id2')
    chaid3 = config.get('channel_id3')
    chaid4 = config.get('channel_id4')
    chaid5 = config.get('channel_id5')
    chaid6 = config.get('channel_id6')
    chaid7 = config.get('channel_id7')
    chaid8 = config.get('channel_id8')
    chaid9 = config.get('channel_id9')
    chaid10 = config.get('channel_id10')
    chaid11 = config.get('channel_id11')
    chaid12 = config.get('channel_id12')
    chaid13 = config.get('channel_id13')
    chaid14 = config.get('channel_id14')
    chaid15 = config.get('channel_id15')
    chaid16 = config.get('channel_id16')
    chaid17 = config.get('channel_id17')
    chaid18 = config.get('channel_id18')
    chaid19 = config.get('channel_id19')
    chaid20 = config.get('channel_id20')

def genocide():
    print(Colorate.Horizontal(Colors.rainbow, '''
AUTOPROMOTE
'''))    
system('cls')                      
genocide()
print(Colorate.Horizontal(Colors.rainbow, '''
\t\t\t'''))    
Style.RESET_ALL
class MyClient(discord.Client):
        async def on_ready(self):
            genocide()
                  
        async def on_message(self,ctx):
            if ctx.channel.id == int(chaid1) or ctx.channel.id == int(chaid2) or ctx.channel.id == int(chaid3) or ctx.channel.id == int(chaid4) or ctx.channel.id == int(chaid5) or ctx.channel.id == int(chaid6) or ctx.channel.id == int(chaid7) or ctx.channel.id == int(chaid8) or ctx.channel.id == int(chaid9) or ctx.channel.id == int(chaid10) or ctx.channel.id == int(chaid11) or ctx.channel.id == int(chaid12) or ctx.channel.id == int(chaid13) or ctx.channel.id == int(chaid14) or ctx.channel.id == int(chaid15) or ctx.channel.id == int(chaid16) or ctx.channel.id == int(chaid17) or ctx.channel.id == int(chaid18) or ctx.channel.id == int(chaid19) or ctx.channel.id == int(chaid20):
                if ctx.content == "":
                    system("title " + f"Username : {self.user} │ Channel : {ctx.channel.name}")
    
                    await ctx.channel.send(mes)
                    print(receive_color() + f'[{now()}] [SEND CHANNEL] {ctx.channel.name}')    
client = MyClient()
client.run(TOKEN,bot = False)


    