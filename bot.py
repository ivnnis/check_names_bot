import telebot


TOKEN = '6486211277:AAETCrj2dnIqRttzlzbkw8_rR2LX33rxq68'
filename = 'user_mentions.txt'

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        bot.send_message(message.chat.id, "Привет! Перешли сообщение в этот чат для записи")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

# Обработчик для пересылаемых сообщений
@bot.message_handler(func=lambda message: message.forward_from is not None)
def handle_forwarded_message(message):
    try:
        # Получаем ник автора пересылаемого сообщения
        author_username = message.forward_from.username
        
        if author_username:
            with open(filename, 'a') as file:
                # Проверяем, есть ли упоминание уже в файле
                if author_username not in open(filename, 'r').read():
                    # Записываем новое упоминание в файл
                    file.write(author_username + '\n')
                else:
                    bot.send_message(message.chat.id, f"Предупреждение: {author_username} уже был.")
                    # Если упоминание уже есть, не записываем его в файл
    except Exception as e:
        print(f"Ошибка при обработке пересылаемого сообщения: {e}")

# Запускаем бота
while True:
    try:
        bot.polling()
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
