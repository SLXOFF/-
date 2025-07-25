python
import telebot

user_bot_token = '8445365374:AAHLzksg0CZDrqIJgt8NYj5M-sgskjFTxQQ'
user_bot = telebot.TeleBot(user_bot_token)

@user_bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_bot.reply_to(message, "Привет! Чем я могу помочь?")

@user_bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Здесь можно добавить обработку и отправку сообщения администратору
    user_bot.reply_to(message, "Спасибо за ваше сообщение. Администратор свяжется с вами в ближайшее время.")

user_bot.polling()
