import telebot
bot = telebot.TeleBot('ваш токен')
@bot.message_handler(commands=['start'])
