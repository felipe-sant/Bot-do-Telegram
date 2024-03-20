import telebot

from config import TOKEN as API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

list = []

@bot.message_handler(commands=["add"])
def mensagem(m):

    mensagem = m.text
    mensagem = mensagem.replace("/add ", "")

    global list
    list.append(mensagem)

    bot.reply_to(m, f"'{mensagem}' foi adicionado a lista")
    print(list)

@bot.message_handler(commands=["list"])
def lista(m):
    global list
    bot.reply_to(m, f"A lista atual é: ")
    for item in list:
        pos = list.index(item) + 1
        bot.send_message(m.chat.id, f"{pos}º {item}")

bot.polling()