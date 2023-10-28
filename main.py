import discord
from discord.ext import commands
import os
import random, requests 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$",intents=intents)


@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def mem_random(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def animal(ctx):
    img_name = random.choice(os.listdir('imageForan'))
    with open(f'imageForan/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)                        #ДЗ! (45-50)
    
@bot.command('dog')
async def dog(ctx):
    '''По команде dog вызывает функцию get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

    
bot.run("TOKEN")
