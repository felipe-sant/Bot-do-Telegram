from config import TOKEN as API_TOKEN
from organizer import organizar_lista
import telebot

listaDeEscolhas = []
assunto = "I would like to buy a muzzarella pizza"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start", "help"])
def iniciar(mensagem):
    bot.reply_to(mensagem, f"Olá, eu sou um bot organizador utilizando o Transformers!\n\n - Comandos:\n/add [item] - Adiciona um item a lista\n/list - Lista os itens\n/organize - Organiza a lista\n/clear - Limpa a lista\n\n O assunto padrão está como '{assunto}', escreva algo sem comandos para mudar o assunto.")

# comando do /add
@bot.message_handler(commands=["add"])
def adicionar(mensagem):
    # pega o texto da mensagem e remove o /add
    elemento = mensagem.text
    elemento = elemento.replace("/add ", "")
    # adiciona o elemento na lista
    global listaDeEscolhas
    listaDeEscolhas.append(elemento) 
    bot.reply_to(mensagem, f"'{elemento}' foi adicionado a lista.")

@bot.message_handler(commands=["list"])
def listar(mensagem):
    global listaDeEscolhas
    if len(listaDeEscolhas) == 0:
        bot.reply_to(mensagem, "A lista está vazia.")
    else:
        bot.reply_to(mensagem, f"A lista é: ")
        # envia a lista
        for item in listaDeEscolhas:
            pos = listaDeEscolhas.index(item) + 1
            bot.send_message(mensagem.chat.id, f"{pos}º {item}")

# comando do /list
@bot.message_handler(commands=["organize"])
def listar(mensagem):
    global listaDeEscolhas
    if len(listaDeEscolhas) == 0:
        bot.reply_to(mensagem, "A lista está vazia.")
    else: 
        bot.reply_to(mensagem, f"Isso pode demorar um pouco.\n\nA lista organizada é: ")
        listaDeEscolhas = organizar_lista(listaDeEscolhas, assunto) # organiza a lista
        # envia a lista organizada
        for item in listaDeEscolhas:
            pos = listaDeEscolhas.index(item) + 1
            bot.send_message(mensagem.chat.id, f"{pos}º {item}")

@bot.message_handler(commands=["clear"])
def limpar(mensagem):
    global listaDeEscolhas
    listaDeEscolhas = []
    bot.reply_to(mensagem, "A lista foi limpa.")

@bot.message_handler(func=lambda message: True)
def echo_all(mensagem):
    bot.reply_to(mensagem, "Mudando o assunto para: " + mensagem.text)
    global assunto
    assunto = mensagem.text

print("- Bot is running -")
bot.polling()