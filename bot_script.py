import weather_data as wd
import data
import telebot
import bot_helper

bot = telebot.TeleBot(data.token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help" or message.text == '/start':
        bot.send_message(message.from_user.id, data.help_text)
    else:
        temp = wd.get_temp(message.text)
        bot.send_message(message.from_user.id, temp)
        if temp != 'Введите название города правильно':
            text = wd.get_data(message.text)
            advice = bot_helper.get_temp_advice(int(temp[:-1]))
            bot.send_message(message.from_user.id, text)
            bot.send_message(message.from_user.id, advice)


bot.polling(none_stop=True, interval=0)
