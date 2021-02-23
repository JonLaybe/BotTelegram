import telebot
from telebot import types

bot = telebot.TeleBot('1154559920:AAFtqPDS2P-nVpM4Xae1HYjo6bju4Vf3dKI')

Error_M = ['/start', '/list', '/appraisals', '/notes']

Admin_Consl = [1396069883]

### list
list_id = []
list_grup = []
list_class = ['171к']
###
Not_id = []#id user
Not_Name = []#название not
Not = []#not
### appraisals
FFid = []
FFG = []
###news
Admin_News = []
Nwes_Time = []
News_Name = ['Привет', 'Каки дела?', 'Что нового!']
News = ['Хай!', 'Хорошо!', 'Ни чего!']
###
consl_user = []
###

###key
@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    ###Not
    if call.data == 'add_mod':
        bot.send_message(call.message.chat.id, 'Напишите название заметки!')
        bot.register_next_step_handler(call.message, add_mod)
    if call.data == 'change_mod':
        if id_user in Not_id:
            bot.send_message(call.message.chat.id, 'Введите изменение!')
            bot.register_next_step_handler(call.message, change_mod)
    if call.data == 'del_mod':
        if messageText in Error_M:
            return Error
        join = Not_id.index(id_user)
        scoreJoin = len(Not_Name[join])
        if scoreJoin > 1:
            join = Not_id.index(id_user)
            Not_M = Not_Name[join]
            join_M = Not_M.index(messageText)
            Git_Not = Not[join]
            del Not_M[join_M]
            del Git_Not[join_M]
            bot.send_message(call.message.chat.id, '✓')
        else:
            join = Not_id.index(id_user)
            del Not_id[join]
            del Not_Name[join]
            del Not[join]
            bot.send_message(call.message.chat.id, '✓')
    ###appraisals
    if call.data == 'change':
        if id_user in FFid:
            join = FFid.index(id_user)
            M_FFG = FFG[join]
            bot.send_message(call.message.chat.id, M_FFG)
            bot.send_message(call.message.chat.id, 'Введите изменение!')
            bot.register_next_step_handler(call.message, change)
    if call.data == 'del':
        if id_user in FFid:
            join = FFid.index(id_user)
            del FFG[join]
            del FFid[join]
            bot.send_message(call.message.chat.id, '✓')
    ###News
    if call.data == 'add_news':
        bot.send_message(call.message.chat.id, 'Напишите название статьи!')
        bot.register_next_step_handler(call.message, add_NewsName)
    if call.data == 'change_news':
        bot.send_message(call.message.chat.id, 'Введите изменение!')
        bot.send_message(call.message.chat.id, join_News)
        bot.register_next_step_handler(call.message, change_news_mod)

###
def Error():
    if message.text == '/start':
        bot.register_next_step_handler(message, start_message)
    if message.text == '/list':
        bot.register_next_step_handler(message, list)
    if message.text == '/appraisals':
        bot.register_next_step_handler(message, appraisals)
### start
@bot.message_handler(commands=['start'])
def start_message(message):
    id_user = message.from_user.id
    if id_user in Admin_Consl:
        bot.send_message(message.chat.id, f'Привет, создатель! Ваш id:{id_user}!')
        global user
        user = 0
    else:
        user += 1
        bot.send_message(message.chat.id, f'Привет, я бот! Ваш id:{id_user}!')

### list
@bot.message_handler(commands=['list'])
def list(message):
    id_user = message.from_user.id
    if id_user in list_id:
        id_user = message.from_user.id
        join = list_id.index(id_user)
        list_M = list_grup[join]
        var = open(list_M+'.txt')
        f = var.read()
        bot.send_message(message.chat.id, f)
    else:
        bot.send_message(message.chat.id, 'В list вы можиите смотреть расписание свой группы!\nВыберите вашу греппу:')
        bot.send_message(message.chat.id, list_class)
        bot.register_next_step_handler(message, grup)

def grup(message):
    if isinstance(message.text, str):
        if message.text in list_class:
            id_user = message.from_user.id
            list_id.append(id_user)
            list_grup.append(message.text)
            id_user = message.from_user.id
            join = list_id.index(id_user)
            list_M = list_grup[join]
            var = open(list_M+'.txt')
            f = var.read()
            bot.send_message(message.chat.id, f)
        else:
            bot.send_message(message.chat.id, 'Я не нашел вашей грппы!')
### notes
@bot.message_handler(commands=['notes'])
def notes(message):
    global id_user
    id_user = message.from_user.id
    if id_user in Not_id:
        join = Not_id.index(id_user)
        Not_M = Not_Name[join]
        str1 = '; '.join(Not_M)
        bot.send_message(message.chat.id, 'Ваши заметки:')
        bot.send_message(message.chat.id, str1)
        bot.register_next_step_handler(message, mod_sea)
    else:
        bot.send_message(message.chat.id, 'Напишите название заметки!')
        bot.register_next_step_handler(message, mod_key)

def mod_key(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        id_sure = message.from_user.id
        Not_id.append(id_sure)
        Not_Name.append([message.text])
        bot.send_message(message.chat.id, 'Напишите заметку!')
        bot.register_next_step_handler(message, mod_notes)

def mod_notes(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        Not.append([message.text])
        bot.send_message(message.chat.id, '✓')
    else:
        print('Я вас не понял!')

def mod_sea(message):
    global messageText
    messageText = message.text
    id_user = message.from_user.id
    join = Not_id.index(id_user)
    Not_M = Not_Name[join]
    if message.text in Not_M:
        join = Not_id.index(id_user)
        Not_M = Not_Name[join]
        Not_M = Not_M.index(message.text)
        Git_Not = Not[join]
        Not_M = Git_Not[Not_M]
        keyboarde = types.InlineKeyboardMarkup()
        key_add_mod = types.InlineKeyboardButton(text = 'Новая заметка', callback_data = 'add_mod')
        key_remuve_mod = types.InlineKeyboardButton(text = 'Изменить', callback_data = 'change_mod')
        key_del_mod = types.InlineKeyboardButton(text = 'Удалить', callback_data = 'del_mod')
        keyboarde.add(key_add_mod)
        keyboarde.add(key_remuve_mod)
        keyboarde.add(key_del_mod)
        bot.send_message(message.chat.id, Not_M, reply_markup = keyboarde)
    else:
        bot.send_message(message.chat.id, 'Такой заметки нет!')

def add_mod(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        id_user = message.from_user.id
        if id_user in Not_id:
            join = Not_id.index(id_user)
            Not_M = Not_Name[join]
            Not_M.append(message.text)
            bot.send_message(message.chat.id, 'Напишите заметку!')
            bot.register_next_step_handler(message, add_mod_a)

def add_mod_a(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        id_user = message.from_user.id
        if id_user in Not_id:
            join = Not_id.index(id_user)
            Not_M = Not[join]
            Not_M.append(message.text)
            bot.send_message(message.chat.id, '✓')

def change_mod(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        id_user = message.from_user.id
        join = Not_id.index(id_user)
        Not_M = Not_Name[join]
        Not_M = Not_M.index(messageText)
        Git_Not = Not[join]
        Git_Not[Not_M] = (message.text)
        bot.send_message(message.chat.id, '✓')

### appraisals
@bot.message_handler(commands=['appraisals'])
def appraisals(message):
    global id_user
    id_user = message.from_user.id
    if id_user in FFid:
        join = FFid.index(id_user)
        M_FFG = FFG[join]
        keyboard = types.InlineKeyboardMarkup()
        key_remuve = types.InlineKeyboardButton(text = 'Изменить', callback_data = 'change')
        key_del = types.InlineKeyboardButton(text = 'Удалить', callback_data = 'del')
        keyboard.add(key_remuve)
        keyboard.add(key_del)
        bot.send_message(message.chat.id, M_FFG, reply_markup = keyboard)
    else:
        qwest = 'Это журнал в котором ты можешь отслежитавть свои оценки!\nНапиши предметы и оценки!\nПредмет: оценки' 
        bot.send_message(message.chat.id, qwest)
        bot.register_next_step_handler(message, prass)

def change(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        id_user = message.from_user.id
        if id_user in FFid:
            join = FFid.index(id_user)
            FFG[join] = (message.text)
            bot.send_message(message.chat.id, '✓')

def prass(message):
    if message.text in Error_M:
        return Error
    if isinstance(message.text, str):
        id_sure = message.from_user.id
        FFid.append(id_sure)
        print(FFid)
        FFG.append(message.text)
        bot.send_message(message.chat.id, '✓')

###news
@bot.message_handler(commands=['news'])
def news(message):
    id_user = message.from_user.id
    if id_user in Admin_News:
        lenNameNews = len(News_Name)
        if lenNameNews > 0:
            str1 = '; '.join(News_Name)
            bot.send_message(message.chat.id, 'Выберите статью:')
            bot.send_message(message.chat.id, str1)
            bot.register_next_step_handler(message, NewsMessage)
        else:
            bot.send_message(message.chat.id, 'News - раздел в котором вы можете написать статью!')
            bot.send_message(message.chat.id, 'Напишите название статьи!')
            bot.register_next_step_handler(message, add_NewsName)
    else:
        scoreNewsName = len(News_Name)
        if scoreNewsName >= 1:
            LenNews = 0
            for i in News_Name:
                NewsName = ''.join(News_Name[LenNews])
                News_Naw = ''.join(News[LenNews])
                LenNews += 1
                messageNews = (f'{NewsName}\n----\n{News_Naw}')
                bot.send_message(message.chat.id, messageNews)
        else:
            bot.send_message(message.chat.id, 'Новостей пока нет!')

def NewsMessage(message):
    if message.text in News_Name:
        if isinstance(message.text, str):
            global join_News, join_NewsName
            join_NewsName = News_Name.index(message.text)
            join_News = News[join_NewsName]
            keyboarde = types.InlineKeyboardMarkup()
            key_add_news = types.InlineKeyboardButton(text = 'Создать навую статью!', callback_data = 'add_news')
            key_remuve_news = types.InlineKeyboardButton(text = 'Изменить', callback_data = 'change_news')
            keyboarde.add(key_add_news)
            keyboarde.add(key_remuve_news)
            bot.send_message(message.chat.id, join_News, reply_markup = keyboarde)
        else:
            bot.send_message(message.chat.id, 'Такой статьи нет!')

def add_NewsName(message):
    if isinstance(message.text, str):
        if message.text in News_Name:
            bot.send_message(message.chat.id, 'Название такой статьи уже существует!')
        else:
            News_Name.append(message.text)
            bot.send_message(message.chat.id, 'Напишите статью!')
            bot.register_next_step_handler(message, add_News)

def add_News(message):
    if isinstance(message.text, str):
        News.append(message.text)
        bot.send_message(message.chat.id, '✓')

def change_news_mod(message):
    if isinstance(message.text, str):
        News[join_NewsName] = (message.text)
        bot.send_message(message.chat.id, '✓')

### consl
@bot.message_handler(commands=['consl'])
def start_message(message):
    id_user = message.from_user.id
    if id_user in Admin_Consl:
        id_user_tg = (f'Учатников: {user}\nЖурналы: {FFG}\nЗаметки: {Not}')

        bot.send_message(message.chat.id, id_user_tg)
### eho
@bot.message_handler()
def eho(message):
    id_userFirst = message.from_user.first_name
    id_userLast = message.from_user.last_name
    print(f'{id_userFirst} {id_userLast}: {message.text}')
    bot.send_message(message.chat.id, 'Я вас не понял!')

### stert_bot
bot.polling()