import requests
import telebot

# Ваши данные
BOT_TOKEN = "замените на телеграмм токен" 
WOL_URL = "адресс включения пк"
USERNAME = "123"  # Замените на имя пользователя
PASSWORD = "123"  # Замените на пароль

# Создание бота
bot = telebot.TeleBot(BOT_TOKEN)

# Функция для включения ПК по WOL
@bot.message_handler(commands=['wake'])
def wake_on_lan(message):
    try:
        response = requests.get(WOL_URL, auth=(USERNAME, PASSWORD))  # Добавление аутентификации
        if response.status_code == 200:
            bot.reply_to(message, "Отправлен запрос на включение ПК. ПК должен включиться.")
        else:
            bot.reply_to(message, f"Ошибка: {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

# Обработчик команд
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для включения ПК. Используйте команду /wake, чтобы включить его.")

# Запуск бота
bot.polling(none_stop=True)
      
