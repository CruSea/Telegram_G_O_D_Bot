# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot("208413095:AAFflQth4lhFdXUQkJaHjemOfIqFRZT2_DU")

menu1 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton(u'ማወቅ ፈልጋለሁ')
itembtn2 = types.KeyboardButton(u'የእግዚአብሔርን ፍቅር  በግል እየተለማመድኩ ነው')
itembtn3 = types.KeyboardButton(u'አጭር ፊልም ይመልከቱ')
itembtn4 = types.KeyboardButton(u'')
menu1.add(itembtn1, itembtn2, itembtn3)

menu2 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'የመጀመርያው ሕግ')
itembtn2 = types.KeyboardButton(u'/start')
menu2.add(itembtn1, itembtn2)

menu3 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ሁለተኛው ሕግ')
itembtn2 = types.KeyboardButton(u'/start')
menu3.add(itembtn1, itembtn2)

menu4 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ሦስተኛው ሕግ')
itembtn2 = types.KeyboardButton(u'/start')
menu4.add(itembtn1, itembtn2)

menu5 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'አራተኛው ሕግ')
itembtn2 = types.KeyboardButton(u'/start')
menu5.add(itembtn1, itembtn2)

menu6 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'አዎ')
itembtn2 = types.KeyboardButton(u'ላስብ')
itembtn3 = types.KeyboardButton(u'ከዚህ በፊት ፀልያለሁ')
itembtn4 = types.KeyboardButton(u'/start')
menu6.add(itembtn1,itembtn2,itembtn3, itembtn4)


menu7 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ኢየሱስ ለምን ሞተ?')
itembtn2 = types.KeyboardButton(u'እግዚአብሔር ፀሎት ይመልሳልን?')
itembtn3 = types.KeyboardButton(u'መንግሥተ ሰማይ ምን ትመስላለች ?')
itembtn4 = types.KeyboardButton(u'የፍቅር ግንኙነት ?')
itembtn5 = types.KeyboardButton(u'የሕይወቴ ዓላማ ምንድነው?')
itembtn6 = types.KeyboardButton(u'/start')
menu7.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6)

intro_markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'ስለ ክርስቶስ ከዚህ በፊት አልሰማሁም')
itembtn2 = types.KeyboardButton(u'ስለ ክርስቶስ ከዚህ በፊት ሰምቻለሁ')
itembtn3 = types.KeyboardButton(u'ስለ ክርስቶስ ተጨማሪ መረጃዎች')
itembtn4 = types.KeyboardButton(u'/start')
intro_markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

non_believer_markup1 = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton(u'እግዚአብሔርን ፍቅር በግል ማወቅ')
non_believer_markup1.add(itembtn1, itembtn2, itembtn3)

text_messages = {'welcome':u'እንካን ወደ አጋፔ መጡ!\n\nየእግዚአብሔርን ፍቅር በግል ማወቅ! '
                           u'\n\nየእግዚአብሔርን ፍቅር በግል ለማወቅ ምን ያስፈልግሀል? የመብረቅ ብልጭታ? ጥብቅ ኃይማኖታዊ ስርዓት? የተሻልክ '
                           u'ሰው ሆኖ መገኘት? አንዳቸውም እነደ ቅደመ ሆኔታ አያስፈልጉህም፡፡ እግዚአብሔር እርሱን ለማወቅ የሚያስፈልገንን '
                           u'መፅሐፍ ቅዱስ ላይ በግልፅ አስቀምጦልናል፡፡ ማንኛውም ነገር ደንብና ስርዓት አለው፡፡ ሰው የሠራቸው ነገሮች ሰው '
                           u'ሰራሽ ስርዓት እንዳላቸው ሁሉ እግዚአብሔር የፈጠራቸው ነገሮች ደግም የተፈጥሮ ሕግጋት አሏቸው፡፡እነዲሁም ሰው '
                           u'ከእግዚአብሔር ጋር የሚኖረውን ግንኙነት የሚወስኑ አራት መንፈሳዊ ሕጎች አሉ፡፡ መርሆች ብለህም ልትወስዳቸው ትችላለህ፡፡ '
                           u'\nይህን ማወቅ ትፈልጋለህ ?',

                 # introduction
                 'step0':u'እነዲሁም ሰው ከእግዚአብሔር ጋር የሚኖረውን ግንኙነት የሚወስኑ አራት መንፈሳዊ ሕጎች አሉ፡፡ መርሆች ብለህም ልትወስዳቸው ትችላለህ፡፡'
                         u'እነኚህም ህጎች አራት ናቸው የመጀመሪያውን እንመልከት',
                 # 4laws
                 'step1':u'የመጀመርያው ሕግ '
                         u'\n\nእግዚአብሔር ይወድሃል ስለዚህም ለሕይወትህ አስደናቂ ዕቅድ አዘጋጅቶልሃል፡፡'
                         u'የእግዚአብሔር ፍቅር “በእርሱ የሚያምን ሁሉ የዘላለም ሕይወት እንዲኖረው እንጂ እንዳይጠፋ እግዚአብሔር አንድያ ልጁን '
                         u'እስኪሰጥ ድረስ አለሙን እንዲሁ ወዶአልና፡፡”(ዮሐ 3፡16) '
                         u'የእግዚአብሔር ዕቅድ ክርስቶስ እንዲህ አለ፡- “እኔ ሕይወት እንዲሆንላቸው እንዲበዛላቸውም መጣሁ፡፡”(ዮሐ 10፡10) '
                         u'ነገር ግን ሰዎች ሁሉ ይህንን መሉና አርኪ ሕይወት አልተለማመዱም ምክንያቱን በ ሁለተኛው ሕግ ያገኙታል።',
                 'step2':u'ሁለተኛው ሕግ '
                         u'\n\nሰው ኃጢአተኛ ነው፡፡ በዚህም ምክንያት ከእግዚአብሔር ተለይቷል፡፡ ስለዚህም የእግዚአብሔርን ፍቅርና ዕቅድ ማወቅና በሕይወቱ መለማመድ አይችልም፡፡'
                         u'ሰው ኃጥአተኛ ነው “ሁሉ ኃጢአትን ሠርተዋልና የእግዚአብሔርም ክብር ጎድሎአቸዋል፡፡”(ሮሜ 3፡23) እግዚአብሔር ሰውን ሲፈጥረው ከእርሱ ጋር የቀረበ ግንኙነት '
                         u'በመመስረት በደስታ እንዲኖር ነበር፡፡ነገር ግን ሰው በራሱ መንገድ ለመጓዝ በመምረጡ ግንኙነታቸው ተቋረጠ፡፡ በራሳችን መንገድ ስንጓዝ ለእግዚአብሔር የማንታዘዝና '
                         u'ለርሱም ግድ የሌለን እንሆናለን፡፡ መጽሐፍ ቅዱስ ይህን አይነቱን አስተሳሰብ ነው ኃጢአት ብሎ የሚጠራው፡፡ '
                         u'“እኛ ሁላችን እንደ በጎች ተቅበዝብዘን ጠፋን ከእኛ እያንዳንዱ ወደ ገዛ መንገዱ አዘነበለ፡፡”(ኢሳ 53፡6) ሰው ከእግዚአብሔር ተለይቷል ሰዎች '
                         u'“የኃጢአት ደመወዝ ሞት ነውና” (ሮሜ 6፡23) ይህም ሞት በመንፈስ ከእግዚአብሔር መለየት ማለት ነው፡፡',
                 'step21':u'ይህ ስዕል የሚያሳው እግዚአብሔር ቅዱስ ሰው ደግሞ ኃጢአተኛ በመሆኑ በመካከላቸው ትልቅ መለያየት መኖሩን ነው፡፡ ቀስቶቹ የሚያመለክቱት ሰው በራሱ መንገድ ወደ እግዚአብሔር ለመድረስ እንዴት እንደሚጥር ነው፡፡'
                          u' ለምሳሌ፡- የሃይማኖት ስርአቶችን በመፈፀም፣ ቤተክርስትያን ሳያቋርጥ በመመላለስ፣ መልካምን ስራ በመስራት፣ ሰውን ባለመጉዳት፣ወ.ዘ.ተ. ነገር ግን ሰውን ጥረቱ ወደ እግዚአብሔር ሊያቀርበው አልቻለም፡፡',
                 'step3':u'ሦስተኛው ሕግ '
                         u'\n\nሰው ወደ እግዚአብሔር ሊደርስ የሚችልበት ብቸኛው መንገድ ኢየሱስ ክርስቶስ ነው፡፡ እርሱ ስለ እኛ ሞቷል፡፡ ስለዚህም ሰው በእርሱ በኩል '
                         u'የእግዚአብሔርን ፍቅርና ዕቅድ ሊያውቅና ሊለማመድ ይችላል፡፡ እርሱ በእኛ ምትክ ሞተ ‹‹ነገር ግን ገና ኃጢያተኞች ሳለን ክርስቶስ ስለ እኛ ሞቷልና እግዚአብሔር ለእኛ ያለውን የራሱን ፍቅር ያስረዳል፡፡›› (ሮሜ. 5፡8) '
                         u'ከሞት ተነስቷል ‹‹…ክርስቶስ ስለ ኃጢያታችን ሞተ ተቀበረም መጽሐፍ እንደሚል በሦስተኛው ቀን ተነሣ፣ …›› (1ኛ ቆሮ. 15፡3-5) እርሱ ብቸኛ መንገድ ነው፡:'
                         u'\nኢየሱስ እንዲህ አለ፡- ‹‹እኔ መንገድና እውነት ሕይወትም ነኝ በእኔ በቀር ወደ አብ የሚመጣ የለም›› (ዩሐ› 14፡6)',
                 'step31':u'ይህ ስዕል የሚያሳየው እኛን ወደ ራሱ ሊመልሰን የሚችለው እግዚአብሔር ብቻ መሆኑን ነው፡፡ ይህንንም ልጁን ኢየሱስ ክርስቶስን በመስቀል ላይ ስለእኛ እንዲሞት በመላክ ፈጽሞታል፡፡ '
                          u'ከዚህም የተነሳ ሁላችንም በእርሱ በኩል ወደ እግዚአብሔር መድረስ እንችላለን፡፡ ነገር ግን እነዚህን ሦስት ሕጎች ብቻ ማወቅ በቂ አይደለም . . .'
                          u'ለክቱት ሰው በራሱ መንገድ ወደ እግዚአብሔር ለመድረስ እንዴት እንደሚጥር ነው፡፡ ለምሳሌ፡- የሃይማኖት ስርአቶችን በመፈፀም፣ ቤተክርስትያን ሳያቋርጥ በመመላለስ፣ መልካምን ስራ በመስራት፣ '
                          u'ሰውን ባለመጉዳት፣ወ.ዘ.ተ. ነገር ግን ሰውን ጥረቱ ወደ እግዚአብሔር ሊያቀርበው አልቻለም፡፡አራተኛው ህግ ሰው ወደ እግዚአብሔር የሚደርስበትን ብቸኛ ሕግ ያሳየናል . . .',
                 'step4':u'አራተኛው ሕግ '
                         u'\n\nእያንዳንዳችን ኢየሱስ ክርስቶስን እንደ አዳኛችንና እንደ ጌታችን ልንቀበለው ይገባናል፡፡ ከዚያም የእግዚአብሔርን ፍቅርና ዕቅድ በሕይወታችን ልናውቅና '
                         u'ልንለማመድ እንችላለን፡፡ ክርስቶስን ልንቀበለው ይገባናል ‹‹ለተቀበሉት ሁሉ ግን በስሙ ለሚያምኑ ለእነርሱ የእግዚአብሔር ልጆች ይሆኑ ዘንድ ሥልጣንን ሰጣቸው››(ዩሐ.1፡12) ክርስቶስን በእምነት ልንቀበለው ይገባል '
                         u'‹‹ጸጋው በእምነት አድኖአችኋልና፤ ይህም የእግዚአብሔር ስጦታ ነው እንጂ ከእናንተ አይደለም ማንም እንዳይመካ ከሥራ አይደለም›› (ኤፌ. 2፡8-9)፡፡ በግላችን ክርስቶስን ወደ ሕይወታችን በመጋበዝ ልንቀበለው ይገባል'
                         u'\nክርስቶስ እንዲህ ይላል፡- ‹‹እነሆ በደጅ ቆሜ አንኳኳለሁ ማንም ድምጼን ቢሰማ ደጁንም ቢከፍትልኝ ወደ እርሱ እገባለሁ ከእርሱም ጋር እራት እበላለሁ እርሱም ከእኔ ጋር ይበላል›› (ራዕ. 3፡20)'
                         u'\nክርስቶስን መቀበል የሚከተሉትን ያጠቃልላል'
                         u'\n\t- ኃጢያተኛ መሆናችንን ማወቅና ከኃጢያታችን ለመመለስ በመወሰን ከእግዚአብሔር ጋር መስማማት'
                         u'\n\t- ኢየሱስ ክርስቶስ ኃጢያታችንን ይቅር እንደሚልና ወደ ሕይወታችንም እንደሚመጣ ማመን'
                         u'\n\t- ክርስቶስ በእኛ ውስጥ እንዲኖር መፍቀድና እርሱን ማሳየት'
                         u'\እነዚህ ሁለት ክቦች ሁለት አይነት ሕይወት ይወክላሉ፡፡',
                 'step41':u'በእኔነት ቁጥጥር ስር ያለ ሕይወት ይህ ሰው የራሱን ሕይወት የሚቆጣጠረው ራሱ ነው፡፡ ክርስቶስ እስከ አሁንም ድረስ ከሕይወቱ ውጪ ነው ሕይወቱን '
                          u'በተለያየ አቅጣጫ የሚመራው ራሱ ነው ውጤቱም ከእግዚአብሔር ጋር ሰላም ማጣት ነው፡፡',
                 'step42':u'በክርስቶስ ቁጥጥር ያለ ሕይወት የዚህ ሰው ሕይወት ተቆጣጣሪ ክርስቶስ ነው፡፡ በማንኛውም አቅጣጫ ክርስቶስ ሕይወቱን እንዲቆጣጠርለት ፈቅዷል ውጤቱም ከእግዚአብሔር ጋር ሰላም መፍጠር ነው፡፡'
                          u'\n\t\t- የትኛው ክብ ሕይወትህን ይወክላል?'
                          u'\n\t\t- ሕይወትህ የትኛውን ክብ እንዲመስል ትፈልጋለህ?',
                 'step5':u'ፈቃደኛ ሆነህ አሁኑኑ ብትፀልይ በሰጠው ተስፋ መሰረት ክርስቶስ ወደ ሕይወትህ ይመጣል፡፡\n\nይህን ፀሎት ልትፀልይ ትወዳለህን? '
                         u'\n\nእንዲህ ልትፀልይ ትችላለህ '
                         u'\n\n‹‹ጌታ ኢየሱስ ሆይ፣ አንተን በግሌ ለማወቅ እፈልጋለሁ፡፡ ስለ ኃጢያቴ በመስቀል ላይ ስለሞትክልኝ አመሰግንሃለሁ፡፡ አሁን ልቤን ከፍቼ አዳኜና ጌታዬ አድርጌ እቀበልሃለሁ፡፡ '
                         u'ኃጢያቴን ሁሉ ይቅር ስላልከኝና የዘላለም ሕይወት ስለሰጠኸኝ አመሰግንሃለሁ፤፤ በሕይወቴ ዙፋን ላይ ሆነህ ግዛኝ አንተ የምትፈልገው ዓይነት ሰው አድርገኝ፡፡ አሜን!››',

                 # Tips and Articles
                 'stept':u'ለህይወቶ ጠቃሚ የሆኑ መረጃዎችን እንስጥዎ ። ክታች ከተዘረዘሩት ይምረጡ ',
                 'stepa1':u'ኢየሱስ ሞትን የመረጠበትን ሁኔታ ስንመለከት አንድ ሰው ራሱን ሊያድን የሚችልበት አቅም እያለው ግን ሆን ብሎ ራሱን በውሃ ውስጥ በመዝፈቅ ሰጥሞ መሞትን ምርጫው የማድረግ አይነት ነው፡፡\n'
u'በዚህ ረገድ ኢየሱስ ዓላማው ግልፅ ነው፡፡ ለእኛ ሲልም ነፍሱን አሳልፎ መስጠትን እንደመረጠም ኢየሱስ እንዲህ ሲል ተናግሯል “ነፍሱን ስለ ወዳጆቹ ከመስጠት ከዚህ የሚበልጥ ፍቅር ለማንም የለውም፡፡'
u'ምክንያቱም ልባችንን ሲያይ፣ ድርጊታችንን ሲመለከት፣ ህመምተኞች፣ የተቸገርን፣ ደካሞች፣ ኃጢአተኞች፣ የታወርን እና የጠፋን ነበርን፡፡ ምንም ባንወድደውም፣ ኢየሱስ ስለ እኛ የሚመለከተው ይህንን ነው፡፡ ይህንን ብቻ ሳይሆን እኛም ደግሞ ስለነዚያ ነገሮች እርሱ ያደረገልንንም እንድንመለከት ያሻል፡፡ እርሱ ድካማችንን አይቶ፣ በሩቅ ቆሞ አልፈረደብንም ወይንም አልረገመንም፡፡ እንደገባችሁ ተወጡት አይመለከተኝም አላለምም ወይንም ችግራችን የማይገባው አልሆነም፡፡ ከእርሱ ጋር ተስማማችሁም አልተስማማችሁም እጅግ ረዳት የሚያስፈልገን ሆነን ይመለከተናል፡፡ እርሱ ለእኛ ያዘጋጀውንም መልካምነት በሙላት መኖር የማንችል፣ ሕይወታችንም የተመሰቃቀለ ሆኖ ይመለከተናል፡፡'
u'ከዚህም ሁሉ ባሻገር፣ በዘላለምም ሞት ከእርሱ ተለይተን በመኖር፣ የዘላለምን ሕይወት ጨርሶውኑ ባለመለማመድ አደጋም ውስጥ ሆነን ያየናል፡፡ በኃጢአታችንም ምክንያት ከእርሱ ተቆርጠን ያየናል፡፡ ስለዚህም (ሞትን በመምረጡ) አነዚህን ሁሉ መሻቶቻችንን ሊያሟላልን ወደደ፡፡'
u'ይህን ሙሉ ፅሁፍ ለማግኘት ይህን ሊንክ ይመልከቱ ። ',
                 'stepa2':u'ለሚያውቁትና ለሚደገፉበት ጌታ ኢየሱስ በሥጦታው ባለጠጋ ነው፡፡ "በእኔ ብትኖሩ፤ ቃሎቼም በእናንተ ቢኖሩ፤ የምትፈልጉትን ማነኘውም ነገር ለምኑ ይሰጣችሁል"( ዮሐ 15፡7)፡፡ '
                          u'በእርሱ መኖርና በቃሉ መኖር ማለት በእግዚአብሔር እውቅና ውስጥ ህይወትን መምራት፤ በእሱ ላይ ራስን መጣል እና እሱ የሚለውን መስማት ማለት ነው፡፡ ይህ ሲሆን ሰው የሚፈልገውን ሁሉ እግዚአብሔርን እንዲጠይቅ ያስችለዋል፡፡'
                          u' እንዲሁም፡ “ በእገዚአብሔር ፊት ለመቅረብ ያለን ድፍረት ይህ ነው፤ ማንኛውም ነገር እነደፈቃዱ ብንለምን እርሱ ይሰማናል፤የምንለምነውን ሁሉ እነደሚሰማን ካወቅን፤ የለመነውንም ነገር እነደተቀበልን እናውቃለን፡:”(1ዮሐ 5፡14) '
                          u'እግዚአብሔር እንደ ፍቃዱ፤እንደ ጥበቡ፤ እንደ ፃድቅነቱ እና እንደ ፍቅሩ የሆነውን ፀሎታችንን ይመልሳል፡'
                          u'ይህን ሙሉ ፅሁፍ ለማግኘት ይህን ሊንክ ይመልከቱ ። http://habeshastudent.com/a/prayers.html' ,
                 'stepa3':u'ብዙ ሰዎች መንግሥተ ሰማይ ብለው የሚጠሯት ዘላለማዊዋን ከተማ ነው። መጽሐፍ ቅዱስ «አዲሲቷ ኢየሩሳሌም» (ራዕይ 21፥2) ብሎ የሚጠራት ማለት ነው። '
                          u'ዘላለማዊቷ ከተማ የተገለጸችው እንዲህ ተብላ ነው። « እነሆ የእግዚአብሔር ድንኳን በሰዎች መካከል ነው ፤ ከእነርሱም ጋር ያድራል። እነርሱም ሕዝቡ ይሆናሉ። እግዚአብሔርም እርሱ ራሱ ከእነርሱ ጋር ሆኖ አምላካቸው ይሆናል። '
                          u'እንባዎችንም ሁሉ ከአይኖቻቸው ያብሳል። ሞትም ከእንግዲህ ወዲህ አይሆንም ፥ ኃዘንም ቢሆን ወይም ጩኸት ወይም ሥቃይ ከእንግዲህ ወዲህ አይሆንም፤ የቀደመው ሥርአት አልፎአልና። ብሎ ሲናገር ሰማሁ። '
                          u'በዙፋንም የተቀመጠው ፡- እነሆ ሁሉን አዲስ አደርጋለሁ አለ፤ ለእኔም እነዚህ ቃሎች የታመኑና እውነተኛዎች ናቸውና ጻፍ አለኝ ። » ራዕይ 21፥ 3-5  '
                          u'ይህን ሙሉ ፅሁፍ ለማግኘት ይህን ሊንክ ይመልከቱ ።http://habeshastudent.com/a/heaven.html',
                 'stepa4':u'እኛ በእግዚአብሔር አምሳል የተፈጠርነው ከእግዚአብሔር ጋር ገንኙነት እንዲኖረን ነው። '
                          u'በዚህች ምድር ላይ ነፍሳችንን የሚያረካው፣ ብቸኛውና ዘላቂው መፍትሄ ከእግዚአብሔር ጋር ግንኙነት አንዲኖረን ማድረግ ነው። '
                          u'የሚገርመው ግን እግዚአብሔርን እስከምናውቀው ድረስ ሕይወታችን የተፈጠረችበትን ዓላማ በመፈለግ ሂደት ውስጥ እጅግ በጣም አስገራሚ በሆኑ ልምምዶች ውስጥ እንደምናልፍ ሳይታለም የተፈታ ነው።'
                          u' ልክ መዶሻው የተፈጠረበትን ምስማር የመምታት ዓላማ ዕድሉን ከማግኘቱ በፊት እንዳለፋቸው ሂደቶች እኛም የተፈጠርንበትን ዓላማ ሳናውቅና ሳናገኝ እንዲሁ በመባዘን እንዳለፍን ግልጽ ነው።'
                          u' እጅግ በጣም የተከበሩ በምንላቸው ዓላማዎች ዙሪያ ራሳችንን አግኝተን ሊሆን ይችላል፣ ቢሆንም የተከበሩ ዓላማዎች መስለውን ቢታዩንም ከተፈጠርንበት ዓላማ ጋር የማይሄዱና ፈጽሞ እርካታን የማናገኘባቸው ሊሆኑ ይችላሉ። '
                          u'ቅዱስ አውግስጦስ ይህን ዕውነታ እንዲህ ብሎ በድንቅ አገላለጽ አቅርቦታል፤ «እግዚአብሔር ሆይ አንተ ለራስህ ክብር ፈጠርኸን፤ ስለዚህ ነፍሳችን አንተን አግኝታ እስከምታርፍ ጊዜ ድረስ መቼም ቢሆን እፎይ አትልም፡፡» አለ።'
                          u'ይህን ሙሉ ፅሁፍ ለማግኘት ይህን ሊንክ ይመልከቱ ። http://habeshastudent.com/a/purpose.html',
                 'stepa5':u'እንደባልና እንደአባት ከሰዎች ጋራ ጥሩ ግንኙነቶችን መፍጠር ከፈለግህ መሥራት ልትጀምርበት የሚገባህ ጥሩ ስፍራ ቢኖር አንተው ራስህ ጋ ነው! '
                          u'ምስጢሩ ትክክለኛ ሚስት ለማግኘት ወይንም ትክክለኛ የሆኑ ልጆችን ለማፍራት ቆርጦ መነሳት አይደለም፡፡ ይልቁንም ቁልፉ ከራስህ መጀመር ነው፡፡ '
                          u'አንተን ጥሩ ባልና አባት ሊያደርግህ የሚችል በጣም ወሳኝ የሆነ ግንኙነት ቢኖር ከእግዚአብሔር ጋራ ያለው ግንኙነትህ ነው፡፡ ለሴትም ልክ እንዲሁ ከእግዚአብሔር ጋራ ያለው ግንኙነትሽ ወሳኝ ነው። እግዚአብሔር የወሲብ፣ የፍቅርና የግንኙነቶች ሁሉ ፈጣሪ ነው፡፡እንድንደሰትባቸው ብሎ የፈጠረልን ነገሮች ናቸው፡፡ስለአጠቃቀማቸው እርሱ ያወጣልንን ስርዓት ከተከተልን በሚገባ እንደሰትባቸዋለን፡፡'
                          u'አንድ የተረዳሁት ነገር ቢኖር እግዚአብሔር የሞራል አስከባሪ በመሆን ‹‹ይህን አድርግ፣ ይህን አታድርግ!›› እያለ አለቃ ወይንም መሪ መሆኑን ለማሳየት የሚሞክር አለመሆኑን ነው፡፡ '
                          u'ለምሳሌ ያህል ‹‹ከጋብቻ በፊት ወሲብን አትፈጽም! ›› ሲል ለራሴ ጥቅም ብሎ ነው፡፡ እርሱ ራሱ ስለሰራኝ ለእኔ የተሻለውንና የተሟላ ደስታ ሊሠጠኝ የሚችለውን ነገር ጠንቅቆ ያውቃል፡፡'
                          u'ይህን ሙሉ ፅሁፍ ለማግኘት ይህን ሊንክ ይመልከቱ ። http://habeshastudent.com/a/wolves.html',
                 'stepa6':u'',
                 'stepa':u'',


                 }

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text_messages['welcome'], reply_markup=menu1)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    replay_send(message)

def replay_send(message):
    if(message.text == 'help'):
        bot.send_message(message.chat.id, text_messages['welcome'], reply_markup=menu1)
    elif(message.text == u"ስለ ክርስቶስ ከዚህ በፊት አልሰማሁም"):
        bot.send_message(message.chat.id, text_messages['step0'], reply_markup=non_believer_markup1)
    elif (message.text == u"የእግዚአብሔርን ፍቅር  በግል እየተለማመድኩ ነው"):
        bot.send_message(message.chat.id, text_messages['stept'], reply_markup=menu7)
    elif (message.text == u"ስለ ክርስቶስ ተጨማሪ መረጃዎች እንስጥዎ"):
        bot.send_message(message.chat.id, text_messages['stept'], reply_markup=menu7)
    elif (message.text == u"ኢየሱስ ለምን ሞተ?"):
        bot.send_message(message.chat.id, text_messages['stepa1'], reply_markup=menu7)
        bot.send_message(message.chat.id, "http://habeshastudent.com/a/whydid.html")
    elif (message.text == u"እግዚአብሔር ፀሎት ይመልሳልን?"):
        bot.send_message(message.chat.id, text_messages['stepa2'], reply_markup=menu7)
        bot.send_message(message.chat.id, "http://habeshastudent.com/a/prayers.html")
    elif (message.text == u"መንግሥተ ሰማይ ምን ትመስላለች ?"):
        bot.send_message(message.chat.id, text_messages['stepa3'], reply_markup=menu7)
        bot.send_message(message.chat.id, "http://habeshastudent.com/a/heaven.html")
    elif (message.text == u"የፍቅር ግንኙነት"):
        bot.send_message(message.chat.id, text_messages['stepa4'], reply_markup=menu7)
        bot.send_message(message.chat.id, "http://habeshastudent.com/a/wolves.html")
    elif (message.text == u"የሕይወቴ ዓላማ ምንድነው?"):
        bot.send_message(message.chat.id, text_messages['stepa5'], reply_markup=menu7)
        bot.send_message(message.chat.id, "http://habeshastudent.com/a/purpose.html")
    elif(message.text == u"ማወቅ ፈልጋለሁ"):
        bot.send_message(message.chat.id, text_messages['step0'], reply_markup=menu2)
    elif (message.text == u"የመጀመርያው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step1'], reply_markup=menu3)
    elif (message.text == u"ሁለተኛው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step2'], reply_markup=menu4)
        photo = open('images/low2.png', 'rb')
        bot.send_photo(message.chat.id,photo)
        bot.send_message(message.chat.id, text_messages['step21'], reply_markup=menu4)
    elif (message.text == u"ሦስተኛው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step3'], reply_markup=menu5)
        photo = open('images/low3.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, text_messages['step31'], reply_markup=menu5)
    elif (message.text == u"አራተኛው ሕግ"):
        bot.send_message(message.chat.id, text_messages['step4'], reply_markup=menu1)
        photo = open('images/low41.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, text_messages['step41'], reply_markup=menu1)
        photo = open('images/low42.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, text_messages['step42'], reply_markup=menu6)
        bot.send_message(message.chat.id, text_messages['step5'], reply_markup=menu6)
        audio = open('audios/salivation.mp3','rb')
        bot.send_audio(message.chat.id,audio)
        bot.send_audio(message.chat.id, "FILEID")
    elif (message.text == u"አጭር ፊልም ይመልከቱ"):
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=KGlx11BxF24", reply_markup=menu1)
    elif (message.text == "song2"):
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=BZrGJXBB3jc", reply_markup=intro_markup)
    else:
        bot.send_message(message.chat.id, message.text, reply_markup=intro_markup)
        # bot.send_photo()


bot.polling()
