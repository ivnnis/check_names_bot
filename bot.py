import telebot


TOKEN = '6486211277:AAETCrj2dnIqRttzlzbkw8_rR2LX33rxq68'
filename = 'user_mentions.txt'

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! скинь ник пользователя в формате @abc")

<<<<<<< HEAD
@bot.message_handler(func=lambda message: message.forward_from is not None)
=======
@bot.message_handler(func=lambda message: True)
>>>>>>> 89ce18739b40ecaa5ac481b6ee683134764aafc5
def handle_forwarded_message(message):
    # Получаем ник автора пересылаемого сообщения
    author_username = message.forward_from.username
    
    if author_username:
        with open(filename, 'a') as file:
            # Проверяем, есть ли упоминание уже в файле
            if author_username not in open(filename, 'r').read():
                # Записываем новое упоминание в файл
                file.write(author_username + '\n')
            else:
<<<<<<< HEAD
                bot.send_message(message.chat.id, f"Предупреждение: {author_username} уже был.")
=======
                bot.send_message(message.chat.id, f"Предупреждение: {author_username} уже был")
>>>>>>> 89ce18739b40ecaa5ac481b6ee683134764aafc5
                # Если упоминание уже есть, не записываем его в файл

# Запускаем бота
bot.polling()
