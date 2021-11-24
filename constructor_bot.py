import telebot

bot = telebot.TeleBot('2145551349:AAEvTby4sRkkw7YCtoSp_f7hOdX7E4prfHI')

answer_dict = {
    'Привет': 'Здорова',
    '/help': 'Напиши привет',
    'Да': 'Нет',
    'Че': 'Каво',
}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in answer_dict:
        bot.send_message(message.from_user.id, answer_dict[message.text])
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)