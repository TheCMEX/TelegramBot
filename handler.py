#-*- coding: utf-8 -*-

'''
Telegram-бот, имитирующий консультанта по образовательным программа GoTo. По большей части работает по приципу одного из
последних новвоведений Telegram'a - клавиатур. На выбор возможны либо полная консультация, дарящая пользователю всю
необходимую информацию, либо же точечный выбор пользователем интересующих его функций или программ.
'''


import telebot                  # импортируем необходимые библиотеки. Бот написан в библиотеке pyTelegramBotAPI
from telebot import types

bot = telebot.TeleBot('344982115:AAHDoI-zYj61OXdypaZuHeLXrisYWIsewpk')   # присваиваем токен, который в целях защиты находится в отдельном файле constants.py

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Для работы с этим ботом мы предусмотрели два варианта консультации: \n \n ' 
'/consultation - Полная подробная консультация по всем образовательным программам GoTo (Рекомендуется) \n \n ' 
'Второй заключается в ответах на вопросы, заданные непосредственно пользователем при выборе одной из команд ниже: \n \n'
'/infgoto - Базовая информация о GoTo \n'
'/infprogramms - Информация обо всех образовательных программах \n \n'
'/gotocampgrant - Получение гранта на полное или частичное покрытие стоимости обучения в GoToCamp \n \n'
'Для повторного вызова этого меню используй команду /help \n'
'Для выбора другой команды введи "/" и выбери команду из появившегося списка \n \n'
'Удачного пользования, не забудь оставить отзыв через команду /service ^-^')


@bot.message_handler(commands=["consultation"])         # Ключевые слова было решено выделить жирным
def handle_consultation(message):
    sent = bot.send_message(message.chat.id, 'Привет! Меня зовут <b>GoToCampBot</b>. Я консультант по серии образовательных'
                                      ' программ в области IT, робототехники и анализа данных <b>GoTo</b>. Как мне к тебе'
                                      ' обращаться? Просто введи своё имя без точек и каких-либо посторонних символов.', parse_mode='HTML')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Информация о GoTo', 'Образовательные программы')
    msg = bot.send_message(message.chat.id, 'Очень приятно познакомиться, {username}. Хочешь ли ты сначала узнать, что такое школа '
                                           '<b>GoTo</b>, или сразу проконсультировать тебя по поводу образовательных программ? '
                                            'Для ответа на этот вопрос выбери один из вариантов ответа ниже.'.format(username=message.text), reply_markup=user_markup, parse_mode='HTML')
    bot.register_next_step_handler(msg, name)

def name(message):
    if message.text == 'Информация о GoTo' or message.text == '/infgoto':       # Второе условие сделано для прямого перехода к нему через команду
        bot.send_message(message.chat.id, 'Образовательные программы <b>GoTo</b> помогают молодежи со всей России '
                                          'воплощать в жизнь самые смелые идеи, получать знания у практикующих '
                                          'специалистов и предпринимателей, находить единомышленников и необходимые'
                                          ' ресурсы для развития своих проектов, обрести мотивацию к дальнейшему осознанному '
                                          'развитию. Участник каждой школы, лагеря, интенсива или хакатона GoTo получает '
                                          'возможность реализовать свои или предложенные компаниями-партнерами проекты и '
                                          'исследования по направлениям: анализ данных и машинное обучение, робототехника и '
                                          'интернет вещей, биоинформатика, веб и мобильная разработка, информационная'
                                          ' безопасность, виртуальная реальность, промдизайн, блокчейн и криптовалюты и др.'
                                          ' Команды участников проходят все этапы развития проекта – от идеи до реализации '
                                          'под кураторством предпринимателей, экспертов лучших университетов и ведущих '
                                          'компаний: <b>МФТИ, ВШЭ, СПбАУ, Иннополис, Яндекс, КРОК, ABBYY, Microsoft, Biocad,'
                                          ' Институт биоинформатики, Тинькофф, Intel, Сбербанк</b> и др. По итогам участники '
                                          'представляют свои проекты и получают рекомендации и поддержку по их развитию, '
                                          'приглашаются к сотрудничеству и на стажировки. Помимо работы над проектом в '
                                          'программы входят профориентационные игры, экскурсии в технологические компании '
                                          'и лаборатории, знакомство c учеными, экспертами и стартаперами, творческие'
                                          ' мастерские и квесты.', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('GoTo Camp', 'GoTo Course')
        user_markup.row('GoTo Hack')
        msg = bot.send_message(message.from_user.id,
                               'У нас на данный момент есть три вида образовательных программ: '
                               '<b>GoTo Camp, GoTo Course, GoTo Hack</b>. Для информации по той, что тебя '
                               'заинтересует, тебе всего лишь нужно выбрать нужную ниже.',
                               reply_markup=user_markup, parse_mode='HTML')
        bot.register_next_step_handler(msg, name1)
    else:
        msg = bot.send_message(message.chat.id, 'Образовательные программы')
        bot.register_next_step_handler(msg, programms)
def programms(message):
    if message.text == 'Образовательные программы' or message.text == '/infprogramms':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('GoTo Camp', 'GoTo Course')
        user_markup.row('GoTo Hack')
        msg = bot.send_message(message.chat.id,
                               'У нас на данный момент есть три вида образовательных программ: '
                               '<b>GoTo Camp, GoTo Course, GoTo Hack</b>. Для информации по той, что тебя '
                               'заинтересует, тебе всего лишь нужно выбрать нужную ниже.', reply_markup=user_markup, parse_mode='HTML')
        bot.register_next_step_handler(msg, name1)
def name1(message):
    if message.text  == 'GoTo Camp':
        bot.send_message(message.chat.id,
                         '<b>GoTo Camp</b> - это выездные школы на каждых каникулах для учеников 7-11 классов и младше'
                         'курсников со всей России и ближнего зарубежья. Школы проходят в формате выездного лагеря и посвящены '
                         'проектной деятельности в области IT: анализ данных и машинное обучение, робототехника, '
                         'информационная безопасность, блокчейн, VR / AR, биоинформатика, мобильная разработка '
                         'и др. С недавних пор открыты отдельные направления для начинающих по прикладному '
                         'программированию и робототехнике для ребят, имеющих совсем небольшой опыт в этих областях. '
                         'Ближайшая выездная школа пройдет в Санкт-Петербурге с 28 октября по 5 ноября.', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Принять участие в GoTo Camp')
        user_markup.row('GoTo Hack', 'GoTo Course')
        msg = bot.send_message(message.chat.id,
                               'Хочешь принять участие в этой программе или получить информацию по остальным? Как '
                               'всегда, дальнейшее действие можно выбрать ниже.', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'GoTo Course':
        bot.send_message(message.chat.id,
                         '<b>GoTo Course</b> - это серия очных интенсивов и курсов в Москве. \n'
                          'В октябре 2017 года повторится курс по прикладному программированию для начинающих. Программа '
                          'курса состоит в последовательной реализации мини-проектов на языке Python. Вся '
                          'необходимая теория, включая изучение самого языка, дается непосредственно в '
                          'процессе работы над проектом. Всего за 6 недель каждый сможет создать своего '
                          'телеграм-бота, приложение в Vk, бота для игры, провести мини-исследование соцсетей '
                          'и много другое. \n'
                          'К участию приглашаются школьники от 12 лет, интересующиеся IT и имеющие хотя бы '
                          'какой-то опыт программирования на любом языке.', parse_mode='HTML')

        bot.send_message(message.chat.id, 'Осенью 2017 года запускается курс по анализу данных – 2 месяца интенсивного'
                                          ' изучения теории и ее применения с преподавателями-практиками. К участию '
                                          'приглашаются все желающие любых возрастов. Курс будет полезен тем, кто хотел бы'
                                          ' освежить знания математики и алгоритмов и погрузиться в методы анализа данных и '
                                          'машинного обучения на продвинутом уровне и приобрести опыт решения практических '
                                          'задач. В рамках обучения участников ждут еженедельные лекции и семинары от опытных '
                                          'практиков, а также домашняя работа и вебинары с консультациями. Курс разработан '
                                          'под руководством Александра Петрова, посвятившего проектам в области анализа'
                                          ' данных компаний <b>E-Contenta, Яндекс, Tinkoff Digital, Data-Centric Alliance,'
                                          ' Mail.Ru Group больше 7 лет.</b> ', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Принять участие в GoTo Course')
        user_markup.row('GoTo Camp', 'GoTo Hack')
        msg = bot.send_message(message.chat.id,
                               'Хочешь принять участие в этой программе или получить информацию по остальным? Как '
                               'всегда, дальнейшее действие можно выбрать ниже.', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'GoTo Hack':
        bot.send_message(message.chat.id,
                         '<b>GoTo Hack</b> - это серия хакатонов для школьников и студентов. \n Второй хакатон прошел '
                         '9-11 декабря 2016 года и был посвящен актуальной теме – <b>Data Science</b> в сфере образования и HR. В рамках первого хакатона'
                         ' в феврале 2016 года участники вместе с экспертами в области Data Science и социологами исследовали свое поколение на '
                         'основе открытых данных соцсети ВКонтакте, проверили различные гипотезы, выявить механизмы распространения информации и '
                         'взаимодействия в соцсети, а также создали различные сервисы и рекомендательные системы.', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Принять участие в GoTo Hack')
        user_markup.row('GoTo Camp', 'GoTo Course')
        msg = bot.send_message(message.chat.id,
                                ' Хочешь принять участие в этой программе или получить информацию по остальным? Как '
                                'всегда, дальнейшее действие можно выбрать ниже.', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'Принять участие в GoTo Camp':
        bot.send_message(message.chat.id,  '<b>Осенняя школа</b> \n \n'
                                            'С 28 октября по 5 ноября в Санкт-Петербурге пройдёт проектная школа '
                                            'программирования для студентов и старшеклассников, интересующихся'
                                            ' биоинформатикой, робототехникой, прикладными разработками,'
                                            ' криптовалютами, анализом данных, инфобезопасностью, и т.д.', parse_mode='HTML')
        bot.send_message(message.chat.id, '<b>Направления</b> \n \n'
                                          'Каждый участник получит возможность реализовать свой проект или решить'
                                          ' задачу от партнеров под руководством экспертов и в деталях познакомиться'
                                          ' с машинным обучением, мобильной разработкой, функциональным'
                                          ' программированием, биоинформатикой, IoT, VR/AR, блокчейн и многим другим.', parse_mode='HTML')
        bot.send_message(message.chat.id, '<b>Программа</b> \n \n'
                                          'В программе школы помимо семинаров и работы над проектами представлены'
                                          ' мастер-классы, встречи с успешными предпринимателями и учеными,'
                                          ' профориентационные игры, экскурсии в компании и стартапы, а также спорт, '
                                          'прогулки, театры и самые необычные места СПб.', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Поехать за полную стоимость', 'Попробовать получить грант')
        user_markup.row('GoTo Course')
        user_markup.row('GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Проживание организовано в Sweet Village. Хостел будет полностью '
                                                 'занят участниками школы. Участие в школе с проживанием будет стоить'
                                                 ' 30 т.р., без проживания 20 т.р. Также любой желающий может принять'
                                                 ' участие в конкурсах GoTo Challenges и выиграть грант, частично или'
                                                 ' полностью покрывающий стоимость обучения. В рамках конкурса '
                                                 'участникам необходимо реализовать до 18 октября один из предложенных'
                                                 ' проектов.', reply_markup=user_markup)
        if message.text == 'Поехать за полную стоимость' or 'Попробовать получить грант':
            bot.register_next_step_handler(msg, name3)
        if message.text == 'GoTo Course' or 'GoTo Hack':
            bot.register_next_step_handler(msg, name1)

    if message.text == 'Вернуться к выбору стоимости':
        bot.send_message(message.chat.id,
                         '<b>Осенняя школа</b> \n \n'
                         'С 28 октября по 5 ноября в Санкт-Петербурге пройдёт проектная школа '
                         'программирования для студентов и старшеклассников, интересующихся'
                         ' биоинформатикой, робототехникой, прикладными разработками,'
                         ' криптовалютами, анализом данных, инфобезопасностью, и т.д.\n \n'
                         '<b>Направления</b> \n \n'
                         'Каждый участник получит возможность реализовать свой проект или решить'
                         ' задачу от партнеров под руководством экспертов и в деталях познакомиться'
                         ' с машинным обучением, мобильной разработкой, функциональным'
                         ' программированием, биоинформатикой, IoT, VR/AR, блокчейн и многим другим.\n \n'
                         '<b>Программа</b> \n \n'
                         'В программе школы помимо семинаров и работы над проектами представлены'
                         ' мастер-классы, встречи с успешными предпринимателями и учеными,'
                         ' профориентационные игры, экскурсии в компании и стартапы, а также спорт, '
                         'прогулки, театры и самые необычные места СПб.', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Поехать за полную стоимость', 'Попробовать получить грант')
        user_markup.row('GoTo Course')
        user_markup.row('GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Проживание организовано в Sweet Village. Хостел будет полностью '
                                                 'занят участниками школы. Участие в школе с проживанием будет стоить'
                                                 ' 30 т.р., без проживания 20 т.р. Также любой желающий может принять'
                                                 ' участие в конкурсах GoTo Challenges и выиграть грант, частично или'
                                                 ' полностью покрывающий стоимость обучения. В рамках конкурса '
                                                 'участникам необходимо реализовать до 18 октября один из предложенных'
                                                 ' проектов.', reply_markup=user_markup)
        if message.text == 'Поехать за полную стоимость' or 'Попробовать получить грант':
            bot.register_next_step_handler(msg, name3)
        else:
            bot.register_next_step_handler(msg, name1)

    if message.text == 'Принять участие в GoTo Course':
        bot.send_message(message.chat.id, '<b>ЕСЛИ ВЫ</b> \n \n' 
                         '· Школьник от 12 до 18 лет из Москвы. \n'
                         '· Интересуетесь программированием и хотите узнать, насколько широкий спектр возможностей в '
                                          'самых разных сферах жизни оно открывает перед вами. \n'
                         '· Знакомы с любым языком программирования.', parse_mode='HTML')
        bot.send_message(message.chat.id, '<b>ВЫ ПОЛУЧИТЕ</b> \n \n'
                         '· Базовые знания и опыт работы с ключевыми современными технологиями. \n'
                         '· Практическую реализацию десятка актуальных проектов под руководством куратора. \n'
                         '· Необходимые знания и практический опыт для реализации собственных ИТ-проектов. \n', parse_mode='HTML')
        bot.send_message(message.chat.id, '6 октября - 14 ноября '
                         'вторник, пятница 19:00 - 21:00')
        bot.send_message(message.chat.id, 'Программа курса состоит в последовательной реализации мини-проектов на'
                                          ' языке Python. Вся необходимая теория, включая изучение самого языка, дается'
                                          ' непосредственно в процессе работы над проектом и только тогда, когда это '
                                          'требуется для решения текущих задач.')
        user_markup = types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Регистрация')
        user_markup.row('GoTo Camp', 'GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Перейди к регистрации на курсы, выбрав вариант "Регистрация", либо же '
                                                 'вернись к одной из предыдущих программ.', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'Регистрация':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Перейти на сайт', url='https://goto.msk.ru/start_course/')
        keyboard.add(url_button)
        url_button1 = types.InlineKeyboardButton(text='Заявка', url='https://docs.google.com/forms/d/e/1FAIpQLSe0vbl3c-5N_STQj1uZ9prW_IZN5dX8EF_pid_iBdAyGOylnQ/viewform')
        keyboard.add(url_button1)
        bot.send_message(message.chat.id, 'Для наиболее точной информации рекомендую перейти на наш сайт, но '
                                          'также можно и сразу перейти к оформлению заявки на'
                                          'участие в курсах, выбрав действие ниже.', reply_markup=keyboard)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('GoTo Camp', 'GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Также можно вернуться к просмотру информации о наших других '
                                                'программах :))', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'Принять участие в GoTo Hack':
        bot.send_message(message.chat.id, '<b>Хакатон</b> \n \n'
                         'Трехдневное командное соревнование и образовательная программа, посвященные анализу данных в '
                                          'области образования и его персонализации. По итогам каждая из команд '
                                          'презентует результаты перед жюри для определения победителей.', parse_mode='HTML')
        bot.send_message(message.chat.id, '<b>GoToHack</b> \n \n'
                         'Серия хакатонов по перспективным технологическим направлениям для школьников и студентов'
                                          ' в рамках образовательного проекта GoTo. Отличительные особенности GoToHack:'
                                          ' длительный обучающий интенсив и кураторство кажого проекта куратором.', parse_mode='HTML')
        bot.send_message(message.chat.id, '<b>Data Science</b> \n \n'
                         'Междисциплинарная область о процессах и системах для извлечения инсайтов и анализа данных в '
                                          'различных формах, являющаяся продолжением статистики, машинного обучения, '
                                          'интеллектуального анализа данных, предиктивной аналитики и др.', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Узнать информацию')
        user_markup.row('GoTo Camp')
        user_markup.row('GoTo Course')
        msg = bot.send_message(message.chat.id, 'Узнай больше информации, либо вернись к одной'
                                                ' из других наших образовательных программ. ', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'Узнать информацию':
        keyboard = types.ReplyKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Перейти на сайт', url='https://goto.msk.ru/hackathon/')
        keyboard.add(url_button)
        url_button2 = types.InlineKeyboardButton(text='Узнать первым',
                                                 url='https://docs.google.com/forms/d/e/1FAIpQLSeKZUGIPnjlFmAp1ijoSvgJmX425izyJiBCOvwlQMzeQStItw/viewform?c=0&w=1')
        keyboard.add(url_button2)
        bot.send_message(message.chat.id, 'Для того, чтобы посмотреть последний состоявшийся <b>Data Science</b>, узнать о '
                                          'первом мероприятии <b>GoTo Hack</b>, а также понять, что даст тебе участие в этой'
                                          'образовательной программе, перейди на сайт. Чтобы узнать первым о приближаю'
                                          'щемся <b>GoTo Hack</b>, заполни форму, на которую тебя перекинет кнопка под сооб'
                                          'щением. Заполнение займёт крайне мало времени :)', parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('GoTo Camp')
        user_markup.row('GoTo Course')
        msg = bot.send_message(message.chat.id, 'Если ты хочешь узнать об оставшихся образовательных программах, смело'
                                                'кликай на нужную ниже ;)'
                                                , reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

def name3(message):
    if message.text == 'Поехать за полную стоимость':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Перейти на сайт', url='https://goto.msk.ru/camp_autumn/')
        keyboard.add(url_button)
        url_button2 = types.InlineKeyboardButton(text='Подать заявку',
                                                 url='https://docs.google.com/forms/d/e/1FAIpQLSf-srXAd7yaBcTET4dpLgLsKmNp-P5TH1HyLq02EfSBa9qBqA/viewform')
        keyboard.add(url_button2)
        bot.send_message(message.chat.id, 'Узнай более подробную информацию на нашем сайте, либо же сразу перейди к '
                                          'заполнению заявки на участие!', reply_markup=keyboard)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('GoTo Course', 'GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Ну, и если ты хочешь принять участие в другой программе, то можешь '
                                                 'получить информацию по остальным, а также оценить мою работу ^-^ ',
                                                    reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text == 'Попробовать получить грант':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Перейти на сайт', url='https://goto.msk.ru/camp_autumn/grants/')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Для наиболее точной информации рекомендую перейти на наш сайт, но '
                                          'также можно и сразу перейти к выбору гранта, выбрав действие ниже.', reply_markup=keyboard)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Стандартный грант', 'Smart контракт')
        user_markup.row('Вернуться к выбору стоимости')
        user_markup.row('GoTo Course', 'GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Можно и сразу перейти к выбору гранта, выбрав действие ниже. '
                                                 'Ну, и если ты хочешь принять участие в другой программе, то можешь '
                                                 'получить информацию по остальным.',
                                reply_markup=user_markup)
        if message.text == 'Стандартный грант' or 'Smart контракт':
            bot.register_next_step_handler(msg, grant)
        else:
            bot.register_next_step_handler(msg, name1)




def grant(message):
    if message.text or message.text.from_is_bot != 'Стандартный грант':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Подать заявку', url='https://docs.google.com/forms/d/e/1FAIpQLSf-srXAd7yaBcTET4dpLgLsKmNp-P5TH1HyLq02EfSBa9qBqA/viewform')
        keyboard.add(url_button)
        url_button1 = types.InlineKeyboardButton(text='Перейти на сайт', url='https://goto.msk.ru/camp_autumn/grants/')
        keyboard.add(url_button1)
        bot.send_message(message.chat.id, 'Любой желающий может принять участие в конкурсах <b>GoTo Challenges</b> и выиграть'
                                          ' грант, частично или полностью покрывающий стоимость обучения. Мы предлагаем'
                                          ' реализовать один из предложенных проектов. В этот раз доступны конкурсные '
                                          'задания по направлениям: анализ данных, функциональное программирование и '
                                          'блокчейн. \n' 
                                            'Помимо обычных грантов с заданиями в этот раз отдельно запускаем конкурс'
                                            ' на лучшие проектные идеи для реализации на школе для абитуриентов и'
                                            ' студентов 1-2 курса Университета ИТМО. В рамках отбора необходимо подать '
                                            'общую заявку на участие и выслать подробную презентацию о проекте и '
                                            'имеющиеся наработки. Абитуриентам необходимо дополнительно указать кодовое'
                                            ' слово от университета. \n' 
                                           'Решения принимаются до 18 октября включительно. Результаты будут объявлены'
                                           ' до 21 октября на нашем сайте. Отметим, что при участии в грантовых '
                                           'конкурсах рассматривается не только решения и предоставленные проекты, '
                                           'но и анкета, дополнительно может быть предложено собеседование.', reply_markup=keyboard, parse_mode='HTML')
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Вернуться к выбору стоимости')
        user_markup.row('GoTo Course', 'GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Ну, а если ты хочешь принять участие в другой программе, то можешь '
                                                 'получить информацию по остальным, либо же вернуться к выбору ' 
                                                 'стоимости программы.', reply_markup=user_markup)
        bot.register_next_step_handler(msg, name1)

    if message.text or message.text.from_is_bot == 'Smart контракт':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Подать заявку', url='https://docs.google.com/forms/d/e/1FAIpQLSf-srXAd7yaBcTET4dpLgLsKmNp-P5TH1HyLq02EfSBa9qBqA/viewform')
        keyboard.add(url_button)
        url_button1 = types.InlineKeyboardButton(text='Перейти на сайт', url='https://goto.msk.ru/camp_autumn/grants/')
        keyboard.add(url_button1)
        bot.send_message(message.chat.id, 'Одна из команд участников прошлой школы вместе с куратором разработала '
                                          'прототип системы для принятия и обработки конкурсных решений в виде '
                                          'приватной блокчейн платформе <b>GoToChain</b>. Блокчейн обеспечивает общедоступность'
                                          ' и неизменность данных о заявках и их проверке, позволит партнёрам и '
                                          'участникам следить за процессом проведения конкурса и создаст верифицируемые '
                                          'пункты портфолио для всех конкурсантов. После окончания соревнования '
                                          'участники получат доступ к проектам друг друга, что упрощает знакомство и '
                                          'взаимодействие внутри сообщества. В будущем планируется расширить область '
                                          'применения платформы: верифицируемое портфолио с проектами, голосования, '
                                          'сертификаты, биржа – все эти функции будут реализованы участниками школ и '
                                          'добавлены к существующей платформе.', parse_mode='HTML')
        bot.send_message(message.chat.id, 'В использовании системы нет ничего сложного. Проходите немного непривычную'
                                          ' регистрацию, выбираете направление, подписываете с нами смарт-контракт о'
                                          ' начале выполнения задания, читаете подробные условия, творите, отправляете '
                                          'результаты, ждёте, радуетесь, знакомитесь с другими участниками и их '
                                          'решениями, список которых станет доступным после окончания соревнования.', reply_markup=keyboard)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Вернуться к выбору стоимости')
        user_markup.row('GoTo Course', 'GoTo Hack')
        msg = bot.send_message(message.chat.id, 'Ну, а если ты хочешь принять участие в другой программе, то можешь '
                                                 'получить информацию по остальным, либо же вернуться к выбору ' 
                                                 'стоимости программы.', reply_markup=user_markup)
        if message.text == 'Вернуться к выбору стоимости':
            bot.register_next_step_handler(msg, name1)
        else:
            bot.register_next_step_handler(msg, name1)

def end(message):
    if message.text == '/service':
        msg = bot.send_message(message.chat.id,
                               "На этом моя консультация заканчивается. Надеюсь, ты узнал обо всём, что "
                               "было тебе интересно.\n"
                               " Также хотелось бы попросить оценить мою работу. Опиши в двух словах качество"
                               " моих ответов и, по возможности, напиши, что можно во мне улучшить :)")
        bot.register_next_step_handler(msg, result)

def result(message):
    if message.text:    # Здесь я подразумеваю обратную связь, как пересылаемое ботом сообщение (отзыв) любому пользователю
        bot.send_message(313191289, message.text)   # В данный момент это я, но потом можно будет завести специальный аккаунт для этого,
                                                    # Где можно будет обрабатывать все отзывы.

@bot.message_handler(commands=['infgoto'])
def infgoto(message):
    name(message)

@bot.message_handler(commands=['infprogramms'])
def infprogramms(message):
    programms(message)

@bot.message_handler(commands=['gotocampgrant'])
def gotocampgrant(message):
    grant(message)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Выполнение команды завершено. Что дальше? Выбери справа '
                                           'от поля отправки сообщений кнопку "/" и определись с '
                                           'дальнейшим путём.', reply_markup=hide_markup)

@bot.message_handler(commands=['help'])
def help(message):
    handle_start(message)

@bot.message_handler(commands=['service'])
def service(message):
    end(message)

bot.polling(none_stop = True, interval=0)   # Потом можно будет реализовать считывание ботом информации через вебхуки,
                                            # но сейчас пока что можно ограмничиться и методом polling





"""import telebot
import constants

bot = telebot.TeleBot(constants.token)

# upd = bot.get_updates()
# print(upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)"""

"""print(bot.get_me())

def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \n Текст - {3}'.format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)
@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Надеюсь, сейчас всё работает. Чайку принести?')


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Фото':
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, constants.template_photo_id)


bot.polling(none_stop = True, interval=0)"""


'''Привет! Для работы с этим ботом мы предусмотрели два варианта консультации:

/consultation - Полная подробная консультация по всем образовательным программам GoTo (Рекомендуется)

Второй заключается в ответах на вопросы, заданные непосредственно пользователем при выборе одной из команд ниже:

/infgoto - Базовая информация о GoTo
/infprogramms - Информация обо всех образовательных программах

Также можно выборочно сразу перейти к интересующей вас программе, если вы уже знаете о нашей деятельности:

/gotocamp - Школа GoToCamp
/gotocourse - Курсы GoToCourse
/gotohack - Хакатоны GoToHack
/gotocampgrant - Получение гранта на полное или частичное покрытие стоимости обучения в GoToCamp

Удачного пользования, не забудьте оставить отзыв через команду /service ^-^'''