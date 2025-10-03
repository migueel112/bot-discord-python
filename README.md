# 🤖 Bot do Discord - Hannover

Este é um bot para **Discord**, desenvolvido em **Python**, que envia memes, piadas e mensagens de apoio.  
O projeto ainda está em **desenvolvimento**, e novas funcionalidades serão adicionadas futuramente.  

O objetivo é criar um ambiente divertido e interativo para os membros do servidor, explorando o uso de APIs, manipulação de arquivos JSON e integrações com o Discord.

---

## 🚀 Funcionalidades atuais
- Enviar memes usando a **API pública** do [meme-api.com](https://meme-api.com/) com `$meme`
- Enviar mensagens de apoio automatizadas com `$apoio`
- Enviar piadas salvas em um arquivo `piadas.json` com `$piada`
- Responder a saudações simples como `$ola`
- Mostrar a lista de comandos disponíveis com `$help`

---

## 🛠️ Tecnologias e recursos usados
- **Python 3** → Linguagem principal do projeto.
- **discord.py** → Biblioteca para criar bots e interagir com a API do Discord.
- **requests** → Biblioteca usada para fazer requisições HTTP a APIs externas.
- **json** → Usado para carregar e manipular dados em arquivos JSON (como as piadas).
- **HTTPS/REST API** → Comunicação com a API de memes é feita via protocolo HTTPS, retornando dados em formato JSON.

Exemplo de fluxo:
1. O bot recebe um comando `$meme`.
2. O Python usa a biblioteca `requests` para acessar a API `https://meme-api.com/gimme`.
3. O retorno vem em formato JSON.
4. O bot lê a chave `"url"` e envia o meme para o canal do Discord.
