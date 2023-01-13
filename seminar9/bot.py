import telebot
import cfg

bot = telebot.TeleBot(cfg.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет Саня")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# def del_abv(text):
#     text = text.split(' ')
#     return ' '.join([i for i in text if 'абв' not in i])


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.send_message(message.chat.id, del_abv(message.text))
#     bot.send_message(message.chat.id, f'из исходной строки {message.text} \
# удалены все слова с "абв"')



# @bot.message_handler(func=lambda message: True)
# def abv(message):
#     a = "абв"
#     new_list = ' '.join([i for i in message.text.split() if i.find(a) == -1])
#     bot.reply_to(message, new_list)


bot.infinity_polling()
