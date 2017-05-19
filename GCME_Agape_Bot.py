# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot("208413095:AAFflQth4lhFdXUQkJaHjemOfIqFRZT2_DU")

menu1 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'የእግዚአብሔርን ፍቅር  በግል እየተለማመድኩ ነው')
itembtn2 = types.KeyboardButton(u'ማወቅ ፈልጋለሁ')
menu1.add(itembtn1, itembtn2)

menu2 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'የመጀመርያው ሕግ')
menu2.add(itembtn1)

menu3 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ሁለተኛው ሕግ')
menu3.add(itembtn1)

menu4 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ሦስተኛው ሕግ')
menu4.add(itembtn1)

menu5 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'አራተኛው ሕግ')
menu5.add(itembtn1)


intro_markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ስለ ክርስቶስ ከዚህ በፊት አልሰማሁም')
itembtn2 = types.KeyboardButton(u'ስለ ክርስቶስ ከዚህ በፊት ሰምቻለሁ')
itembtn3 = types.KeyboardButton(u'ስለ ክርስቶስ ተጨማሪ መረጃዎች')
intro_markup.add(itembtn1, itembtn2, itembtn3)

non_believer_markup1 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'እግዚአብሔርን ፍቅር በግል ማወቅ')
non_believer_markup1.add(itembtn1, itembtn2, itembtn3)

non_believer_markup2 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'እግዚአብሔርን ፍቅር በግል ማወቅ')
non_believer_markup2.add(itembtn1, itembtn2, itembtn3)

text_messages = {'welcome':u'እንካን ወደ አጋፔ መጡ!\n\nየእግዚአብሔርን ፍቅር በግል ማወቅ(AGAPE BOT) '
                           u'\nየእግዚአብሔርን ፍቅር በግል ለማወቅ ምን ያስፈልግሀል? የመብረቅ ብልጭታ? ጥብቅ ኃይማኖታዊ ስርዓት? የተሻልክ '
                           u'ሰው ሆኖ መገኘት? አንዳቸውም እነደ ቅደመ ሆኔታ አያስፈልጉህም፡፡ እግዚአብሔር እርሱን ለማወቅ የሚያስፈልገንን '
                           u'መፅሐፍ ቅዱስ ላይ በግልፅ አስቀምጦልናል፡፡ ማንኛውም ነገር ደንብና ስርዓት አለው፡፡ ሰው የሠራቸው ነገሮች ሰው '
                           u'ሰራሽ ስርዓት እንዳላቸው ሁሉ እግዚአብሔር የፈጠራቸው ነገሮች ደግም የተፈጥሮ ሕግጋት አሏቸው፡፡እነዲሁም ሰው '
                           u'ከእግዚአብሔር ጋር የሚኖረውን ግንኙነት የሚወስኑ አራት መንፈሳዊ ሕጎች አሉ፡፡ መርሆች ብለህም ልትወስዳቸው ትችላለህ፡፡ '
                           u'\nይህን ማወቅ ትፈልጋለህ ?',
                 'step1':u'የመጀመርያው ሕግ '
                         u'\nእግዚአብሔር ይወድሃል ስለዚህም ለሕይወትህ አስደናቂ ዕቅድ አዘጋጅቶልሃል፡፡'
                         u'የእግዚአብሔር ፍቅር “በእርሱ የሚያምን ሁሉ የዘላለም ሕይወት እንዲኖረው እንጂ እንዳይጠፋ እግዚአብሔር አንድያ ልጁን '
                         u'እስኪሰጥ ድረስ አለሙን እንዲሁ ወዶአልና፡፡”(ዮሐ 3፡16) '
                         u'የእግዚአብሔር ዕቅድ ክርስቶስ እንዲህ አለ፡- “እኔ ሕይወት እንዲሆንላቸው እንዲበዛላቸውም መጣሁ፡፡”(ዮሐ 10፡10) '
                         u'ነገር ግን ሰዎች ሁሉ ይህንን መሉና አርኪ ሕይወት አልተለማመዱም ምክንያቱን በ ሁለተኛው ሕግ ያገኙታል።',
                 'step2':u'ሁለተኛው ሕግ '
                         u'\nሰው ኃጢአተኛ ነው፡፡ በዚህም ምክንያት ከእግዚአብሔር ተለይቷል፡፡ ስለዚህም የእግዚአብሔርን ፍቅርና ዕቅድ ማወቅና በሕይወቱ መለማመድ አይችልም፡፡'
                         u'ሰው ኃጥአተኛ ነው “ሁሉ ኃጢአትን ሠርተዋልና የእግዚአብሔርም ክብር ጎድሎአቸዋል፡፡”(ሮሜ 3፡23) እግዚአብሔር ሰውን ሲፈጥረው ከእርሱ ጋር የቀረበ ግንኙነት '
                         u'በመመስረት በደስታ እንዲኖር ነበር፡፡ነገር ግን ሰው በራሱ መንገድ ለመጓዝ በመምረጡ ግንኙነታቸው ተቋረጠ፡፡ በራሳችን መንገድ ስንጓዝ ለእግዚአብሔር የማንታዘዝና '
                         u'ለርሱም ግድ የሌለን እንሆናለን፡፡ መጽሐፍ ቅዱስ ይህን አይነቱን አስተሳሰብ ነው ኃጢአት ብሎ የሚጠራው፡፡ '
                         u'“እኛ ሁላችን እንደ በጎች ተቅበዝብዘን ጠፋን ከእኛ እያንዳንዱ ወደ ገዛ መንገዱ አዘነበለ፡፡”(ኢሳ 53፡6) ሰው ከእግዚአብሔር ተለይቷል ሰዎች '
                         u'“የኃጢአት ደመወዝ ሞት ነውና” (ሮሜ 6፡23) ይህም ሞት በመንፈስ ከእግዚአብሔር መለየት ማለት ነው፡፡',
                 'step3':u'ሦስተኛው ሕግ '
                         u'\nሰው ወደ እግዚአብሔር ሊደርስ የሚችልበት ብቸኛው መንገድ ኢየሱስ ክርስቶስ ነው፡፡ እርሱ ስለ እኛ ሞቷል፡፡ ስለዚህም ሰው በእርሱ በኩል '
                         u'የእግዚአብሔርን ፍቅርና ዕቅድ ሊያውቅና ሊለማመድ ይችላል፡፡ እርሱ በእኛ ምትክ ሞተ ‹‹ነገር ግን ገና ኃጢያተኞች ሳለን ክርስቶስ ስለ እኛ ሞቷልና እግዚአብሔር ለእኛ ያለውን የራሱን ፍቅር ያስረዳል፡፡›› (ሮሜ. 5፡8) '
                         u'ከሞት ተነስቷል ‹‹…ክርስቶስ ስለ ኃጢያታችን ሞተ ተቀበረም መጽሐፍ እንደሚል በሦስተኛው ቀን ተነሣ፣ …›› (1ኛ ቆሮ. 15፡3-5) እርሱ ብቸኛ መንገድ ነው፡:'
                         u'\nኢየሱስ እንዲህ አለ፡- ‹‹እኔ መንገድና እውነት ሕይወትም ነኝ በእኔ በቀር ወደ አብ የሚመጣ የለም›› (ዩሐ› 14፡6)',
                 'step4':u'አራተኛው ሕግ '
                         u'\nእያንዳንዳችን ኢየሱስ ክርስቶስን እንደ አዳኛችንና እንደ ጌታችን ልንቀበለው ይገባናል፡፡ ከዚያም የእግዚአብሔርን ፍቅርና ዕቅድ በሕይወታችን ልናውቅና '
                         u'ልንለማመድ እንችላለን፡፡ ክርስቶስን ልንቀበለው ይገባናል ‹‹ለተቀበሉት ሁሉ ግን በስሙ ለሚያምኑ ለእነርሱ የእግዚአብሔር ልጆች ይሆኑ ዘንድ ሥልጣንን ሰጣቸው››(ዩሐ.1፡12) ክርስቶስን በእምነት ልንቀበለው ይገባል '
                         u'‹‹ጸጋው በእምነት አድኖአችኋልና፤ ይህም የእግዚአብሔር ስጦታ ነው እንጂ ከእናንተ አይደለም ማንም እንዳይመካ ከሥራ አይደለም›› (ኤፌ. 2፡8-9)፡፡ በግላችን ክርስቶስን ወደ ሕይወታችን በመጋበዝ ልንቀበለው ይገባል'
                         u'\nክርስቶስ እንዲህ ይላል፡- ‹‹እነሆ በደጅ ቆሜ አንኳኳለሁ ማንም ድምጼን ቢሰማ ደጁንም ቢከፍትልኝ ወደ እርሱ እገባለሁ ከእርሱም ጋር እራት እበላለሁ እርሱም ከእኔ ጋር ይበላል›› (ራዕ. 3፡20)'
                         u'\nክርስቶስን መቀበል የሚከተሉትን ያጠቃልላል'
                         u'\n\t- ኃጢያተኛ መሆናችንን ማወቅና ከኃጢያታችን ለመመለስ በመወሰን ከእግዚአብሔር ጋር መስማማት'
                         u'\n\t- ኢየሱስ ክርስቶስ ኃጢያታችንን ይቅር እንደሚልና ወደ ሕይወታችንም እንደሚመጣ ማመን'
                         u'\n\t- ክርስቶስ በእኛ ውስጥ እንዲኖር መፍቀድና እርሱን ማሳየት'
                         u'\እነዚህ ሁለት ክቦች ሁለት አይነት ሕይወት ይወክላሉ፡፡'
                 }



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text_messages['welcome'], reply_markup=menu1)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    replay_send(message)

@bot.inline_handler(lambda query: query.query == 'mezmur')
def query_text(inline_query):
# Query message is text
    pass

def replay_send(message):
    if(message.text == u"ማወቅ ፈልጋለሁ"):
        bot.send_message(message.chat.id, text_messages['step1'], reply_markup=menu1)
    elif (message.text == u"የመጀመርያው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step2'], reply_markup=menu2)
    elif (message.text == u"ሁለተኛው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step3'], reply_markup=menu3)
    elif (message.text == u"አራተኛው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step3'], reply_markup=menu4)
    else:
        bot.send_message(message, u'እባክዎ ከታች የተመለከቱትን የምርጫ ቁልፎች ይጠቀሙ', reply_markup=menu1)

bot.polling()