import telebot


bot = telebot.TeleBot('715031522:AAHpH7B6TElSxMBKLqsM66_VdKR7QiN32F4')


@bot.message_handler(commands=['start'])
def handler_start1(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('✅Купить VNS дедик', '✅Купить VDS дедик')
    user_markup.row('Что такое дедики VNS и как ими пользоваться?',"Что такое дедики VDS и как ими пользоваться?")
    user_markup.row('Нужна помощь?🆘')
    send = bot.send_message(message.from_user.id, 'Добро пожаловать в чат-бот магазина по продаже дедиков VNS и VDS. По всем вопросам: @MrGob1 или @Derept', reply_markup=user_markup)
    bot.register_next_step_handler(send, second)

def second(message):
    if message.text == 'Нужна помощь?':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("<--Назад")
        keyboard.row("Я хочу вернуть дедик")
        send = bot.send_message(message.from_user.id, ' awfawf', reply_markup=keyboard)
        bot.register_next_step_handler(send, second1,)
def second1(message):
    if message.text == "<--Назад":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Купить VNS дедик', 'Купить VDS дедик')
        user_markup.row('Что такое дедики VNS и как ими пользоваться?',"Что такое дедики VDS и как ими пользоваться?")
        user_markup.row('Нужна помощь?')
        send = bot.send_message(message.from_user.id, 'Добро пожаловать в чат-бот магазина по продаже дедиков VNS и VDS. По всем вопросам: @MrGob1 или @Derept', reply_markup=user_markup)
        bot.register_next_step_handler(send, handler_start1)
#отправка смс
@bot.message_handler(content_types=['text'])
def handler_start(message):
    if message.text == "✅Купить VNS дедик":
        bot.send_message(message.chat.id, '''
        Покупка☑️

Оренда дедика на день = 5р
Заказать можна минимум на 3 дня!
--------------------------------
Тарифы:
3 дня = 15р
7 дней = 30р
31 день = 110р
--------------------------------
Выбор ОС:
1. Windows = 40р день
2. Linux (Debian) = 5р день
3. CentOS = 5р день
4. Debian = 5р день
5. FreeBSD = 5р день
6. BitrixVM = 40р день
--------------------------------
Покупайте через админа: @MrGob1 или @Derept ( Очеень шустро )
Скоро будет открыт наш сайт с магазином!''')
    elif message.text == "✅Купить VDS дедик":
        bot.send_message(message.chat.id, '''
Покупка☑️

Дедик работает от 3 дней до 1года!
Обично 25-30 дней стабильной держится ;)
----------------------------------------
Тарифы:
1 дедик = 55р
5 дедиков = 270р
Гарантия 3 дня
----------------------------------------
Покупайте через админа: @MrGob1 или @Derept ( Очеень шустро )
Скоро будет открыт наш сайт с магазином!


        ''')
    elif message.text == "Что такое дедики VNS и как ими пользоваться?":
        bot.send_message(message.chat.id, '''
        -------------------------------------------------------------------
Самый обичный дедик.. только полностю
через консоль и без GUI интерфейса (Если
что не ясно спроси: @MrGob1 или @Derept)
-------------------------------------------------------------------
''')
    elif message.text == "Что такое дедики VDS и как ими пользоваться?":
        bot.send_message(message.chat.id, '''
        -------------------------------------------------------------------
Стандартый дедик с GUI интерфесом и
обычной виндой (Если что не ясно
спроси:@MrGob1 или @Derept)
-------------------------------------------------------------------
''')
    elif message.text == "1":
        bot.send_message(message.chat.id, 'Пока что с данным вопрос поможет только админ:@MrGob1 или @Derept')
    elif message.text == "2":
        bot.send_message(message.chat.id, 'Пока что с данным вопрос поможет только админ:@MrGob1 или @Derept')
    elif message.text == "Нужна помощь?🆘":
        bot.send_message(message.chat.id, ''' Вопросы:
1) Я хочу вернуть дедик!
2) Дедик начал виснуть
3) Как подключиться к дедику?
4) Другой вопрос
Укажыте цыфру вопроса.''')
    elif message.text == "3":
        bot.send_message(message.chat.id, 'Подключиться к дедику можно с помошью встроеного в ОС windows утилиты: Подключение к удаленному рабочему столу. Пуск => Программы => Стандартные => Связь => Подключение к удаленному рабочему столу. Можно еще так: Пуск => Выполнить => mstsc. Еще одно утилита для подключение к дедику - это [BL4CK] VNC Viewer: Authentication Bypass. Просто запустите ее и вводите ip адрес дедика. Можно еще Радмином юзать дедик если он установлен на дедике.')
    elif message.text == "4":
        bot.send_message(message.chat.id, 'Пока что с данным вопрос поможет только админ:@MrGob1 или @Derept')
bot.polling(none_stop=True)
