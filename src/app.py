import discord
import os
from discord import colour
import pandas as pd
import json
import sys
import youtube_dl

sys.dont_write_bytecode = True

class MyClient(discord.Client):
    with open('C:\\Users\\PC\\Desktop\\Gabriel\\syBot\\src\\urls.json', 'r', encoding='utf8') as f:
        global urls
        urls = json.load(f)
    # LOGIN
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # DEV
        developer = "('gabs')"
        global num, valorant, lol, wr, cs
        num = 10
        c = 0
        valorant = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']
        lol = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']
        wr = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']
        cs = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']

        

        if message.content == '!syBOT' or message.content == '!about' or message.content == '!sobre':
            await message.author.send(f'Olá {message.author.name}, eu sou o syBOT! Fui desenvolvido pelo {developer} com o objetivo de auxiliar nos servidores do discord.Eu ainda estou em desenvolvimento (BETA) mas posso ajudar bastante, para vizualizar os comandos, vá ao canal e digite ?comandos ou ?commands {os.linesep} Atenciosamente, syBOT <3 !')

        # COMANDOS 
        elif message.content == '!comandos' or message.content == '!commands':
            await message.channel.send(f'Vou te mostrar todos os meus comandos. Eles estão disponíveis em português/inglês! {os.linesep} 1. Para mostrar os comandos, digite !comandos ou !commands {os.linesep} 2. Para mostrar a descrição do bot, digite !syBOT ou !about/!sobre {os.linesep} 3. Para ativar prontidão à partida de Valorant, digite !valorant {os.linesep} 4. Para ativar prontidão à partida de League of Legends, digite !lol {os.linesep} 5. Para ativar prontidão à partida de LOL - WildRift, digite !wr {os.linesep} 6. Para ativar prontidão à partida de CS:GO, digite !cs {os.linesep} 7. Mostrar o desenvolvedor, digite !dev')
        # DEV
        elif message.content.lower() == '!dev':
            await message.channel.send(f'Powered by Gabriel Carvalho {os.linesep} Github: https://github.com/GabPhoenix {os.linesep} Instagram: https://www.instagram.com/iamgabc/')

        # TYPE PYTHON
        elif message.content.lower() == 'python':
            for key, value in urls.items():
                if key == 'python':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do python é o : {link}')
        # TYPE JAVA
        elif message.content.lower() == 'java':
            for key, value in urls.items():
                if key == 'java':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do java é o : {link}')
        # TYPE JAVASCRIPT
        elif message.content.lower() == 'javascript' or message.content.lower() == 'js':
            for key, value in urls.items():
                if key == 'javascript':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do javascript é o : {link}')
        # TYPE C++
        elif message.content.lower() == 'c++':
            for key, value in urls.items():
                if key == 'c++':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do C++ é o : {link}')
        # TYPE C
        elif message.content.lower() == 'c':
            for key, value in urls.items():
                if key == 'c':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? confira um site sobre C: {link}')
        # TYPE Php
        elif message.content.lower() == 'php':
            for key, value in urls.items():
                if key == 'php':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do php é o : {link}')
        # TYPE Dart
        elif message.content.lower() == 'dart':
            for key, value in urls.items():
                if key == 'dart':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Dart é o : {link}')
        # TYPE Swift
        elif message.content.lower() == 'swift':
            for key, value in urls.items():
                if key == 'swift':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Swift é o : {link}')
        # TYPE KOTLIN
        elif message.content.lower() == 'kotlin':
            for key, value in urls.items():
                if key == 'kotlin':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do kotlin é o : {link}')
        # TYPE REACT 
        elif message.content.lower() == 'react':
            for key, value in urls.items():
                if key == 'react':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do React é o : {link}')
        # TYPE Django
        elif message.content.lower() == 'django':
            for key, value in urls.items():
                if key == 'django':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Django é o : {link}')
        # TYPE React Native
        elif message.content.lower() == 'react native':
            for key, value in urls.items():
                if key == 'react native':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? confira um site sobre do React Native: {link}')
        # TYPE FLUTTER
        elif message.content.lower() == 'flutter':
            for key, value in urls.items():
                if key == 'flutter':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Flutter é o : {link}')
        # TYPE NODEJS
        elif message.content.lower() == 'nodejs' or message.content.lower() == 'node js':
            for key, value in urls.items():
                if key == 'nodejs':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do NodeJs é o : {link}')
        # TYPE MYSQL
        elif message.content.lower() == 'mysql':
            for key, value in urls.items():
                if key == 'mysql':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do MySql é o : {link}')      
        # TYPE POSTGRES
        elif message.content.lower() == 'postgres' or message.content.lower() == 'postgresql' :
            for key, value in urls.items():
                if key == 'postgres':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do PostgreSQL é o : {link}')     
        # TYPE ORACLE
        elif message.content.lower() == 'oracle':
            for key, value in urls.items():
                if key == 'oracle':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Oracle é o : {link}')    
        # TYPE MONGODB
        elif message.content.lower() == 'mongodb' or message.content.lower() == 'mongo':
            for key, value in urls.items():
                if key == 'mongodb':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do MongoDB é o : {link}')    
        # TYPE MARIADB
        elif message.content.lower() == 'mariadb':
            for key, value in urls.items():
                if key == 'mariadb':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do MariaDB é o : {link}')  
        # TYPE GITHUB
        elif message.content.lower() == 'github':
            for key, value in urls.items():
                if key == 'github':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do GitHub é o : {link}')  
        # TYPE YOUTUBE
        elif message.content.lower() == 'youtube':
            for key, value in urls.items():
                if key == 'youtube':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do YouTube é o : {link}')  
        # TYPE NOTION
        elif message.content.lower() == 'notion':
            for key, value in urls.items():
                if key == 'notion':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Notion é o : {link}')  
        # TYPE CANVA
        elif message.content.lower() == 'canva':
            for key, value in urls.items():
                if key == 'canva':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Canva é o : {link}')  
        # TYPE FIGMA
        elif message.content.lower() == 'figma':
            for key, value in urls.items():
                if key == 'figma':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Figma é o : {link}')  
        # TYPE CLASSROOM
        elif message.content.lower() == 'classroom':
            for key, value in urls.items():
                if key == 'classroom':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial do Classroom é o : {link}')  
        # TYPE AMAZON
        elif message.content.lower() == 'amazon':
            for key, value in urls.items():
                if key == 'amazon':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial da Amazon é o : {link}')  
        # TYPE TWITCHTV
        elif message.content.lower() == 'twitch' or message.content.lower() == 'twitchtv':
            for key, value in urls.items():
                if key == 'twitch':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial da Twitch é o : {link}')  
        # TYPE NIMOTV
        elif message.content.lower() == 'nimo' or message.content.lower() == 'nimotv':
            for key, value in urls.items():
                if key == 'nimotv':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial da NimoTv é o : {link}')  
        # TYPE NETFLIX
        elif message.content.lower() == 'netflix':
            for key, value in urls.items():
                if key == 'netflix':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial da Netflix é o : {link}')  
        # TYPE GMAIL
        elif message.content.lower() == 'gmail':
            for key, value in urls.items():
                if key == 'gmail':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial da Gmail é o : {link}')  
        # TYPE STACKOVERFLOW
        elif message.content.lower() == 'stackoverflow':
            for key, value in urls.items():
                if key == 'stackoverflow':
                    link = value
                    await message.channel.send(f'Olá {message.author.name}! Tudo bem? O site oficial da Stackoverflow é o : {link}')  
        
        # GAME VALORANT
        elif message.content.lower() == '!valorant':
            if not message.author.name in valorant:
                num -= 1
                embed = discord.Embed(
                    description = 'Partida de Valorant',
                    colour = discord.Color.red(),   
                )
                embed.set_author(name='Valorant', icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSks9EcbnJJvy81pYvEs--d6mPyCX5SESNULQ&usqp=CAU')
                for i in valorant:
                    if valorant[c] == 'Em espera':
                        valorant.remove(valorant[c])
                        valorant.insert(c, message.author.name)
                        c +=1
                        break

                embed.add_field(name=valorant[0], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=valorant[1], value='-', inline=1)
                embed.add_field(name=valorant[2], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=valorant[3], value='-', inline=1)
                embed.add_field(name=valorant[4], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=valorant[5], value='-', inline=1)
                embed.add_field(name=valorant[6], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=valorant[7], value='-', inline=1)
                embed.add_field(name=valorant[8], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=valorant[9], value='-', inline=1)


                if valorant[9] != 'Em espera':
                    valorant = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']


                embed.set_footer(text=f'faltam {num} jogadores!')

                await message.channel.send(embed = embed)
        # GAME LEAGUE OF LEGENDS
        elif message.content.lower() == '!lol':
            if not message.author.name in lol:
                num -= 1
                embed = discord.Embed(
                    description = 'Partida de LOL',
                    colour = discord.Color.blue()   
                )
                embed.set_author(name='League of Legends', icon_url='https://cf.shopee.com.br/file/18161864da5ffa51bd62118fb461b997_tn')
                for i in lol:
                    if lol[c] == 'Em espera':
                        lol.remove(lol[c])
                        lol.insert(c, message.author.name)
                        c +=1
                        break

                embed.add_field(name=lol[0], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=lol[1], value='-', inline=1)
                embed.add_field(name=lol[2], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=lol[3], value='-', inline=1)
                embed.add_field(name=lol[4], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=lol[5], value='-', inline=1)
                embed.add_field(name=lol[6], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=lol[7], value='-', inline=1)
                embed.add_field(name=lol[8], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=lol[9], value='-', inline=1)


                if lol[9] != 'Em espera':
                    lol = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']


                embed.set_footer(text=f'faltam {num} jogadores!')

                await message.channel.send(embed = embed)
        # GAME WILD RIFT
        elif message.content.lower() == '!wr':
            if not message.author.name in wr:
                num -= 1
                embed = discord.Embed(
                    description = 'Partida de WildRift',
                    colour = discord.Color.blue()   
                )
                embed.set_author(name='Lol - WildRift', icon_url='https://img.ibxk.com.br/2020/11/10/10174259667315.jpg')
                for i in wr:
                    if wr[c] == 'Em espera':
                        wr.remove(lol[c])
                        wr.insert(c, message.author.name)
                        c +=1
                        break

                embed.add_field(name=wr[0], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=wr[1], value='-', inline=1)
                embed.add_field(name=wr[2], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=wr[3], value='-', inline=1)
                embed.add_field(name=wr[4], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=wr[5], value='-', inline=1)
                embed.add_field(name=wr[6], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=wr[7], value='-', inline=1)
                embed.add_field(name=wr[8], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=wr[9], value='-', inline=1)


                if wr[9] != 'Em espera':
                    wr = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']


                embed.set_footer(text=f'faltam {num} jogadores!')

                await message.channel.send(embed = embed)

        # GAME CS:GO
        elif message.content.lower() == '!cs':
            if not message.author.name in cs:
                num -= 1
                embed = discord.Embed(
                    description = 'Partida de CS:GO',
                    colour = discord.Color.gold()
                )
                embed.set_author(name='CS:GO', icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_UkSn7PNFvaHwrsoPmCilreY5ThFDI0HLoBamNI8YyXvlm40wBu7oveM6WJT636y9kXU&usqp=CAU')
                for i in cs:
                    if cs[c] == 'Em espera':
                        cs.remove(lol[c])
                        cs.insert(c, message.author.name)
                        c +=1
                        break

                embed.add_field(name=cs[0], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=cs[1], value='-', inline=1)
                embed.add_field(name=cs[2], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=cs[3], value='-', inline=1)
                embed.add_field(name=cs[4], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=cs[5], value='-', inline=1)
                embed.add_field(name=cs[6], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=cs[7], value='-', inline=1)
                embed.add_field(name=cs[8], value='-', inline=1)
                embed.add_field(name='     |', value='-', inline=1)
                embed.add_field(name=cs[9], value='-', inline=1)


                if cs[9] != 'Em espera':
                    cs = ['Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera', 'Em espera']


                embed.set_footer(text=f'faltam {num} jogadores!')

                await message.channel.send(embed = embed)

        # BADWORDS DETECTION 
        elif message.content.lower() == 'filho da puta' or message.content.lower() == 'gado' or message.content.lower() == 'puta' or message.content.lower() == 'rapariga' or message.content.lower() == 'caralho' or message.content.lower() == 'motherfucker' or message.content.lower() == 'bitch' or message.content.lower() == 'mtf' or message.content.lower() == 'mtfb' or message.content.lower() == 'fdp' or message.content.lower() == 'foda-se' or message.content.lower() == 'fodase' or message.content.lower() == 'foda se' or message.content.lower() == 'vai se fuder' or message.content.lower() == 'vão se fuder' or message.content.lower() == 'vao se fuder' or message.content.lower() == 'vsf':
            await message.author.send(f'Olá {message.author.name}, é devidamente proibido o envio de palavrões no servidor. A repetição dessa conduta poderá resultar em punições futuras')
            await message.channel.purge(limit=1)

        # WARNING NOT VERIFYED LINK
        elif message.content[0:5] == 'http/':
            await message.channel.send(f'ATENÇÃO: este link pode não ser seguro!')

    # MENSAGEM DE MEMBRO NOVO
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None :
            mensagem = f'{member.mention} acabou de entrar no servidor {guild.name}!Seja bem-vindo(a)!'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('TOKEN')