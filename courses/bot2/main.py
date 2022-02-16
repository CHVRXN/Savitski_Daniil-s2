import telebot
from telebot import types

bot = telebot.TeleBot('5110925989:AAEJdiQM9R3m0T6cgWzPskEuawEXit4X9Xg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Lina')
    btn2 = types.KeyboardButton('Legion Commander')
    btn3 = types.KeyboardButton('Terrorblade')
    btn4 = types.KeyboardButton('Techies')
    btn5 = types.KeyboardButton('Shadow Fiend')
    btn6 = types.KeyboardButton('Phantom Assassin')
    btn7 = types.KeyboardButton('Crystal Maiden')
    btn8 = types.KeyboardButton('Zeus')
    btn9 = types.KeyboardButton('Monkey King')
    btn10 = types.KeyboardButton('Juggernaut')
    btn11 = types.KeyboardButton('Io')
    btn12 = types.KeyboardButton('Pudge')
    btn13 = types.KeyboardButton('Rubick')
    btn14 = types.KeyboardButton('Earthshaker')
    btn15 = types.KeyboardButton('Ogre Magi')
    btn16 = types.KeyboardButton('Wraith King')
    btn17 = types.KeyboardButton('Queen of Pain')
    btn18 = types.KeyboardButton('Windranger')
    btn19 = types.KeyboardButton('Spectre')
    btn20 = types.KeyboardButton('Drow Ranger')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
               btn17, btn18, btn19, btn20)
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nКакой герой тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "Выбрать другого героя":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Lina')
        btn2 = types.KeyboardButton('Legion Commander')
        btn3 = types.KeyboardButton('Terrorblade')
        btn4 = types.KeyboardButton('Techies')
        btn5 = types.KeyboardButton('Shadow Fiend')
        btn6 = types.KeyboardButton('Phantom Assassin')
        btn7 = types.KeyboardButton('Crystal Maiden')
        btn8 = types.KeyboardButton('Zeus')
        btn9 = types.KeyboardButton('Monkey King')
        btn10 = types.KeyboardButton('Juggernaut')
        btn11 = types.KeyboardButton('Io')
        btn12 = types.KeyboardButton('Pudge')
        btn13 = types.KeyboardButton('Rubick')
        btn14 = types.KeyboardButton('Earthshaker')
        btn15 = types.KeyboardButton('Ogre Magi')
        btn16 = types.KeyboardButton('Wraith King')
        btn17 = types.KeyboardButton('Queen of Pain')
        btn18 = types.KeyboardButton('Windranger')
        btn19 = types.KeyboardButton('Spectre')
        btn20 = types.KeyboardButton('Drow Ranger')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17, btn18, btn19, btn20)

        final_message = "Выбрать другого героя"
    elif get_message_bot == 'lina':
        markup = types.InlineKeyboardMarkup()
        img = open('res/artlina.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Lina"))
        final_message = "Многие знают, что волосы Lina благословлены огнём, но лишь некоторые знают, почему. Когда " \
                        "Lina была ещё совсем молодой, именно дымящиеся и тлеющие волосы были первым признаком того, " \
                        "что она обладает огромной силой. Потребовались годы усердных тренировок, чтобы волшебница " \
                        "смогла контролировать подобные проявления своего таланта. Но, тем не менее, эту силу нельзя " \
                        "скрывать вечно, и в самые напряжённые моменты битвы волосы Lina вспыхивают, " \
                        "показывая абсолютную концентрацию и высшую степень владения пламенем, которое способно " \
                        "испепелить всё на своем пути. "
    elif get_message_bot == 'legion commander':
        markup = types.InlineKeyboardMarkup()
        img = open('res/artlega.png', 'rb')
        markup.add(
            types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Legion_Commander"))
        final_message = "Встав на путь мести против бездны, Тресдин посетила кузнеца Квита, о котором ходила недобрая " \
                        "молва. Он подарил ей эти адские клинки. Но слишком поздно может прийти осознание факта, " \
                        "что цена за использование такой силы будет намного больше того, с чем она готова расстаться… "
    elif get_message_bot == 'terrorblade':
        markup = types.InlineKeyboardMarkup()
        img = open('res/tb.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Terrorblade"))
        final_message = "Глубоко в аду внутри ада, Terrorblade был заключён в стенах своей тюрьмы-измерения, приговорённый к вечности извращённого созерцания. Он долго смотрел на отражение худшего себя. А то, в свою очередь, долго смотрело в него. Но теперь они сражаются бок о бок — единая сущность, более могущественная, чем когда-либо прежде. "
    elif get_message_bot == 'techies':
        markup = types.InlineKeyboardMarkup()
        img = open('res/tech.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Techies"))
        final_message = "После месяцев работы подрывники Techies с гордостью представляют своё новейшее вооружение: The Swine, самую мощную в мире пушку. Во время первого своего выстрела она разорвала на части галеру, на которой стояла, и вылетела на берег. Через несколько дней её нашли глубоко в скале прямо под мастерской её создателей."
    elif get_message_bot == 'shadow fiend':
        markup = types.InlineKeyboardMarkup()
        img = open('res/sf.jpg', 'rb')
        markup.add(
            types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Shadow_Fiend"))
        final_message = "Shadow Fiend уже давно собирает души своих врагов. Как и у любого коллекционера, у него есть крайне ценные трофеи, которые хочется показать всем окружающим. Однако есть души, которые бы не следовало трогать, переполненные тьмой и яростью настолько, что ни одно живое существо не способно их удержать. Изменившись навсегда, Shadow Fiend познал плату за сбор душ демонов, но вместе с ней он познал и всю их мощь."
    elif get_message_bot == 'phantom assassin':
        markup = types.InlineKeyboardMarkup()
        img = open('res/pa.jpg', 'rb')
        markup.add(
            types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Phantom_Assassin"))
        final_message = "Издав хриплый смешок, старший кузнец Крейлер взмахнул мечом, ковавшимся 11 поколениями его " \
                        "семьи. Он был настолько острым, что окружающий мир, с треском разорвавшейся материи, " \
                        "разошёлся. Через этот разрыв Крейлер увидел себя несколькими мгновениями ранее, державшего " \
                        "тот же самый вожделенный меч. Вдруг, в приступе алчности и сумасшествия, он сразил своего " \
                        "двойника, чтобы заполучить второй меч. Но, с запозданием Крейлер почувствовал знакомую рану, " \
                        "и внезапно воспоминания о ней нахлынули на него… "
    elif get_message_bot == 'crystal maiden':
        markup = types.InlineKeyboardMarkup()
        img = open('res/cm.jpg', 'rb')
        markup.add(
            types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Crystal_Maiden"))
        final_message = "Ходят слухи, что это одеяние было свадебным платьем древней королевы. По другим сведениям оно являлось плащом ледяного огра. Однако в действительности, эти зачарованные ткани изменчивы, как лавина, и могут принимать любые формы. Последняя форма привлекла одинокого волчонка, который стал выносливым и верным спутником."
    elif get_message_bot == 'zeus':
        markup = types.InlineKeyboardMarkup()
        img = open('res/zeus.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Zeus"))
        final_message = "Этот шлем, выкованный кланом Молотов Целестарра и наполненный энергией древних, словно влитой сидит на голове самого Повелителя небес. Неверующие содрогнутся, когда заслышат над полем боя раскаты грома!"
    elif get_message_bot == 'monkey king':
        markup = types.InlineKeyboardMarkup()
        img = open('res/mk.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Monkey_King"))
        final_message = "Пусть прегрешения Сунь Укуна были давно прощены, его волнующие свершения живы в нашей памяти и по сей день. Переживите три легендарных подвига из прошлых похождений героя."
    elif get_message_bot == 'juggernaut':
        markup = types.InlineKeyboardMarkup()
        img = open('res/jugger.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Juggernaut"))
        final_message = "Маска Юрнеро раскололась надвое, пробудив покоившиеся в ней древние души. Они стали одним целым с Юрнеро, наделив его мудростью и яростью предков. Такой симбиоз превратил знакомого нам героя во что-то новое и пугающее… Снизошедшее до простых смертных стихийное бедствие."

    elif get_message_bot == 'io':
        markup = types.InlineKeyboardMarkup()
        img = open('res/io.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Io"))
        final_message = "В каждой из вселенных таятся отголоски этого предвечного существа, что существовало меж пределами известных и неизвестных нам миров ещё до начала времён. Проведя вечность в самых удалённых уголках загадочных пределов, Io знает: куда бы вас не вела буря сражения, связь дружбы поможет пережить что угодно."

    elif get_message_bot == 'pudge':
        markup = types.InlineKeyboardMarkup()
        img = open('res/pudge.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Pudge"))
        final_message = "Много веков назад румуссская волшебница Крелла сковала нерушимый крюк на цепи, что остановил бы самых могучих прислужников Мёртвого бога и отвадил бы погибель от её избранников. Но мор Мёртвого бога превзошёл даже легендарные заклинания Креллы. Одержимые песнью панихиды, цепи оставили свою госпожу и стали сокрушать её подданных, подчиняясь приказам Мёртвого бога. Теперь же, давно исполнив своё нечистое предназначение, цепи поклялись служить новому господину… и его упоительному ремеслу."

    elif get_message_bot == 'rubick':
        markup = types.InlineKeyboardMarkup()
        img = open('res/rubick.png', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Rubick"))
        final_message = "Многие маги считали, что Великая головоломка — это лишь занятная диковинка. И всё же целые поколения волшебников убивались в попытках её понять. Даже когда величайший маг посчитал, что раскрыл её секрет, он ещё долго не ведал её истинного смысла: знания, сокрытые внутри Великой головоломки, позволяли ему изменять саму природу магии. И теперь Rubick не просто виртуозно подражает чужому искусству. Отметая все пределы магических возможностей, он по своему велению меняет суть волшебства и непрестанно ищет и разгадывает новые сверхъестественные загадки. Быть может, они тоже откроют ему неведомые стороны чародейства."

    elif get_message_bot == 'earthshaker':
        markup = types.InlineKeyboardMarkup()
        img = open('res/es.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Earthshaker"))
        final_message = "Будучи единым с духом этой земли, теперь он несёт её частицу в другие почвы. Преисполненный отголосками воспоминаний о разбитой тверди, Землевержец заплатил великую цену, но уже одолел одного межзвёздного гостя, возжелавшего уничтожить силу внутри него. Она пробудилась и стремится возродить сгинувший мир, однако её преследуют многие тёмные силы, желающие закончить начатое. И вот впервые в жизни Землевержец устремил свой взор к небесам, чтобы хоть как-нибудь смириться с разрушительной смертью, что понесла его сестрица-земля… И любой ценой отомстить за её кончину."

    elif get_message_bot == 'ogre magi':
        markup = types.InlineKeyboardMarkup()
        img = open('res/ogre.png', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Ogre_Magi"))
        final_message = "Потерянная, отбившаяся от стаи, так ещё и осёдланная невыносимо глупым огром, виновным в этом всём, жар-жаворонок Сердцестайка была вынуждена довериться богине удачи, чтобы пережить испытания на пути воссоединения со своими сородичами. Как-никак, сама богиня и поставила Огра-мага присматривать за этой стаей. Вот только… с какого дуба она рухнула, посчитав это хорошей затеей?"

    elif get_message_bot == 'wraith king':
        markup = types.InlineKeyboardMarkup()
        img = open('res/wk.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Wraith_King"))
        final_message = "Во времена, позабытые даже самим Остарионом, он утолял страсть к вечной жизни не призрачной эссенцией, а безостановочной жатвой костей. Выжженные кости образовали стены его дворца; улицы мостились костьми всех известных существ и врагов. И боялись существа из плоти заходить во владения Короля, ведь он прежде всего был коллекционером, и ничто в Костяной империи не ускользало от вечного взора его безжизненных глаз."

    elif get_message_bot == 'queen of pain':
        markup = types.InlineKeyboardMarkup()
        img = open('res/qop.jpg', 'rb')
        markup.add(
            types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Queen_of_Pain"))
        final_message = "Довольная своим долгим путешествием по миру смертных, Акаша возвращается к опасному Ристульскому двору, где за время отсутствия её влияние иссякло. Но королева в мире верхнем намеревается покорить себе и трон нижних пределов. Заключив сделку с изгнанным демоном-принцем, Акаша расширила свою власть, и её дьявольские планы наконец начинают осуществляться."

    elif get_message_bot == 'windranger':
        markup = types.InlineKeyboardMarkup()
        img = open('res/wr.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Windranger"))
        final_message = "Лиралей и её приёмную семью всегда занимала загадка рождения лучницы. Но чем старше она становилась, чем крепче была её необыкновенная связь с ветром, тем больше Лиралей тревожили мысли о её происхождении. Надеясь сбежать от тягостных дум, она лишь обрекла себя узнать горькую истину: что в ночь праведной расплаты её деревню и кровных родственников уничтожили элементали ветра и что без этой катастрофы Лиралей не стала бы одной из них."

    elif get_message_bot == 'spectre':
        markup = types.InlineKeyboardMarkup()
        img = open('res/spectre.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Spectre"))
        final_message = "Многочисленные проявления Меркуриал — больше не осколки единой сущности. Один из них крал у многих, и теперь из него восходит новый лик Спектры. Обманом заключённая в проклятые доспехи, отчуждённая тень Меркуриал заметила: с каждой душой, отнятой во имя этой испорченной брони, она всё сильнее осознавала себя. Сперва насильное разделение привело Меркуриал в ярость, но теперь она ищет эту дразнящую свободу… и ради неё убивает столько, сколько потребуется."

    elif get_message_bot == 'drow ranger':
        markup = types.InlineKeyboardMarkup()
        img = open('res/traks.jpg', 'rb')
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Drow_Ranger"))
        final_message = "Через глаза безумной маски Траксекс мельком взглянула на забытые воспоминания своей молодости. Но помимо кошмаров, о которых лучница не давала себе думать, маска раскрыла и многое другое — ужасы, увиденные другими глазами в другие времена. Память о жестокости, простирающейся сквозь несчётные года, загадочным образом заполнила кровожадностью каждый уголок подсознания Траксекс. И даже сняв маску, она сражается, чтобы преодолеть порывы саморазрушения, высвобожденные злом, выжженным за её глазами. В этом водовороте ненависти её единственное спасение — это месть… Месть любой достойной жертве, встреченной на пути."


    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Lina')
        btn2 = types.KeyboardButton('Legion Commander')
        btn3 = types.KeyboardButton('Terrorblade')
        btn4 = types.KeyboardButton('Techies')
        btn5 = types.KeyboardButton('Shadow Fiend')
        btn6 = types.KeyboardButton('Phantom Assassin')
        btn7 = types.KeyboardButton('Crystal Maiden')
        btn8 = types.KeyboardButton('Zeus')
        btn9 = types.KeyboardButton('Monkey King')
        btn10 = types.KeyboardButton('Juggernaut')
        btn11 = types.KeyboardButton('Io')
        btn12 = types.KeyboardButton('Pudge')
        btn13 = types.KeyboardButton('Rubick')
        btn14 = types.KeyboardButton('Earthshaker')
        btn15 = types.KeyboardButton('Ogre Magi')
        btn16 = types.KeyboardButton('Wraith King')
        btn17 = types.KeyboardButton('Queen of Pain')
        btn18 = types.KeyboardButton('Windranger')
        btn19 = types.KeyboardButton('Spectre')
        btn20 = types.KeyboardButton('Drow Ranger')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17, btn18, btn19, btn20)
        markup = types.InlineKeyboardMarkup()
        final_message = "ошибка\nВоспользуйся одной из интерактивных кнопок ниже"
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
