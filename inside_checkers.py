# Реализация для русские шашки без дамок и функции, заканчивающей игру

import random

# Одна из важнейших функций, анализирующая возможные ходы за сторону, цвет которой в переменной color

def search_moves(position):
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


# Цвет шашек бота (устанавливается)
color = "black"

# Игровое поле
game_area = [[0, 2, 0, 2, 0, 2, 0, 2],
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
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        game_area[iTo][jTo] = game_area[iFr][jFr]
        game_area[iFr][jFr] = 0


    elif abs(fr[0] - to[0]) == 2 and abs(fr[1] - to[1]) == 2:
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        game_area[iTo][jTo] = game_area[iFr][jFr]
        game_area[iFr][jFr] = 0
        game_area[abs((iTo + iFr)) // 2][abs((jTo + jFr)) // 2] = 0

    if iTo == 0:
        game_area[iTo][jTo] = 11

    if iTo == 7:
        game_area[iTo][jTo] = 22

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
def take_go():
    count = 0
    isStop = True
    for i in range(len(taking)):
        for j in range(len(taking[i])):
            if taking[i][j] != []:
                take = taking[i][j][0]
                iTo = take[0]
                jTo = take[1]
                game_area[iTo][jTo] = game_area[i][j]
                game_area[i][j] = 0
                game_area[abs((iTo + i)) // 2][abs((jTo + j)) // 2] = 0
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
        moves_bot(game_area)
        take_go()
