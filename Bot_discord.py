import random
import discord
import requests
import json


#funcoes:

#MEME
def get_meme():
  resposta = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(resposta.text)
  return json_data['url']



#PIADAS
def load_piadas():
    with open('piadas.json ', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_piada():
    piadas = load_piadas()
    return random.choice(piadas)



#APOIOS
def carregar_apoio():
    with open('apoio.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
def get_apoio():
    apoios = carregar_apoio()
    return random.choice(apoios)




class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
       
        if message.author == self.user:
            return

        conteudo = message.content.lower()
        

        if conteudo.startswith('$help'):
            await message.channel.send(
                'Olá! Sou o Bot do Discord da hannover, aqui vai uma lista do que posso fazer:\n'
                ' - Enviar memes com $meme\n'
                ' - Enviar mensagens de apoio automatizadas com $apoio\n'
                ' - Enviar piadas com $piada\n'
            )
            return

        if conteudo.startswith('$piada'):
            await message.channel.send(get_piada())
            return

        if conteudo.startswith('$meme'):
            await message.channel.send(get_meme())
            return
         
        if conteudo.startswith('$apoio'):
            await message.channel.send(get_apoio())
            return 
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token') #meu token
