# Осталось сделать: 1) обязательные взятия для дамки(больше 1), 2) 2) Бот 2 уровня

import random

# Одна из важнейших функций, анализирующая возможные ходы за сторону, цвет которой в переменной color

def moves_bot(position):
    if color == "white":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 0:

                            matrixArea[i][j].append([i - 1, j - 1])

                        elif position[i - 1][j - 1] == 2 or position[i - 1][j - 1] == 22:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:

                                    taking[i][j].append([i - 2, j - 2])

                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 0:

                            matrixArea[i][j].append([i - 1, j + 1])

                        elif position[i - 1][j + 1] == 2 or position[i - 1][j + 1] == 22:
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


                elif position[i][j] == 11:
                    iD = i + 1
                    jD = j + 1
                    while iD != 8 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD,jD])
                            iD += 1
                            jD += 1
                            take = False
                            while iD != 8 and jD != 8 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0<=iD+1<= 7 and 0<=jD+1<= 7 and take == False and (position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD+=1
                                    jD+=1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD += 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD += 1
                            jD += 1
                            while iD != 8 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break

                    iD = i - 1
                    jD = j - 1
                    while iD != -1 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD -= 1
                            take = False
                            while iD != -1 and jD != -1 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0 <= iD - 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD -= 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD -= 1
                            jD -= 1
                            while iD != -1 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break


                    iD = i + 1
                    jD = j - 1
                    while iD != 8 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD += 1
                            jD -= 1
                            take = False
                            while iD != 8 and jD != -1 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0 <= iD + 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD += 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD += 1
                            jD -= 1
                            while iD != 8 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break

                    iD = i - 1
                    jD = j + 1
                    while iD != -1 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD += 1
                            take = False
                            while iD != -1 and jD != 8 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0 <= iD - 1 <= 7 and 0 <= jD + 1 <= 7 and take == False and (
                                        position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD -= 1
                                    jD += 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD += 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD -= 1
                            jD += 1
                            while iD != -1 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break


    if color == "black":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 2:
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 0:
                            matrixArea[i][j].append([i + 1, j - 1])

                        elif position[i + 1][j - 1] == 1 or position[i + 1][j - 1] == 11:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:

                                    taking[i][j].append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 0:

                            matrixArea[i][j].append([i + 1, j + 1])

                        elif position[i + 1][j + 1] == 1 or position[i + 1][j + 1] == 11:
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



                elif position[i][j] == 22:
                    iD = i + 1
                    jD = j + 1
                    while iD != 8 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD,jD])
                            iD += 1
                            jD += 1
                            take = False
                            while iD != 8 and jD != 8 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0<=iD+1<= 7 and 0<=jD+1<= 7 and take == False and (position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD+=1
                                    jD+=1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD += 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD += 1
                            jD += 1
                            while iD != 8 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break

                    iD = i - 1
                    jD = j - 1
                    while iD != -1 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD -= 1
                            take = False
                            while iD != -1 and jD != -1 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0 <= iD - 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD -= 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD -= 1
                            jD -= 1
                            while iD != -1 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break


                    iD = i + 1
                    jD = j - 1
                    while iD != 8 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD += 1
                            jD -= 1
                            take = False
                            while iD != 8 and jD != -1 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0 <= iD + 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD += 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD += 1
                            jD -= 1
                            while iD != 8 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break

                    iD = i - 1
                    jD = j + 1
                    while iD != -1 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD += 1
                            take = False
                            while iD != -1 and jD != 8 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0 <= iD - 1 <= 7 and 0 <= jD + 1 <= 7 and take == False and (
                                        position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD -= 1
                                    jD += 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD += 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD -= 1
                            jD += 1
                            while iD != -1 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break


# Цвет шашек бота (устанавливается)
color = "white"

# Игровое поле
area = [[0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]]

# Матрица ходов
matrixArea = [[[], [],[], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []]]

# Матрица взятий
taking = [[[], [],[], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], []]]

# Функция для программы, реализующей ход бота.
# Изменяет положение шашек на текущем игровом поле, производя ход в матрице.
def move_bot(fr, to):
    if abs(fr[0] - to[0]) == 1 and abs(fr[1] - to[1]) == 1:
        shape = area[fr[0]][fr[1]];
        if shape == 1 and to[0] == 0:
            shape = 11
        elif shape == 2 and to[0] == 7:
            shape = 22
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        area[iTo][jTo] = shape
        area[iFr][jFr] = 0



    elif abs(fr[0] - to[0]) == 2 and abs(fr[1] - to[1]) == 2:
        shape = area[fr[0]][fr[1]];
        if shape == 1 and to[0] == 0:
            shape = 11
        elif shape == 2 and to[0] == 7:
            shape = 22
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        area[iTo][jTo] = shape
        area[iFr][jFr] = 0
        area[abs((iTo + iFr)) // 2][abs((jTo + jFr)) // 2] = 0

    return True

# Функция бота 1 уровня, делающего обязательные взятия и рандомные ходы
def bot_level_1():
        forLevel1 = []
        isTake = False
        ask = take_go()

        if ask == "No":
            for i in range(len(matrixArea)):
                for j in range(len(matrixArea[i])):
                    if matrixArea[i][j] != []:
                        forLevel1.append([[i, j], matrixArea[i][j]])

            hod = random.choice(forLevel1)
            fr = hod[0]
            to = random.choice(hod[1])
            move_bot(fr, to)

# Функция для обязательного взятия
# На данный момент проходится по матрице взятий и берёт первое встретившиеся возможное взятие
def take_go(iT = "Null", jT = "Null"):
    count = 0
    isStop = True
    if iT != "Null":
        if taking[iT][jT] != []:
            take = taking[iT][jT][0]
            iTo = take[0]
            jTo = take[1]
            area[iTo][jTo] = area[iT][jT]
            area[iT][jT] = 0
            area[abs((iTo + iT)) // 2][abs((jTo + jT)) // 2] = 0
            isStop = False
            count += 1
            iT = iTo
            jT = jTo

    else:
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
                    iT = iTo
                    jT = jTo
                    break
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
        moves_bot(area)
        take_go(iT,jT)

# Функция для создания правильного взятия подряд дамкой
def take_queen(moves_queen):
    areaIn = area[:]


test_position = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0 ,0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

# print("Взятия")
# moves_bot(test_position)
# for i in taking:
#     print(i)
# print("Ходы")
# for i in matrixArea:
#     print(i)



