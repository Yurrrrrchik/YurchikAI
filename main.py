import telebot

bot = telebot.TeleBot('6101573081:AAHGx3Di3qjtLMnmCM4IpuVXPWyWj_uYRYE')

@bot.message_handler(commands=['start'])
def start(message):
    file = open('./chpau.m4a', 'rb')
    bot.send_voice(message.chat.id, file)
    bot.send_message(message.chat.id, "Let's get it started here")

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, "Что я могу делать? ахм, честно говоря, пока не особо много чего. "
                                      "Могу посчитать ваш психологический возраст! Для этого введите 5 чисел "
                                      "через пробел, и используя свою гениальнейшую (нет) математику я скажу, "
                                      "на сколько лет вы чувствуете себя внутри. ✨")

@bot.message_handler()
def hello(message):
    sep = message.text.split(" ")
    try:
        for i in sep:
            i = int(i)
        if len(sep) == 5:
            if int(sep[4]) != 0:
                age = round((int(sep[0]) + int(sep[1]) - int(sep[2]))*int(sep[3])/int(sep[4]), 2)
                bot.send_message(message.chat.id, f"Ваш психологический возраст: {age}")
                if age > 100:
                    bot.send_message(message.chat.id, "(офигеть вы пенсионер)")
            else:
                bot.send_message(message.chat.id, "оу-- я боюсь вы слишком стары для этого мира...")
        else:
            bot.send_message(message.chat.id, "я сказав 5 цифр!!! пересчитайте ! 🦄")
    except ValueError:
        bot.send_message(message.chat.id, "???")
    if message.text.lower() == 'привет' or message.text.lower() == 'hello' or message.text.lower() == 'bonjour':
        bot.reply_to(message, "hello from the other siiiiiiiiiiiiiiiiiide")
    if message.text.lower() == 'доброе утро':
        bot.reply_to(message, "Доброе утро, мои родные люди")


bot.polling(none_stop=True)