import random, time, winsound
from tkinter import *

print('started')

def secretEnd():
    canv = Canvas(root, width = 300, height = 300, bg = 'black')
    canv.pack(expand = YES, fill = BOTH)
    root.geometry('500x500')
    root['bg'] = 'black'
    root.title("Желудок собаки")
    
    #Еда в желудке
    food1 = PhotoImage(file='./food/1food.png')
    id_food1 = canv.create_image(400, 10, anchor = NW, image = food1)  #1
    
    food2 = PhotoImage(file='./food/2food.png')
    id_food2 = canv.create_image(102, 30, anchor = NW, image = food2)  #2
    
    food3 = PhotoImage(file='./food/3food.png')
    id_food3 = canv.create_image(392, 288, anchor = NW, image = food3)  #3

    food4 = PhotoImage(file='./food/4food.png')
    id_food4 = canv.create_image(144, 285, anchor = NW, image = food4)  #4

    food5 = PhotoImage(file='./food/5food.png')
    id_food5 = canv.create_image(250, 400, anchor = NW, image = food5)  #5

    food6 = PhotoImage(file='./food/6food.png')
    id_food6 = canv.create_image(7, 76, anchor = NW, image = food6)  #6

    food7 = PhotoImage(file='./food/7food.png')
    id_food7 = canv.create_image(80, 172, anchor = NW, image = food7)  #7

    food8 = PhotoImage(file='./food/8food.png')
    id_food8 = canv.create_image(100, 400, anchor = NW, image = food8)  #8 

    food9 = PhotoImage(file='./food/9food.png')
    id_food9 = canv.create_image(266, 120, anchor = NW, image = food9)  #9

    food10 = PhotoImage(file='./food/10food.png')
    id_food10 = canv.create_image(12, 292, anchor = NW, image = food10)  #10

    eaten = PhotoImage(file='./food/youWereEaten.png')
    id_eaten = canv.create_image(250, 250, anchor = CENTER, image = eaten)  #10
    root.update()

    root.update()
    winsound.PlaySound('./music secret/secretEndMus.wav',winsound.SND_LOOP + winsound.SND_ASYNC)

    foodLst = [id_food1, id_food2, id_food3, id_food4, id_food5, id_food6, id_food7, id_food8, id_food9, id_food10]

    while True:
        for i in range(0,10):
            
            x=random.triangular(-4, 4)
            y=random.triangular(-4, 4)

            canv.move(foodLst[i], x,y)
            pos = canv.coords(foodLst[i])
            
            if pos[0] >= 450:
                canv.move(foodLst[i], -10,y)
            elif pos[0] < 1:
                canv.move(foodLst[i], 10,y)
            if pos[1] >= 450:
                canv.move(foodLst[i], x,-10)
            elif pos[1] <= 0:
                canv.move(foodLst[i], x,10)

            root.update()
    time.sleep(10)
# Остановка программы на Esc
def stopIt(event):
    root.destroy()

#Уничтожает таблицу с результатами
def DestroyAllScores(event):
    global CloseResultsBut, ResultsTxt
    CloseResultsBut.destroy()
    ResultsTxt.destroy()

def AllScores(event):
    global CloseResultsBut, ResultsTxt
    with open('scores.txt', 'r') as file:
        Results = file.read()
    CloseResultsBut = Button(root, text='Закрыть резултаты', width=50, height=2, font=("Soviet font Regular", 11), bg='beige')
    ResultsTxt = Text(root, width = 41, height = 20)
    ResultsTxt.insert(END, Results)
    CloseResultsBut.place(relx=0.5, rely=0.05, anchor=CENTER)
    ResultsTxt.place(relx=0.5, rely=0.6, anchor=CENTER)

    CloseResultsBut.bind('<1>', DestroyAllScores)
    #Scrollbar
# сохранение результатов. Появление 'Ваш результат успешно сохранен!'. Запись в файл scores.txt. Вызов rand
def save(event):
    global message, moves, SavedLabel
    flagClick = False
    SavedLabel = Label(root, width=50, height=1, text='Ваш результат успешно сохранен!', fg='white', bg='royalblue')
    SavedLabel.place(relx=0.5, rely=0.03, anchor=CENTER)
    SavedLabel.update()
    NewLine = f'имя: {message.get()} результат: {moves - 1} \n'
    with open('scores.txt', 'a') as file:
        file.write(NewLine)

    moves = 1
    rand(event)

# Размещение всех элементов в root. Если имя == '', то
def root1(event):
    global lab, ent, StartButt, message

    flagClick = False

    #Основное окно
    root.geometry('330x344')
    destroy_object = [lab, ent, StartButt]
    for object_name in destroy_object:
        object_name.destroy()
    # 1
    Sc1.place(relx=0, rely=0, anchor=CENTER)
    Sc2.place(relx=0.5, rely=0, anchor=CENTER)
    Sc3.place(relx=1, rely=0, anchor=CENTER)
    # 2
    Sc4.place(relx=0, rely=0.5, anchor=CENTER)
    Sc5.place(relx=0.5, rely=0.5, anchor=CENTER)
    Sc6.place(relx=1, rely=0.5, anchor=CENTER)
    # 3
    Sc7.place(relx=0, rely=0.827, anchor=CENTER)
    Sc8.place(relx=0.5, rely=0.827, anchor=CENTER)
    Sc9.place(relx=1, rely=0.827, anchor=CENTER)

    but.place(relx=0.5, rely=0.5, anchor=CENTER)
    if message.get() != '':
        pass
    else:
        ErrorLabel.place(relx = 0.5, rely = 0.03, anchor = CENTER)
        ErrorLabel.update()

# Ошибка последовательности пользователя. Обнуление резултатов. Кнопки сохр и заново
def Error(ev):
    global x1, comp, countOfMoves, moves, but, lab, user, message, butt, SaveBut, ScoresBut, flagClick

    flagClick = False

    # Индиткатор ошибки
    root['bg'] = 'red'
    root.update()
    time.sleep(0.5)
    root['bg'] = 'white'
    root.update()

    # Кнопки заново и сохранить
    SaveBut = Button(root, text='Сохранить результат', width=20, height=2, font=("Soviet font Regular", 11), bg='beige')
    butt = Button(root, text='Начать заново', width=20, height=2, font=("Soviet font Regular", 11), bg='beige')
    ScoresBut = Button(root, text='Все результы', width=20, height=2, font=("Soviet font Regular", 11), bg='beige')


    butt.place(relx=0.5, rely=0.4, anchor=CENTER)
    if message.get() != '': # Если пользователь ничего не ввел в имя
        SaveBut.place(relx=0.5, rely=0.6, anchor=CENTER)
        ScoresBut.place(relx=0.5, rely=0.2, anchor=CENTER)
    else:
        ScoresBut.place(relx=0.5, rely=0.6, anchor=CENTER)
        moves = 1
    ScoresBut.bind('<1>', AllScores)
    butt.bind('<1>', rand)
    SaveBut.bind('<1>', save)

    # Сколько смог набрать
    lab.update()
    lab = Label(root, text=f'your score is {countOfMoves - 2}', font=('Franklin gotich Medium', 13), bg='black', fg='blue')
    lab.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Обновление программы

    countOfMoves = 1
    x1 = []
    comp = []
    user = []

# Выводит надпсиь с обратным отсчетом после секретного секрета
def foo():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    secretLab = Label(root, text = 'ПрОДоЛжиМ чеРЕз ', width=20, height=2, font=("Determination Mono(RUS BY LYAJK", 11), bg='beige')
    secretLab.place(relx=0.5, rely = 0.4)
    for i in range(0,4):
        secretLab['text'] = f'ПрОДоЛжиМ чеРЕз {3-i}'
        secretLab.update()
        time.sleep(1)
    secretLab.destroy()
    rand(Event)

# Функция сравнения списков
def NewMove(comp, user):
    if len(comp) == len(user):
        i = 0
        while i < len(comp):
            if comp[i] != user[i]:
                return False
            i += 1
    else:
        return False

    return True

#  Сравнивает последовательность пользователя с последовательностью секретного секрета
def SecretFoo(secretLst, user):
    if len(secretLst) == len(user):
        i = 0
        while i < len(secretLst):
            if secretLst[i] != user[i]:
                return False
            i += 1
    else:
        return False

    return True

# Обновляет программу после секретного секрета и делает кнопки разноцветными
def meow(event):
    global canv, butt1, butt2, secretLab, countOfMoves, x1, comp, user
    canv.destroy()
    root['bg'] = 'beige'
    root.title("Among As Dog")
    root.geometry('330x344')

    Sc1['bg'] = 'maroon'
    Sc2['bg'] = 'lawn green'
    Sc3['bg'] = 'cyan'
    Sc4['bg'] = 'tan4'
    Sc5['bg'] = 'chocolate1'
    Sc6['bg'] = 'gold'
    Sc7['bg'] = 'navy'
    Sc8['bg'] = 'gray10'
    Sc9['bg'] = 'LemonChiffon4'
    root.update()



    #Изменение правильных списков и обновление
    countOfMoves = 1
    x1 = []
    comp = []
    user = []

    foo()










    root.update()

# Функция нажатия на квадрат 1) издет звук 2) NewMove 1 тогда 2) секретный секрет
def F1(event):
    global x1, user, comp, moves, countOfMoves, but, SaveBut, butt, flagClick, secretEnt, canv, secretFlag, secretErrFlag
    if flagClick == True:
        # Для звуков во время нажатия
        SavedLabel.destroy()
        ErrorLabel.destroy()
        SaveBut.destroy()
        SavedLabel.update()
        '''ErrorLabel.update()'''
        if event.widget == Sc1:
            winsound.PlaySound('./klick/4.wav', winsound.SND_FILENAME)
        if event.widget == Sc2:
            winsound.PlaySound('./klick/3.wav', winsound.SND_FILENAME)
        if event.widget == Sc3:
            winsound.PlaySound('./klick/2.wav', winsound.SND_FILENAME)
        if event.widget == Sc4:
            winsound.PlaySound('./klick/1.wav', winsound.SND_FILENAME)
        if event.widget == Sc5:
            winsound.PlaySound('./klick/0.wav', winsound.SND_FILENAME)
        if event.widget == Sc6:
            winsound.PlaySound('./klick/-1.wav', winsound.SND_FILENAME)
        if event.widget == Sc7:
            winsound.PlaySound('./klick/-2.wav', winsound.SND_FILENAME)
        user.append(event.widget)
        if event.widget == Sc8:
            winsound.PlaySound('./klick/-3.wav', winsound.SND_FILENAME)
        if event.widget == Sc9:
            winsound.PlaySound('./klick/-4.wav', winsound.SND_FILENAME)
        moves += 1
        if moves >= countOfMoves:
            if NewMove(comp, user):
                # если списки равны

                flagClick = False

                root['bg'] = 'blue'

                root.update()
                time.sleep(0.5)
                root['bg'] = 'white'
                root.update()
                moves = 1
                user = []
                but = Button(root, text=('Начать', countOfMoves, 'раунд'),font=("Mastodon Bold", 20), width=15, height=1, bg='beige')
                but.place(relx=0.5, rely=0.5, anchor=CENTER)
                but.bind('<1>', rand)
            elif SecretFoo(user, secretLst) and secretFlag == False:
                root.geometry('500x500')
                root['bg'] = 'black'
                root.title(".....................")

                secretErrFlag = True
                secretFlag = True
                flagClick = False

  
                canv.pack(expand = YES, fill = BOTH)
                dogObj = PhotoImage(file='1.gif')
                
                idDog = canv.create_image(550, 50, anchor = NW, image = dogObj)
                root.update()

                winsound.PlaySound('./music secret/repairing.wav', winsound.SND_FILENAME)

                for i in range(50):
                    canv.move(1, -10,0)
                    if i == 5:
                        winsound.PlaySound('./music secret/roomOfDog.wav', winsound.SND_ASYNC)

                    root.update()

                    time.sleep(0.2)
                time.sleep(2)
                dogObj = PhotoImage(file='2.gif')
                idDog = canv.create_image(50, 135, anchor = NW, image = dogObj)
                root.update()
                time.sleep(5)
                dogObj = PhotoImage(file='3.gif')
                idDog = canv.create_image(50, 70, anchor = NW, image = dogObj)
                root.update()
                time.sleep(2)

                dogObj = PhotoImage(file='1.gif')
                idDog = canv.create_image(50, 50, anchor = NW, image = dogObj)
                root.update()
                time.sleep(1)
                i = 40
                while i != 0:
                    canv.move(idDog, i,0)
                    root.update()

                    time.sleep(0.05)
                    i -=4
                for i in range(0,90,4):
                    canv.move(idDog, -i,0)
                    time.sleep(0.05)
                    root.update()
                root.title('$%!НАЖМИ НА ЛЮБУЮ КНОПКУ@#!')
                root.bind('<KeyPress>', meow)
                countOfMoves = 1
                x1 = []
                comp = []
                user = []
                moves = 1
              
            else:
                # если списки не равны
                if secretErrFlag:
                    secretEnd()
                else:
                    Error(event)

# уничтожение кнопок заново и сохр, Верхних надписей. Озвучивание загорающихся квадратиков. Добавление эл-тов в comp[-1]
def rand(event):
    global x1, comp, countOfMoves, moves, lab, memory_time, butt, SaveBut, ScoresBut, flagClick, butt1, butt2, secretLab
    destroy_object = [SaveBut, ScoresBut, butt, butt1, butt2, lab, secretLab, but]
    for object_name in destroy_object:
        object_name.destroy()
    flagClick = False
    butt1.update()
    butt2.update()
    secretLab.update()

    root.unbind("<KeyPress>")

    if moves > countOfMoves:  # В случае ошибки
        moves = countOfMoves

    but.update()
    i = 0
    if countOfMoves > 8:
        memory_time = 0.4
    x1 = random.choice([Sc1, Sc2, Sc3, Sc4, Sc5, Sc6, Sc7, Sc8, Sc9])
    comp.append(x1)
    while i != countOfMoves:
        time.sleep(memory_time)
        comp[i]['bg'] = 'green'
        root.update()
        #Для звуков во время запоминания
        if comp[i] == Sc1:
            winsound.PlaySound('./klick/4.wav', winsound.SND_FILENAME)
        if comp[i] == Sc2:
            winsound.PlaySound('./klick/3.wav', winsound.SND_FILENAME)
        if comp[i] == Sc3:
            winsound.PlaySound('./klick/2.wav', winsound.SND_FILENAME)
        if comp[i] == Sc4:
            winsound.PlaySound('./klick/1.wav', winsound.SND_FILENAME)
        if comp[i] == Sc5:
            winsound.PlaySound('./klick/0.wav', winsound.SND_FILENAME)
        if comp[i] == Sc6:
            winsound.PlaySound('./klick/-1.wav', winsound.SND_FILENAME)
        if comp[i] == Sc7:
            winsound.PlaySound('./klick/-2.wav', winsound.SND_FILENAME)
        if comp[i] == Sc8:
            winsound.PlaySound('./klick/-3.wav', winsound.SND_FILENAME)
        if comp[i] == Sc9:
            winsound.PlaySound('./klick/-4.wav', winsound.SND_FILENAME)
        time.sleep(memory_time)
        if secretFlag:
             colorBg = random.choice(['gold', 'snow', 'cornflower blue', 'tan1', 'DarkOrange2', 'ivory2', 'linen', 'coral', 'green2', 'black', 'brown4', 'purple1', 'LightSalmon2', 'bisque2'])
             comp[i]['bg'] = colorBg
        else:
            comp[i]['bg'] = 'black'
        root.update()
        i += 1
        if i > countOfMoves:
            root.destroy()
    countOfMoves += 1
    flagClick = True

root = Tk()
root.resizable(height=False, width=False)

#Окно регистрации
root.geometry('500x170')
root['bg'] = 'beige'
root.title("Among Us Task")
root.iconphoto(True, PhotoImage(file = ('icon.ico')))

message = StringVar() # Текст с Entry
lab = Label(root, text = 'Введите имя: ', font=("Soviet font Regular", 30), bg = 'beige')
ent = Entry(root, width = 20, font=("Mastodon Bold", 20), bg = 'beige', fg ='black', textvariable=message)
StartButt = Button(root, text='старт', width=5, height=1, bg='beige', font=("Soviet font Regular", 20))

lab.place(relx=0.5, rely=0.15, anchor=CENTER)
ent.place(relx=0.5, rely=0.45, anchor=CENTER)
StartButt.place(relx=0.5, rely=0.82, anchor=CENTER)
StartButt.bind('<1>', root1)

#Все переменные
Sc1 = Label(root, width=30, height=15, bg='black')
Sc2 = Label(root, width=15, height=15, bg='black')
Sc3 = Label(root, width=30, height=15, bg='black')
Sc4 = Label(root, width=30, height=7, bg='black')
Sc5 = Label(root, width=15, height=7, bg='black')
Sc6 = Label(root, width=30, height=7, bg='black')
Sc7 = Label(root, width=30, height=7, bg='black')
Sc8 = Label(root, width=15, height=7, bg='black')
Sc9 = Label(root, width=30, height=7, bg='black')
but = Button(root, text='старт', font=("Mastodon Bold", 20), width=20, height=1, bg='beige')
ErrorLabel = Label(root, width=50, height=1, text = 'Ваше имя короче 1 символа, резульат не будет сохранен', fg = 'white', bg='red')
SavedLabel = Label(root, width=50, height=1, text = 'Ваш результат успешно сохранен!', fg = 'white', bg='royalblue')
CloseResultsBut = Button(root, text='Закрыть резултаты', width=20, height=2, font=("Soviet font Regular", ), bg='beige')
ResultsTxt = Text(root, width=100, height=100)
SaveBut = Button(root)
butt = Button(root)
ScoresBut = Button(root)
secretEnt = Text(root, height = 10, width = 20,font=("Mastodon Bold", 20), bg = 'beige', fg ='black')
canv = Canvas(root, width = 300, height = 300, bg = 'black')

secretLab = Label(root, text = 'ПрОДоЛжиИть?&?', width=20, height=2, font=("Determination Mono(RUS BY LYAJK", 11), bg='beige')
butt2 = Button(root)
butt1 = Button(root)

flagClick = False
x1 = [] # Для случайного выбора
comp = [] # Список квадратов на которые надо нажать
user = [] # Спиоск квадратов на которые нажал пользователь
memory_time = 0.2 # Время на которое квадрат загорается зеленым цветом
moves = 1 # Сколько раз пользователь нажал на квадраты
countOfMoves = 1 # Сколько раз пользователю нужно нажать на квадраты
secretLst = [Sc1, Sc9, Sc3, Sc7] # Супер секретная последовательность 
secretFlag = False 
secretErrFlag = False

but.bind('<1>', rand)

Sc1.bind('<1>', F1)
Sc2.bind('<1>', F1)
Sc3.bind('<1>', F1)

Sc4.bind('<1>', F1)
Sc5.bind('<1>', F1)
Sc6.bind('<1>', F1)

Sc7.bind('<1>', F1)
Sc8.bind('<1>', F1)
Sc9.bind('<1>', F1)
root.bind('<Escape>', stopIt)

root.mainloop()




