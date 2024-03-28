
import telebot
from telebot import types
import random
bot=telebot.TeleBot('7199398435:AAHxpw0GB01kSNGDDcR216KTBN2xFe64PzY')

points = 0

words1= ['Ответ правильный!']
random1=random.choices(words1)
random2= random1[0] or random1[1] or random1[2] or random1[3]

words2= ['Ответ неправильный!']
random1_=random.choices(words2)
random2_= random1_[0] or random1_[1] or random1_[2] or random1_[3]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет!Я предлагаю тебе принять участие в викторине «Каждый шаг – эпоха»')

@bot.message_handler(content_types=['text'])
def lalala(message):
    global points
    global random2
    global random2_
    if message.text =='Викторина' or message.text =='викторина':
        points = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Зайцев В.М')
        item2 = types.KeyboardButton('Гарелин Я.П.')
        item3 = types.KeyboardButton('Бурылин Д.Г.')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id,'1) Назовите  имя  ивановского мецената- коллекционера – основателя Ивановского историко-краеведческого музея',reply_markup=markup)

    if message.chat.type =='private':
        if message.text == 'Бурылин Д.Г.':
            bot.send_message(message.chat.id,random2)
            points +=1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('1914')
            item2 = types.KeyboardButton('1924')
            item3 = types.KeyboardButton('1912')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '2) Когда произошло торжественное открытие Ивановского историко-краеведческого музея', reply_markup=markup)

        elif message.text == 'Гарелин Я.П.':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Ответ:Бурылин Д.Г.')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('1914')
            item2 = types.KeyboardButton('1924')
            item3 = types.KeyboardButton('1912')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '2) Когда произошло торжественное открытие Ивановского историко-краеведческого музея', reply_markup=markup)


        elif message.text == 'Зайцев В.М':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Ответ:Бурылин Д.Г.')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('1914')
            item2 = types.KeyboardButton('1924')
            item3 = types.KeyboardButton('1912')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '2) Когда произошло торжественное открытие Ивановского историко-краеведческого музея', reply_markup=markup)


        if message.text == '1914':
            bot.send_message(message.chat.id, random2)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('более 780 тысяч')
            item2 = types.KeyboardButton('менее 500 тысяч')
            item3 = types.KeyboardButton('около 300 тысяч')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '3) Сколько музейных предметов от античности до современности имеет  в своих фондах Ивановский историко-краеведческий музей.', reply_markup=markup)


        elif message.text == '1924':
            bot.send_message(message.chat.id,random2_)
            bot.send_message(message.chat.id,'ответ 1914')
            points +=0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('более 780 тысяч')
            item2 = types.KeyboardButton('менее 500 тысяч')
            item3 = types.KeyboardButton('около 300 тысяч')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id,'3) Сколько музейных предметов от античности до современности имеет  в своих фондах Ивановский историко-краеведческий музей.',reply_markup=markup)


        elif message.text == '1912':
            bot.send_message(message.chat.id,random2_)
            bot.send_message(message.chat.id,'ответ 1914')
            points +=0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('более 780 тысяч')
            item2 = types.KeyboardButton('менее 500 тысяч')
            item3 = types.KeyboardButton('около 300 тысяч')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id,'3) Сколько музейных предметов от античности до современности имеет  в своих фондах Ивановский историко-краеведческий музей.',reply_markup=markup)

        elif message.text == '1924':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'ответ 1914')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('более 780 тысяч')
            item2 = types.KeyboardButton('менее 500 тысяч')
            item3 = types.KeyboardButton('около 300 тысяч')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '3) Сколько музейных предметов от античности до современности имеет  в своих фондах Ивановский историко-краеведческий музей.',reply_markup=markup)



        if message.text=='более 780 тысяч':
            bot.send_message(message.chat.id,random2)
            points+=1

            bot.send_message(message.chat.id, f'Набранное количество баллов: {points} ')
        elif message.text=='менее 500 тысяч':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'ответ: более 780 тысяч')
            points += 0

            bot.send_message(message.chat.id, f'Набранное количество баллов: {points}')
        elif message.text=='около 300 тысяч':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'ответ: более 780 тысяч')
            points += 0

            bot.send_message(message.chat.id, f'Набранное количество баллов: {points} ')


bot.polling(none_stop=True)

