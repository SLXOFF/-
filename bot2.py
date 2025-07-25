python
import telebot

admin_bot_token = '8445335154:AAGrzCMpSyo_ko0G8VIGp00-H8aE8TNHvec'
admin_bot = telebot.TeleBot(admin_bot_token)

@admin_bot.message_handler(commands=['start', 'manage'])
def send_welcome(message):
    admin_bot.reply_to(message, "Добро пожаловать, администратор!")

@admin_bot.message_handler(func=lambda message: True)
def respond_to_user(message):
    # Логика взаимодействия администратора с пользователем
    admin_bot.reply_to(message, "Ответ на запрос пользователя.")

admin_bot.polling()
