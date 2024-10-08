# import telebot
# import os
# import django
# from blog.models import Contact
# from local_settings import API_TOKEN,chat_id
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'super_info_core.settings')
# django.setup()
#
# bot = telebot.TeleBot(API_TOKEN)
#
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Напишите мне своё сообщение, и я передам его команде 'Супер Инфо'.")
#
# @bot.message_handler(func=lambda message: True)
# def receive_feedback(message):
#     name = message.from_user.username or message.from_user.first_name
#     id = message.from_user.id
#     message = message.text
#
#     Contact.objects.create(name=name, id=chat_id, message=message)
#
#     bot.reply_to(message, "Спасибо за ваше сообщение! Мы его получили и обязательно рассмотрим.")
#
# bot.polling(none_stop=True, timeout=123)
