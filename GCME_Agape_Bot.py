# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot("208413095:AAGiAHbryA-lcYBD_vQaWZQo4nlRIdPCrkY")

intro_markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ስለ ክርስቶስ ከዚህ በፊት አልሰማሁም')
itembtn2 = types.KeyboardButton(u'ስለ ክርስቶስ ከዚህ በፊት ሰምቻለሁ')
itembtn3 = types.KeyboardButton(u'ስለ ክርስቶስ ተጨማሪ መረጃዎች')
intro_markup.add(itembtn1, itembtn2, itembtn3)

non_believer_markup1 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'እግዚአብሔርን ፍቅር በግል ማወቅ')
non_believer_markup1.add(itembtn1, itembtn2, itembtn3)

text_messages = {'welcome':u'እንካን ወደ አጋፔ መጡ!\n\nይህን ስልጡን የጽሁፍ ቀመር የተለያዩ ጥያቄዎትን ሊጠይቁት ይችላሉ ስለዚህ ከታች የተመለከቱትን ምርጫዎችን ይምረጡ',
                 'non_believer':u'እግዚዘብሔርን በግል ለማወቅ ምን ያስፈልግሀል? የመብረቅ ብልጭታ? ጥብቅ ኃይማኖታዊ ስርዓት? የተሻልክ ሰው ሆኖ መገኘት? አንዳቸውም እነደ ቅደመ ሆኔታ አያስፈልጉህም፡፡ እግዚአብሔር እርሱን ለማወቅ የሚያስፈልገንን መፅሐፍ ቅዱስ ላይ በግልፅ አስቀምጦልናል፡፡'
                                u'\nማንኛውም ነገር ደንብና ስርዓት አለው፡፡ ሰው የሠራቸው ነገሮች ሰው ሰራሽ ስርዓት እንዳላቸው ሁሉ እግዚአብሔር የፈጠራቸው ነገሮች ደግም የተፈጥሮ ሕግጋት አሏቸው፡፡'
                                u'\nእነዲሁም ሰው ከእግዚአብሔር ጋር የሚኖረውን ግንኙነት የሚወስኑ አራት መንፈሳዊ ሕጎች አሉ፡፡ መርሆች ብለህም ልትወስዳቸው ትችላለህ፡፡'
                 }



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text_messages['welcome'], reply_markup=intro_markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    replay_send(message)

def replay_send(message):
    if(message.text == 'help'):
        bot.send_message(message.chat.id, text_messages['welcome'], reply_markup=intro_markup)
    elif(message.text == u"ስለ ክርስቶስ ከዚህ በፊት አልሰማሁም"):
        bot.send_message(message.chat.id, text_messages['non_believer'], reply_markup=non_believer_markup1)
    elif (message.text == "song2"):
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=BZrGJXBB3jc", reply_markup=intro_markup)
    else:
        bot.send_message(message.chat.id, message.text, reply_markup=intro_markup)


bot.polling()