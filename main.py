import tkinter, time
from modules.visual import checkers_board, draw,draw_reversed
from modules.bot import moves_bot, bot_level_1, mark
from global_variables import COORDS, MATRIX_AREA, TAKING, AREA

WHITE_CHECKERS = []
BLACK_CHECKERS = []
DONE = False
QUEEN_Q = False
TAKEE = False
BLACK = False
WHITE = False
STARTED = False
FR = []
CHOSE = False


#Step 1. создание игрового поля
WINDOW = tkinter.Tk()
WINDOW.geometry('500x700')
CANVAS = tkinter.Canvas(WINDOW, height=500, width=500)
label1 = tkinter.Label(text="Нажми левой кнопкой мыши на шашку, двойное нажатие на пустое поле - туда поставится шашка ")
label1.pack()
CANVAS.pack()
WINDOW.title("Шашки")

def motion1(event):
    '''Функция, с помощью которой можно выбрать шашку.'''
    global CHOSE, AREA, MATRIX_AREA, TAKEE, COORDS, TAKING, FR
    MATRIX_AREA = moves_bot(AREA, "white")[0]
    TAKING = moves_bot(AREA, "white")[1]
    for it in range(len(TAKING)):
        for jt in range(len(TAKING[it])):
            if TAKING[it][jt]!=[]:
                TAKEE = True
                break
    for i in range(len(COORDS)):
        for j in range(len(COORDS[i])):
            if abs((COORDS[i][j][0] + COORDS[i][j][2]) // 2 - event.x) < 25 and abs((COORDS[i][j][1] + COORDS[i][j][3]) // 2 - event.y) < 25:
                if(AREA[i][j] == 1 and not CHOSE and not TAKEE):
                    # print("taking: ", TAKING)
                    if MATRIX_AREA[i][j] != []:
                        CHOSE = True
                        FR.append([i, j])
                        FR.append(MATRIX_AREA[i][j])
                        # print(FR)
                        AREA[i][j] = 0
                elif(AREA[i][j] == 11 and not CHOSE and not TAKEE):
                    if MATRIX_AREA[i][j] != []:
                        global QUEEN_Q
                        QUEEN_Q = True
                        CHOSE = True
                        FR.append([i, j])
                        FR.append(MATRIX_AREA[i][j])
                        # print(FR)
                        AREA[i][j] = 0
                elif AREA[i][j] == 1 and not CHOSE and TAKEE:
                    if TAKING[i][j]!=[]:
                        CHOSE = True
                        FR.append([i, j])
                        FR.append(TAKING[i][j])
                        # print(FR)
                        AREA[i][j]=0
                elif AREA[i][j] == 11 and not CHOSE and TAKEE:
                    if TAKING[i][j]!=[]:
                        QUEEN_Q = True
                        CHOSE = True
                        FR.append([i, j])
                        FR.append(TAKING[i][j])
                        # print(FR)
                        AREA[i][j] = 0
    # print(QUEEN_Q, TAKEE, CHOSE)

def motion2(event):
    '''Функцию, с помощью которой можно переместить шашку.'''
    global CHOSE, DONE, TAKEE, QUEEN_Q, FR, AREA
    for i in range(len(COORDS)):
        for j in range(len(COORDS[i])):
            if abs((COORDS[i][j][0] + COORDS[i][j][2]) // 2 - event.x) < 25 and abs((COORDS[i][j][1] + COORDS[i][j][3]) // 2 - event.y) < 25:
                if TAKEE and [i, j] in FR[-1] and CHOSE and QUEEN_Q:
                    if FR[0][0] < i and FR[0][1] < j:
                        for k in range(FR[0][0], i):
                            for t in range(FR[0][1], j):
                                if k-t == i-j and AREA[k][t] == 2 or AREA[k][t] == 22:
                                    AREA[k][t] = 0
                                    break
                    elif FR[0][0] < i and FR[0][1] > j:
                        for k in range(FR[0][0], i):
                            for t in range(j, FR[0][1]):
                                if k + t == i + j and AREA[k][t] == 2 or AREA[k][t] == 22:
                                    AREA[k][t] = 0
                                    break
                    elif FR[0][0] > i and FR[0][1] < j:
                        for k in range(i,FR[0][0]):
                            for t in range(FR[0][1], j):
                                if k + t == i + j and AREA[k][t] == 2 or AREA[k][t] == 22:
                                    AREA[k][t] = 0
                                    break
                    elif FR[0][0] > i and FR[0][1] > j:
                        for k in range(i, FR[0][0]):
                            for t in range(j, FR[0][1]):
                                if k - t == i - j and AREA[k][t] == 2 or AREA[k][t] == 22:
                                    AREA[k][t] = 0
                                    break
                    print(i, j)
                    AREA[i][j] = 11
                    global DONE
                    DONE = True
                    TAKING = moves_bot(AREA,"white")[1]
                    if TAKING[i][j] != []:
                        TAKEE = False
                        QUEEN_Q = False
                        DONE = False
                        CHOSE = False
                        FR = []
                        CANVAS.update()

                elif [i,j] in FR[-1] and CHOSE and TAKEE:
                    if i == 0:
                        AREA[i][j] = 11
                        AREA[(i + FR[0][0]) // 2][(j + FR[0][1]) // 2] = 0
                        DONE = True
                    else:
                        AREA[i][j] = 1
                        AREA[(i + FR[0][0]) // 2][(j + FR[0][1]) // 2] = 0
                        DONE = True
                    TAKING = moves_bot(AREA, "white")[1]
                    if TAKING[i][j] != []:
                        TAKEE = False
                        QUEEN_Q = False
                        DONE = False
                        CHOSE = False
                        FR = []
                        CANVAS.update()
                elif [i,j] in FR[-1] and CHOSE and abs(i - FR[0][0]) == 1 and abs(j - FR[0][1]) == 1 and not QUEEN_Q:
                    if i == 0:
                        AREA[i][j] = 11
                    else:
                        AREA[i][j] = 1
                    DONE = True

                elif QUEEN_Q and [i, j] in FR[-1] and CHOSE:
                    AREA[i][j]=11
                    DONE = True
                elif QUEEN_Q:
                    AREA[FR[0][0]][FR[0][1]] = 11
                    CHOSE = False
                else:
                    AREA[FR[0][0]][FR[0][1]] = 1
                    CHOSE = False
    CANVAS.update()

def startedQ():
    '''Функция, которая начинает игру'''
    global STARTED
    STARTED = True

def finishedQ():
    '''Функция, которая заканчивает игру'''
    global STARTED
    STARTED = False

def blackQ():
    '''Функция, которая говорит, что данные фигуры чёрные'''
    global BLACK
    BLACK = True

def whiteQ():
    '''Функция, которая говорит, что данные фигуры белые'''
    global WHITE
    WHITE = True

buttons = []

def choose_color():
    '''Функция, позволяющая сделать выбор цвета'''
    global buttons
    buttons.append(tkinter.Button(text = "Белые", command = lambda : [whiteQ(),startedQ()]))
    buttons.append(tkinter.Button(text = "Чёрные", command = lambda : [blackQ(),startedQ()]))
    buttons[-1].pack()
    buttons[-2].pack()

def get_back():
    "Функция, которая сделать шаг назад в меню."
    for i in buttons:
        i.pack_forget()


#процесс игры
checkers_board(CANVAS)
buttons = []
buttons.append(tkinter.Button(text = "Против бота", command = lambda :[buttons[0].pack_forget(), buttons[1].pack(),choose_color()]))
buttons.append(tkinter.Button(text = "Назад", command=lambda : [get_back(),buttons[0].pack(), buttons[1].pack(), finishedQ()]))
for item in buttons:
    item.pack()
while not STARTED and (not WHITE or not BLACK):
    time.sleep(0.3)
    CANVAS.update()
if STARTED and WHITE:
    checkers_board(CANVAS)
    CANVAS.bind('<Button-1>', motion1)
    CANVAS.bind('<Double-1>', motion2)
    CANVAS.update()
    while mark(AREA, "white") == "Null" and STARTED:
        CANVAS.delete("all")
        TAKEE = False
        take_again = False
        QUEEN_Q = False
        DONE = False
        CHOSE = False
        checkers_board(CANVAS)
        CANVAS.update()
        draw(AREA, CANVAS)
        print(WHITE_CHECKERS)
        CANVAS.update()
        while not DONE:
            time.sleep(0.3)
            draw(AREA, CANVAS)
            CANVAS.update()
        FR = []
        CANVAS.delete("all")
        checkers_board(CANVAS)
        CANVAS.update()
        draw(AREA, CANVAS)
        time.sleep(0.3)
        print("Сейчас ходит бот")
        CANVAS.update()
        time.sleep(0.5)
        if mark(AREA, "white") != "Null":
            WINDOW.destroy()
            print(mark(AREA, "white"))
            break
        bot_level_1(AREA)
        print("Бот походил")
        draw(AREA, CANVAS)
        CANVAS.update()
elif STARTED and BLACK:
    checkers_board(CANVAS)
    CANVAS.bind('<Button-1>', motion1)
    CANVAS.bind('<Double-1>', motion2)
    CANVAS.update()
    draw_reversed(AREA, CANVAS)
    while mark(AREA, "black") == "Null" and STARTED:
        CANVAS.delete("all")
        checkers_board(CANVAS)
        draw_reversed(AREA, CANVAS)
        CANVAS.update()
        time.sleep(0.3)
        print("Сейчас ходит бот")
        bot_level_1(AREA)
        print("Бот походил")
        CANVAS.delete("all")
        checkers_board(CANVAS)
        draw_reversed(AREA, CANVAS)
        CANVAS.update()
        take_again = False
        TAKEE = False
        QUEEN_Q = False
        DONE = False
        CHOSE = False
        checkers_board(CANVAS)
        CANVAS.update()
        draw_reversed(AREA, CANVAS)
        CANVAS.update()
        if mark(AREA, "black") != "Null":
            WINDOW.destroy()
            print(mark(AREA, "black"))
            break
        while not DONE:
            time.sleep(0.3)
            draw_reversed(AREA, CANVAS)
            CANVAS.update()
        CANVAS.update()
        FR = []
WINDOW.destroy()
if BLACK:
    print(mark(AREA, "black"))
else:
    print(mark(AREA, "white"))

WINDOW.mainloop()
