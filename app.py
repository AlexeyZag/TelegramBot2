'@alex_zag_top_bot'

import telebot
from extensions import ConvertionExcepyion, Converter
from config_data import TOKEN


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"""Добро пожаловать в обменник, {message.chat.username}\nВводите данные в таком порядке:\n
"Валюта1" - "Валюта2" - "Количество"\n'
Например: доллар рубль 100'
:) Обменник покажет сколько валюты2 вы получите за "количество" валюты1\n
Для отображения списка валют нажмите /values""")
@bot.message_handler(commands=['values'])
def send_values(message):
    bot.send_message(message.chat.id, """ЕВРО\nДоллар\nРубль\nЙена\nКанадский_доллар\nШвейцарский_франк
Турецкая_лира\nИндийская_рупия""")

@bot.message_handler(content_types=['text'])
def convert(message):
    ask = message.text.split()
    try:
        if len(ask) != 3:
            raise ConvertionExcepyion('Вы ввели не три параметра.')
        quote, base, amount = ask
        text = Converter.convert(quote, base, amount)
    except ConvertionExcepyion as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'не удалось обработать команду\n{e}')
    else:
        bot.reply_to(message, text)
bot.polling(none_stop=True)