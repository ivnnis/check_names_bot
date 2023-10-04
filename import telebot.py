import telebot


TOKEN = '6486211277:AAETCrj2dnIqRttzlzbkw8_rR2LX33rxq68'
filename = 'user_mentions.txt'

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! скинь ник пользователя в формате @abc")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получаем текст сообщения
    text = message.text
    
    # Проверяем, есть ли упоминания пользователей с @
    mentions = [user_mention for user_mention in text.split() if user_mention.startswith('@')]
    
    if mentions:
        with open(filename, 'a') as file:
            for mention in mentions:
                # Проверяем, есть ли упоминание уже в файле
                if mention not in open(filename, 'r').read():
                    # Записываем новое упоминание в файл
                    file.write(mention + '\n')
                    bot.send_message(message.chat.id, f"Записал {mention}")
                else:
                    bot.send_message(message.chat.id, f"Предупреждение: {mention} уже был")
                    # Если упоминание уже есть, не записываем его в файл

# Запускаем бота
bot.polling()
