import random, tkinter, time


#Step 1. создание игрового поля
window = tkinter.Tk()
window.geometry('500x500')
frame = tkinter.Frame(window)
canvas = tkinter.Canvas(window, height=500, width=500)
label1 = tkinter.Label(text="Нажми левой кнопкой мыши на шашку, двойное нажатие на пустое поле - туда поставится шашка ")
label1.pack()
canvas.pack()
window.title("Шашки")

coords = a = [[0] * 8 for i in range(8)]

#
#Часть, созданная Димой
#

matrixArea = [[[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[]]]
color1 = "white"
color2 = "black" # цвет шашек для бота
actual_moves = []
taking = [[[], [],[], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []]]
nes_take = []
queen = []
queen_take = []

def moves_bot(position, color):
    global matrixArea, taking
    matrixArea = [[[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []]]
    taking = [[[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []]]
    if color == "white":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 0:

                            matrixArea[i][j].append([i - 1, j - 1])

                        elif position[i - 1][j - 1] == 2:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:

                                    taking[i][j].append([i - 2, j - 2])

                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 0:

                            matrixArea[i][j].append([i - 1, j + 1])

                        elif position[i - 1][j + 1] == 2:
                            if i - 2 >= 0 and j + 2 < 8:
                                if position[i - 2][j + 2] == 0:
                                    taking[i][j].append([i - 2, j + 2])

                                    matrixArea[i][j].append([i - 2, j + 2])

                    # Проверка на возможность взятия назад
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 2 or position[i + 1][j - 1] == 22:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:
                                    taking[i][j].append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 2 or position[i + 1][j + 1] == 22:
                            if i + 2 < 8 and j + 2 < 8:
                                if position[i + 2][j + 2] == 0:
                                    taking[i][j].append([i + 2, j + 2])

                                    matrixArea[i][j].append([i + 2, j + 2])

    if color == "black":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 2:
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 0:

                            matrixArea[i][j].append([i + 1, j - 1])


                        elif position[i + 1][j - 1] == 1:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:

                                    taking[i][j].append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 0:

                            matrixArea[i][j].append([i + 1, j + 1])

                        elif position[i + 1][j + 1] == 1:
                            if i + 2 < 8 and j + 2 < 8:
                                if position[i + 2][j + 2] == 0:

                                    taking[i][j].append([i + 2, j + 2])

                                    matrixArea[i][j].append([i + 2, j + 2])

                    # Проверка на возможность взятия назад
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 1 or position[i - 1][j - 1] == 11:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:
                                    taking[i][j].append([i - 2, j - 2])
                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 1 or position[i - 1][j + 1] == 11:
                            if i - 2 >= 0 and j + 2 < 8:
                                if position[i - 2][j + 2] == 0:
                                    taking[i][j].append([i - 2, j + 2])

                                    matrixArea[i][j].append([i - 2, j + 2])
#Поиск текущих возможных ходов
def moves_bot1(position, color):
    global matrixArea
    matrixArea = [[[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []]]
    if color == "white":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 0:
                            actual_moves.append([i - 1, j - 1])

                            matrixArea[i][j].append([i - 1, j - 1])

                        elif position[i - 1][j - 1] == 2:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:
                                    nes_take.append([i - 2, j - 2])
                                    taking.append([i - 2, j - 2])

                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 0:
                            actual_moves.append([i - 1, j + 1])

                            matrixArea[i][j].append([i - 1, j + 1])

                        elif position[i - 1][j + 1] == 2:
                            if i - 2 >= 0 and j + 2 < 8:
                                if position[i - 2][j + 2] == 0:
                                    nes_take.append([i - 2, j + 2])
                                    taking.append([i - 2, j + 2])

                                    matrixArea[i][j].append([i - 2, j + 2])

                    # Проверка на возможность взятия назад
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 2 or position[i + 1][j - 1] == 22:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:
                                    taking.append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 2 or position[i + 1][j + 1] == 22:
                            if i + 2 < 8 and j + 2 < 8:
                                if position[i + 2][j + 2] == 0:
                                    taking.append([i + 2, j + 2])

                                    matrixArea[i][j].append([i + 2, j + 2])

                elif position[i][j] == 11:
                    iD = i + 1
                    jD = j + 1
                    while iD != 8 and jD != 8:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            if iD + 1 < 8 and jD + 1 < 8:
                                if position[iD + 1][jD + 1] == 0:
                                    queen_take.append([iD + 1, jD + 1])

                                    matrixArea[i][j].append([iD + 1, jD + 1])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break
                        iD += 1
                        jD += 1

                    iD = i - 1
                    jD = j - 1
                    while iD != -1 and jD != -1:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            if iD - 1 >= 0 and jD - 1 >= 0:
                                if position[iD - 1][jD - 1] == 0:
                                    queen_take.append([iD - 1, jD - 1])

                                    matrixArea[i][j].append([iD - 1, jD - 1])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break
                        iD -= 1
                        jD -= 1

                    iD = i + 1
                    jD = j - 1
                    while iD != 8 and jD != -1:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            if iD + 1 < 8 and jD - 1 >= 0:
                                if position[iD + 1][jD - 1] == 0:
                                    queen_take.append([iD + 1, jD - 1])

                                    matrixArea[i][j].append([iD + 1, jD - 1])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break
                        iD += 1
                        jD -= 1

                    iD = i - 1
                    jD = j + 1
                    while iD != -1 and jD != 8:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            if iD - 1 >= 0 and jD + 1 < 8:
                                if position[iD - 1][jD + 1] == 0:
                                    queen_take.append([iD - 1, jD + 1])

                                    matrixArea[i][j].append([iD - 1, jD + 1])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break
                        iD -= 1
                        jD += 1
    if color == "black":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 2:
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 0:
                            ##Для кнопки
                            actual_moves.append([i + 1, j - 1])
                            # ##Для кнопки
                            matrixArea[i][j].append([i + 1, j - 1])


                        elif position[i + 1][j - 1] == 1:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:
                                    nes_take.append([i + 2, j - 2])
                                    taking.append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 0:
                            actual_moves.append([i + 1, j + 1])

                            matrixArea[i][j].append([i + 1, j + 1])

                        elif position[i + 1][j + 1] == 1:
                            if i + 2 < 8 and j + 2 < 8:
                                if position[i + 2][j + 2] == 0:
                                    nes_take.append([i + 2, j + 2])
                                    taking.append([i + 2, j + 2])

                                    matrixArea[i][j].append([i + 2, j + 2])

                    # Проверка на возможность взятия назад
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 1 or position[i - 1][j - 1] == 11:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:
                                    taking.append([i - 2, j - 2])
                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 1 or position[i - 1][j + 1] == 11:
                            if i - 2 >= 0 and j + 2 < 8:
                                if position[i - 2][j + 2] == 0:
                                    taking.append([i - 2, j + 2])

                                    matrixArea[i][j].append([i - 2, j + 2])
                elif position[i][j] == 22:
                    iD = i + 1
                    jD = j + 1
                    while iD != 8 and jD != 8:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            if iD + 1 < 8 and jD + 1 < 8:
                                if position[iD + 1][jD + 1] == 0:
                                    queen_take.append([iD + 1, jD + 1])

                                    matrixArea[i][j].append([iD + 1, jD + 1])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break
                        iD += 1
                        jD += 1

                    iD = i - 1
                    jD = j - 1
                    while iD != -1 and jD != -1:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            if iD - 1 >= 0 and jD - 1 >= 0:
                                if position[iD - 1][jD - 1] == 0:
                                    queen_take.append([iD - 1, jD - 1])

                                    matrixArea[i][j].append([iD - 1, jD - 1])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break
                        iD -= 1
                        jD -= 1

                    iD = i + 1
                    jD = j - 1
                    while iD != 8 and jD != -1:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea.append([iD, jD])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            if iD + 1 < 8 and jD - 1 >= 0:
                                if position[iD + 1][jD - 1] == 0:
                                    queen_take.append([iD + 1, jD - 1])

                                    matrixArea[i][j].append([iD + 1, jD - 1])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break
                        iD += 1
                        jD -= 1

                    iD = i - 1
                    jD = j + 1
                    while iD != -1 and jD != 8:
                        if position[iD][jD] == 0:
                            queen.append([iD, jD])

                            matrixArea[i][j].append([iD, jD])

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            if iD - 1 >= 0 and jD + 1 < 8:
                                if position[iD - 1][jD + 1] == 0:
                                    queen_take.append([iD - 1, jD + 1])

                                    matrixArea[i][j].append([iD - 1, jD + 1])

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break
                        iD -= 1
                        jD += 1

def move_bot(fr, to):
    if abs(fr[0] - to[0]) == 1 and abs(fr[1] - to[1]) == 1:
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        area[iTo][jTo] = area[iFr][jFr]
        area[iFr][jFr] = 0


    elif abs(fr[0] - to[0]) == 2 and abs(fr[1] - to[1]) == 2:
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        area[iTo][jTo] = area[iFr][jFr]
        area[iFr][jFr] = 0
        area[abs((iTo + iFr)) // 2][abs((jTo + jFr)) // 2] = 0

    if iTo == 0:
        area[iTo][jTo] = 11

    if iTo == 7:
        area[iTo][jTo] = 22

    return True

# Функция бота 1 уровня, делающего обязательные взятия и рандомные ходы
def bot_level_1():
    time.sleep(0.3)
    global matrixArea
    matrixArea = [[[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []]]
    forLevel1 = []
    isTake = False
    ask = take_go()

    if ask == "No":
        moves_bot(area, "black")
        for i in range(len(matrixArea)):
            for j in range(len(matrixArea[i])):
                if matrixArea[i][j] != [] and area[i][j] == 2 or area[i][j] == 22:
                    forLevel1.append([[i, j], matrixArea[i][j]])
            print(matrixArea[i])
        hod = random.choice(forLevel1)
        print(hod)
        fr1 = hod[0]
        to1 = random.choice(hod[1])
        move_bot(fr1, to1)

# Функция для обязательного взятия
def take_go():
    moves_bot(area, "black")
    count = 0
    isStop = True
    for i in range(len(taking)):
        for j in range(len(taking[i])):
            if taking[i][j] != []:
                take = taking[i][j][0]
                iTo = take[0]
                jTo = take[1]
                area[iTo][jTo] = area[i][j]
                area[i][j] = 0
                area[abs((iTo + i)) // 2][abs((jTo + j)) // 2] = 0
                isStop = False
                count += 1
                break

    if isStop and count == 0:
        # Взятий не было
        return "No"
    elif isStop and count != 0:
        # Взятия были
        return "Yes"
    elif not isStop and count != 0:
        # Пытаемся продолжить брать
        for i in range(len(taking)):
            for j in range(len(taking[i])):
                taking[i][j] = []
        for i in range(len(matrixArea)):
            for j in range(len(matrixArea[i])):
                matrixArea[i][j] = []
        moves_bot(area, "black")
        take_go()

#ход бота
def move_bot1(Fr, To):
    if abs(Fr[0] - To[0]) == 1 and abs(Fr[1] - To[1]) == 1:
        iFr = Fr[0]
        jFr = Fr[1]
        iTo = To[0]
        jTo = To[1]
        area[iTo][jTo] = area[iFr][jFr]
        area[iFr][jFr] = 0


    elif abs(Fr[0] - To[0]) == 2 and abs(Fr[1] - To[1]) == 2:
        iFr = Fr[0]
        jFr = Fr[1]
        iTo = To[0]
        jTo = To[1]
        area[iTo][jTo] = area[iFr][jFr]
        area[iFr][jFr] = 0
        area[abs((iTo + iFr)) // 2][abs((jTo + jFr)) // 2] = 0

    if iTo == 0:
        area[iTo][jTo] = 11

    if iTo == 7:
        area[iTo][jTo] = 22

    draw(area)
    return True


# Без учёта условия обязательного взятия

def bot_level_1_1():
    global matrixArea, area
    matrixArea = [[[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []]]
    forLevel1 = []
    if taking == []:
        moves_bot(area, "black")
        for i in range(len(matrixArea)):
            for j in range(len(matrixArea[i])):
                if matrixArea[i][j] != [] and area[i][j] == 2 or area[i][j] == 22:
                    forLevel1.append([[i, j], matrixArea[i][j]])
            print(matrixArea[i])
        hod = random.choice(forLevel1)
        print(hod)
        fr1 = hod[0]
        to1 = random.choice(hod[1])
        move_bot(fr1, to1)
    else:
        print("taking: ", taking)
        moves_bot(area, "black")
        for i in range(len(matrixArea)):
            for j in range(len(matrixArea[i])):
                if matrixArea[i][j] != [] and area[i][j] == 2 or area[i][j] == 22:
                    forLevel1.append([[i, j], matrixArea[i][j]])
            print(matrixArea[i])
        hod = random.choice(forLevel1)
        print(hod)
        fr1 = hod[0]
        to1 = random.choice(hod[1])
        move_bot(fr1, to1)

#
#Далее создано мной
#

# Функция создания игрового поля
def checkers_board():
    canvas.delete("all")
    # ---------------------
    # COLUMN 1
    # ---------------------
    re1_coord = (40, 30, 90, 80)
    coords[0][0] = re1_coord
    re1 = canvas.create_rectangle(re1_coord, outline="tomato", fill="tomato", tags="red")
    bl2_coord = (40, 80, 90, 130)
    coords[1][0] = bl2_coord
    bl2 = canvas.create_rectangle(bl2_coord, outline="black", fill="black", tags="black")
    re3_coord = (40, 130, 90, 180)
    coords[2][0] = re3_coord
    re3 = canvas.create_rectangle(re3_coord, outline="tomato", fill="tomato", tags="red")
    bl4_coord = (40, 180, 90, 230)
    coords[3][0] = bl4_coord
    bl4 = canvas.create_rectangle(bl4_coord, outline="black", fill="black", tags="black")
    re5_coord = (40, 230, 90, 280)
    coords[4][0] = re5_coord
    re5 = canvas.create_rectangle(re5_coord, outline="tomato", fill="tomato", tags="red")
    bl6_coord = (40, 280, 90, 330)
    coords[5][0] = bl6_coord
    bl6 = canvas.create_rectangle(bl6_coord, outline="black", fill="black", tags="black")
    re7_coord = (40, 330, 90, 380)
    coords[6][0] = re7_coord
    re7 = canvas.create_rectangle(re7_coord, outline="tomato", fill="tomato", tags="red")
    bl8_coord = (40, 380, 90, 430)
    coords[7][0] = bl8_coord
    bl8 = canvas.create_rectangle(bl8_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 2
    # ---------------------
    bl9_coord = (90, 30, 140, 80)
    coords[0][1] = bl9_coord
    bl9 = canvas.create_rectangle(bl9_coord, outline="black", fill="black", tags="black")
    re10_coord = (90, 80, 140, 130)
    coords[1][1] = re10_coord
    re10 = canvas.create_rectangle(re10_coord, outline="tomato", fill="tomato", tags="red")
    bl11_coord = (90, 130, 140, 180)
    coords[2][1] = bl11_coord
    bl11 = canvas.create_rectangle(bl11_coord, outline="black", fill="black", tags="black")
    re12_coord = (90, 180, 140, 230)
    coords[3][1] = re12_coord
    re12 = canvas.create_rectangle(re12_coord, outline="tomato", fill="tomato", tags="red")
    bl13_coord = (90, 230, 140, 280)
    coords[4][1] = bl13_coord
    bl13 = canvas.create_rectangle(bl13_coord, outline="black", fill="black", tags="black")
    re14_coord = (90, 280, 140, 330)
    coords[5][1] = re14_coord
    re14 = canvas.create_rectangle(re14_coord, outline="tomato", fill="tomato", tags="red")
    bl15_coord = (90, 330, 140, 380)
    coords[6][1] = bl15_coord
    bl15 = canvas.create_rectangle(bl15_coord, outline="black", fill="black", tags="black")
    re16_coord = (90, 380, 140, 430)
    coords[7][1] = re16_coord
    re16 = canvas.create_rectangle(re16_coord, outline="tomato", fill="tomato", tags="red")

    # ---------------------
    # COLUMN 3
    # ---------------------
    re17_coord = (140, 30, 190, 80)
    coords[0][2] = re17_coord
    re17 = canvas.create_rectangle(re17_coord, outline="tomato", fill="tomato", tags="red")
    bl18_coord = (140, 80, 190, 130)
    coords[1][2] = bl18_coord
    bl18 = canvas.create_rectangle(bl18_coord, outline="black", fill="black", tags="black")
    re19_coord = (140, 130, 190, 180)
    coords[2][2] = re19_coord
    re19 = canvas.create_rectangle(re19_coord, outline="tomato", fill="tomato", tags="red")
    bl20_coord = (140, 180, 190, 230)
    coords[3][2] = bl20_coord
    bl20 = canvas.create_rectangle(bl20_coord, outline="black", fill="black", tags="black")
    re21_coord = (140, 230, 190, 280)
    coords[4][2] = re21_coord
    re21 = canvas.create_rectangle(re21_coord, outline="tomato", fill="tomato", tags="red")
    bl22_coord = (140, 280, 190, 330)
    coords[5][2] = bl22_coord
    bl22 = canvas.create_rectangle(bl22_coord, outline="black", fill="black", tags="black")
    re23_coord = (140, 330, 190, 380)
    coords[6][2] = re23_coord
    re23 = canvas.create_rectangle(re23_coord, outline="tomato", fill="tomato", tags="red")
    bl24_coord = (140, 380, 190, 430)
    coords[7][2] = bl24_coord
    bl24 = canvas.create_rectangle(bl24_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 4
    # ---------------------
    bl25_coord = (190, 30, 240, 80)
    coords[0][3] = bl25_coord
    bl25 = canvas.create_rectangle(bl25_coord, outline="black", fill="black", tags="black")
    re26_coord = (190, 80, 240, 130)
    coords[1][3] = re26_coord
    re26 = canvas.create_rectangle(re26_coord, outline="tomato", fill="tomato", tags="red")
    bl27_coord = (190, 130, 240, 180)
    coords[2][3] = bl27_coord
    bl27 = canvas.create_rectangle(bl27_coord, outline="black", fill="black", tags="black")
    re28_coord = (190, 180, 240, 230)
    coords[3][3] = re28_coord
    re28 = canvas.create_rectangle(re28_coord, outline="tomato", fill="tomato", tags="red")
    bl29_coord = (190, 230, 240, 280)
    coords[4][3] = bl29_coord
    bl29 = canvas.create_rectangle(bl29_coord, outline="black", fill="black", tags="black")
    re30_coord = (190, 280, 240, 330)
    coords[5][3] = re30_coord
    re30 = canvas.create_rectangle(re30_coord, outline="tomato", fill="tomato", tags="red")
    bl31_coord = (190, 330, 240, 380)
    coords[6][3] = bl31_coord
    bl31 = canvas.create_rectangle(bl31_coord, outline="black", fill="black", tags="black")
    re32_coord = (190, 380, 240, 430)
    coords[7][3] = re32_coord
    re32 = canvas.create_rectangle(re32_coord, outline="tomato", fill="tomato", tags="red")

    # ---------------------
    # COLUMN 5
    # ---------------------
    re33_coord = (240, 30, 290, 80)
    coords[0][4] = re33_coord
    re33 = canvas.create_rectangle(re33_coord, outline="tomato", fill="tomato", tags="red")
    bl34_coord = (240, 80, 290, 130)
    coords[1][4] = bl34_coord
    bl34 = canvas.create_rectangle(bl34_coord, outline="black", fill="black", tags="black")
    re35_coord = (240, 130, 290, 180)
    coords[2][4] = re35_coord
    re35 = canvas.create_rectangle(re35_coord, outline="tomato", fill="tomato", tags="red")
    bl36_coord = (240, 180, 290, 230)
    coords[3][4] = bl36_coord
    bl36 = canvas.create_rectangle(bl36_coord, outline="black", fill="black", tags="black")
    re37_coord = (240, 230, 290, 280)
    coords[4][4] = re37_coord
    re37 = canvas.create_rectangle(re37_coord, outline="tomato", fill="tomato", tags="red")
    bl38_coord = (240, 280, 290, 330)
    coords[5][4] = bl38_coord
    bl38 = canvas.create_rectangle(bl38_coord, outline="black", fill="black", tags="black")
    re39_coord = (240, 330, 290, 380)
    coords[6][4] = re39_coord
    re39 = canvas.create_rectangle(re39_coord, outline="tomato", fill="tomato", tags="red")
    bl40_coord = (240, 380, 290, 430)
    coords[7][4] = bl40_coord
    bl40 = canvas.create_rectangle(bl40_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 6
    # ---------------------
    bl41_coord = (290, 30, 340, 80)
    coords[0][5] = bl41_coord
    bl41 = canvas.create_rectangle(bl41_coord, outline="black", fill="black", tags="black")
    re42_coord = (290, 80, 340, 130)
    coords[1][5] = re42_coord
    re42 = canvas.create_rectangle(re42_coord, outline="tomato", fill="tomato", tags="red")
    bl43_coord = (290, 130, 340, 180)
    coords[2][5] = bl43_coord
    bl43 = canvas.create_rectangle(bl43_coord, outline="black", fill="black", tags="black")
    re44_coord = (290, 180, 340, 230)
    coords[3][5] = re44_coord
    re44 = canvas.create_rectangle(re44_coord, outline="tomato", fill="tomato", tags="red")
    bl45_coord = (290, 230, 340, 280)
    coords[4][5] = bl45_coord
    bl45 = canvas.create_rectangle(bl45_coord, outline="black", fill="black", tags="black")
    re46_coord = (290, 280, 340, 330)
    coords[5][5] = re46_coord
    re46 = canvas.create_rectangle(re46_coord, outline="tomato", fill="tomato", tags="red")
    bl47_coord = (290, 330, 340, 380)
    coords[6][5] = bl47_coord
    bl47 = canvas.create_rectangle(bl47_coord, outline="black", fill="black", tags="black")
    re48_coord = (290, 380, 340, 430)
    coords[7][5] = re48_coord
    re48 = canvas.create_rectangle(re48_coord, outline="tomato", fill="tomato", tags="red")
    canvas.pack()

    # ---------------------
    # COLUMN 7
    # ---------------------
    re49_coord = (340, 30, 390, 80)
    coords[0][6] = re49_coord
    re49 = canvas.create_rectangle(re49_coord, outline="tomato", fill="tomato", tags="red")
    bl50_coord = (340, 80, 390, 130)
    coords[1][6] = bl50_coord
    bl50 = canvas.create_rectangle(bl50_coord, outline="black", fill="black", tags="black")
    re51_coord = (340, 130, 390, 180)
    coords[2][6] = re51_coord
    re51 = canvas.create_rectangle(re51_coord, outline="tomato", fill="tomato", tags="red")
    bl52_coord = (340, 180, 390, 230)
    coords[3][6] = bl52_coord
    bl52 = canvas.create_rectangle(bl52_coord, outline="black", fill="black", tags="black")
    re53_coord = (340, 230, 390, 280)
    coords[4][6] = re53_coord
    re53 = canvas.create_rectangle(re53_coord, outline="tomato", fill="tomato", tags="red")
    bl54_coord = (340, 280, 390, 330)
    coords[5][6] = bl54_coord
    bl54 = canvas.create_rectangle(bl54_coord, outline="black", fill="black", tags="black")
    re55_coord = (340, 330, 390, 380)
    coords[6][6] = re55_coord
    re55 = canvas.create_rectangle(re55_coord, outline="tomato", fill="tomato", tags="red")
    bl56_coord = (340, 380, 390, 430)
    coords[7][6] = bl56_coord
    bl56 = canvas.create_rectangle(bl56_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 8
    # ---------------------
    bl57_coord = (390, 30, 440, 80)
    coords[0][7] = bl57_coord
    bl57 = canvas.create_rectangle(bl57_coord, outline="black", fill="black", tags="black")
    re58_coord = (390, 80, 440, 130)
    coords[1][7] = re58_coord
    re58 = canvas.create_rectangle(re58_coord, outline="tomato", fill="tomato", tags="red")
    bl59_coord = (390, 130, 440, 180)
    coords[2][7] = bl59_coord
    bl59 = canvas.create_rectangle(bl59_coord, outline="black", fill="black", tags="black")
    re60_coord = (390, 180, 440, 230)
    coords[3][7] = re60_coord
    re60 = canvas.create_rectangle(re60_coord, outline="tomato", fill="tomato", tags="red")
    bl61_coord = (390, 230, 440, 280)
    coords[4][7] = bl61_coord
    bl61 = canvas.create_rectangle(bl61_coord, outline="black", fill="black", tags="black")
    re62_coord = (390, 280, 440, 330)
    coords[5][7] = re62_coord
    re62 = canvas.create_rectangle(re62_coord, outline="tomato", fill="tomato", tags="red")
    bl63_coord = (390, 330, 440, 380)
    coords[6][7] = bl63_coord
    bl63 = canvas.create_rectangle(bl63_coord, outline="black", fill="black", tags="black")
    re64_coord = (390, 380, 440, 430)
    coords[7][7] = re64_coord
    re64 = canvas.create_rectangle(re64_coord, outline="tomato", fill="tomato", tags="red")

# Шашечная матрица
area = [[0, 2, 0, 2, 0, 2, 0, 2],
[2, 0, 2, 0, 2, 0, 2, 0],
[0, 2, 0, 2, 0, 2, 0, 2],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0]]

# Функция помещения шашек со списка на картинку
def draw(lst):
    white_checkers = []
    black_checkers = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if area[i][j] == 2:
                black_checkers.append(canvas.create_oval(coords[i][j][0]+5,coords[i][j][1]+5,coords[i][j][2]-5,coords[i][j][3]-5, outline="yellow", fill="yellow", tags="yellow"))
            elif area[i][j] == 1:
                ci = canvas.create_oval(coords[i][j][0]+5,coords[i][j][1]+5, coords[i][j][2]-5, coords[i][j][3]-5, outline="white", fill="white", tags="white")
                white_checkers.append(ci)
            elif area[i][j] == 22:
                black_checkers.append(canvas.create_oval(coords[i][j][0]+5,coords[i][j][1]+5,coords[i][j][2]-5,coords[i][j][3]-5, outline="red", fill="yellow", tags="yellow"))
            elif area[i][j] == 11:
                ci = canvas.create_oval(coords[i][j][0] + 5, coords[i][j][1] + 5, coords[i][j][2] - 5,
                                        coords[i][j][3] - 5, outline="red", fill="white", tags="white")
                white_checkers.append(ci)


    canvas.update()

queen_q = False

def motion1(event):
    global chose
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            if abs((coords[i][j][0]+coords[i][j][2])//2 - event.x) < 25 and abs((coords[i][j][1]+coords[i][j][3])//2 - event.y) < 25:
                if(area[i][j] == 1 and not chose):
                    moves_bot(area, "white")
                    if matrixArea[i][j] != []:
                        chose = True
                        fr.append([i, j])
                        fr.append(matrixArea[i][j])
                        print(fr)
                        area[i][j] = 0
                elif(area[i][j] == 11 and not chose):
                    moves_bot(area, "white")
                    if matrixArea[i][j] != []:
                        global queen_q
                        queen_q = True
                        chose = True
                        fr.append([i, j])
                        fr.append(matrixArea[i][j])
                        print(fr)
                        area[i][j] = 0
    draw(area)

done = False

def motion2(event):
    global chose
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            if abs((coords[i][j][0]+coords[i][j][2])//2 - event.x) < 25 and abs((coords[i][j][1]+coords[i][j][3])//2 - event.y) < 25:
                if queen_q and [i, j] in fr[-1] and chose:
                    if fr[0][0] < i and fr[0][1] < j:
                        if area[i - 1][j - 1] == 2 or area[i - 1][j - 1] == 22:
                            area[i - 1][j - 1] = 0
                    elif fr[0][0] < i and fr[0][1] > j:
                        if area[i - 1][j + 1] == 2 or area[i - 1][j + 1] == 22:
                            area[i - 1][j + 1] = 0
                    elif fr[0][0] > i and fr[0][1] < j:
                        if area[i + 1][j - 1] == 2 or area[i + 1][j - 1] == 22:
                            area[i + 1][j - 1] = 0
                    elif fr[0][0] > i and fr[0][1] > j:
                        if area[i + 1][j + 1] == 2 or area[i + 1][j + 1] == 22:
                            area[i + 1][j + 1] = 0
                    print(i, j)
                    area[i][j] = 11
                    global done
                    done = True
                elif [i,j] in fr[-1] and chose and abs(i - fr[0][0]) == 2:
                    if i == 0:
                        area[i][j] = 11
                        area[(i + fr[0][0]) // 2][(j + fr[0][1]) // 2] = 0
                        done = True
                    else:
                        area[i][j] = 1
                        area[(i + fr[0][0]) // 2][(j + fr[0][1]) // 2] = 0
                        done = True
                elif [i,j] in fr[-1] and chose and abs(i - fr[0][0]) == 1 and abs(j - fr[0][1])==1:
                    if i == 0:
                        area[i][j] = 11
                    else:
                        area[i][j] = 1
                    done = True

                elif queen_q:
                    area[fr[0][0]][fr[0][1]] = 11
                    chose = False
                else:
                    area[fr[0][0]][fr[0][1]] = 1
                    chose = False

    draw(area)

def clear():
    for widget in frame.winfo_children():
        widget.destroy()

def mark(position):
    winWhite = False
    winBlack = False
    for i in range(len(position)):
        if position[i].count(1) != 0 or position[i].count(11) != 0:
            winWhite = True
        if position[i].count(2) != 0 or position[i].count(22) != 0:
            winBlack = True
    if winWhite and not winBlack:
        return "Белые победили"
    elif not winWhite and winBlack:
        return "Чёрные победили"
    return "Null"

buttons = []

def choose_color():
    global buttons
    buttons.append(tkinter.Button(text = "Белые"))
    buttons.append(tkinter.Button(text = "Чёрные"))
    buttons[-1].pack()
    buttons[-2].pack()

def get_back():
    for i in buttons:
        i.pack_forget()


#создание поля
checkers_board()
fr = []
buttons = []
buttons.append(tkinter.Button(text = "Против бота", command = lambda :[buttons[0].pack_forget(), buttons[1].pack_forget(),choose_color()]))
buttons.append(tkinter.Button(text = "Против друга"))
buttons.append(tkinter.Button(text = "Назад", command=lambda : [get_back(),buttons[0].pack(), buttons[1].pack(), buttons[2].pack()]))
for item in buttons:
    item.pack()
done = False
chose = False
canvas.bind('<Button-1>', motion1)
canvas.bind('<Double-1>', motion2)
while mark(area) == "Null":
    queen_q = False
    done = False
    chose = False
    checkers_board()
    canvas.update()
    draw(area)
    canvas.update()
    while not done:
        time.sleep(0.5)
        canvas.update()
    canvas.update()
    fr = []
    print("Сейчас ходит бот")
    bot_level_1()
    print("Бот походил")
    draw(area)
    canvas.update()
print(mark(area))
#    clear()

window.mainloop()
