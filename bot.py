import CONFIG
import telebot
import os

tok = CONFIG.TOKEN
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,'/help - all the commands')


@bot.message_handler(commands=['help'])
def help(message):
        bot.send_message(message.chat.id,'/help - all the commands, /start - start bot, /sd - shut down pc, /csd cancel sd')

@bot.message_handler(commands=['sd'])
def sd(message):
	bot.send_message(message.chat.id,'shutdown your PC')
	os.system('shutdown -P +1 "PC shutdown"')

@bot.message_handler(commands=['csd'])
def csd(message):
	bot.send_message(message.chat.id,'cancel shutdown PC')
	os.system('shutdown -c')

@bot.message_handler()
def mes(message):
	res = os.system(message.text)
	bot.send_message(message.chat.id,res)

bot.polling(none_stop=True)
#print('bot started')
#
