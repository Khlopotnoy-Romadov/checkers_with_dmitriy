# Ру́сские ша́шки — традиционный и наиболее популярный вид шашек в России, странах бывшего СССР и в Израиле. Цель игры — лишить противника возможности хода
# путём взятия или запирания всех его шашек (в обратных русских шашках цель противоположна — лишить себя возможности хода).
#
#
# Набор шашек, типичный для стран бывшего СССР
# Отличительные особенности:
#
# Шашки ходят только по клеткам тёмного цвета.
# Доска расположена так, чтобы угловое поле внизу слева со стороны игрока было тёмным.
# Простая шашка бьёт вперёд и назад, дамка ходит и бьёт на любое поле диагонали.
# Во время боя простая шашка может превратиться в дамку и сразу продолжить бой по правилам дамки.
# При наличии нескольких вариантов боя можно выбрать любой из них.
import random

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

# 1 - белая шашка, 11 - белая дамка
# 2 - чёрная шашка, 22 - чёрная дамка


# Функция проверки на конец игры
# Стоит переделать, учитывая правило об отсутствии ходов и ничьи
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


test_mark = [[0,1,1],[0,0,0]]
#print(mark(test_mark)) # Успешно


status = mark(area) #текущее состояние
color = "black" # цвет шашек для бота

actual_moves = []
taking = []
#necessarily = False # условие для взятия
nes_take = [] # анализ поля, откуда проверять дальнейшее взятие
#transfer = False
queen = []
queen_take = []




##### Сделать анализ дальнейших взятий




test_move = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


#Поиск текущих возможных ходов
def moves_bot(position):
        if color == "white":
                for i in range(len(position)):
                        for j in range(len(position[i])):
                                if position[i][j] == 1:
                                        if i - 1 >= 0 and j - 1 >= 0:
                                                if position[i-1][j-1] == 0:
                                                        actual_moves.append([i-1,j-1])

                                                        matrixArea[i][j].append([i-1,j-1])

                                                elif position[i-1][j-1] == 2:
                                                        if i - 2 >= 0 and j - 2 >= 0:
                                                                if position[i-2][j-2] == 0:
                                                                        nes_take.append([i - 2, j - 2])
                                                                        taking.append([i-2,j-2])

                                                                        matrixArea[i][j].append([i - 2, j - 2])

                                        if i - 1 >= 0 and j + 1 < 8:
                                                if position[i-1][j+1] == 0:
                                                        actual_moves.append([i-1,j+1])

                                                        matrixArea[i][j].append([i - 1, j + 1])

                                                elif position[i-1][j+1] == 2:
                                                        if i - 2 >= 0 and j + 2 < 8:
                                                                if position[i-2][j+2] == 0:
                                                                        nes_take.append([i - 2, j + 2])
                                                                        taking.append([i-2,j+2])

                                                                        matrixArea[i][j].append([i - 2, j + 2])


                                        # Проверка на возможность взятия назад
                                        if i + 1 < 8 and j - 1 >= 0:
                                                if position[i+1][j-1] == 2 or position[i+1][j-1] == 22:
                                                        if i + 2 < 8 and j - 2 >= 0:
                                                                if position[i+2][j-2] == 0:
                                                                        taking.append([i+2,j-2])

                                                                        matrixArea[i][j].append([i + 2, j - 2])

                                        if i + 1 < 8 and j + 1 < 8:
                                                if position[i+1][j+1] == 2 or position[i+1][j+1] == 22:
                                                        if i + 2 < 8 and j + 2 < 8:
                                                                if position[i+2][j+2] == 0:
                                                                        taking.append([i+2,j+2])

                                                                        matrixArea[i][j].append([i + 2, j + 2])

                                elif position[i][j] == 11:
                                        iD = i + 1
                                        jD = j + 1
                                        while iD != 8 and jD != 8:
                                                if position[iD][jD] == 0:
                                                        queen.append([iD,jD])

                                                        matrixArea[i][j].append([iD, jD])

                                                elif position[iD][jD] == 2 or position[iD][jD] == 22:
                                                        if iD + 1 < 8 and jD + 1 < 8:
                                                                if position[iD+1][jD+1] == 0:
                                                                        queen_take.append([iD+1,jD+1])

                                                                        matrixArea[i][j].append([iD+1, jD+1])

                                                elif position[iD][jD] == 1 or position[iD][jD] == 11:
                                                        break
                                                iD+=1
                                                jD+=1

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

                                                                        matrixArea[i][j].append([iD-1, jD-1])

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
                                                        if iD +1 < 8 and jD - 1 >= 0:
                                                                if position[iD + 1][jD - 1] == 0:
                                                                        queen_take.append([iD + 1, jD - 1])

                                                                        matrixArea[i][j].append([iD+1, jD-1])

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
                                                if position[i+1][j-1] == 0:
                                                        ##Для кнопки
                                                        actual_moves.append([i+1,j-1])
                                                        # ##Для кнопки
                                                        matrixArea[i][j].append([i+1,j-1])


                                                elif position[i+1][j-1] == 1:
                                                        if i + 2 < 8 and j - 2 >= 0:
                                                                if position[i+2][j-2] == 0:
                                                                        nes_take.append([i + 2, j - 2])
                                                                        taking.append([i+2,j-2])

                                                                        matrixArea[i][j].append([i+2,j-2])

                                        if i + 1 < 8 and j + 1 < 8:
                                                if position[i+1][j+1] == 0:
                                                        actual_moves.append([i+1,j+1])

                                                        matrixArea[i][j].append([i+1,j+1])

                                                elif position[i+1][j+1] == 1:
                                                        if i + 2 < 8 and j + 2 < 8:
                                                                if position[i+2][j+2] == 0:
                                                                        nes_take.append([i+2,j+2])
                                                                        taking.append([i+2,j+2])

                                                                        matrixArea[i][j].append([i+2,j+2])

                                        # Проверка на возможность взятия назад
                                        if i - 1 >= 0 and j - 1 >= 0:
                                                if position[i-1][j-1] == 1 or position[i-1][j-1] == 11:
                                                        if i - 2 >= 0 and j - 2 >= 0:
                                                                if position[i-2][j-2] == 0:
                                                                        taking.append([i-2,j-2])
                                                                        matrixArea[i][j].append([i-2,j-2])

                                        if i - 1 >= 0 and j + 1 < 8:
                                                if position[i-1][j+1] == 1 or position[i-1][j+1] == 11:
                                                        if i - 2 >= 0 and j + 2 < 8:
                                                                if position[i-2][j+2] == 0:
                                                                        taking.append([i-2,j+2])

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



#moves_bot(test_move)

# for i in matrixArea:
#         print(i)

#print(actual_moves)
# print(taking)

# moves_bot(area)
# print(actual_moves)
# print(taking)
# Тесты успешны

# moves_bot(test_queen)
# print(queen)
# print(queen_take)
# Тесты успешны

game_area = [[0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]]

game_area = test_move

# Без обязательного взятия

def move_user(fr, to):
        if abs(fr[0]-to[0]) == 1 and abs(fr[1]-to[1]) == 1:
                iFr = fr[0]
                jFr = fr[1]
                iTo = to[0]
                jTo = to[1]
                game_area[iTo][jTo] = game_area[iFr][jFr]
                game_area[iFr][jFr] = 0

        elif abs(fr[0]-to[0]) == 2 and abs(fr[1]-to[1]) == 2:
                iFr = fr[0]
                jFr = fr[1]
                iTo = to[0]
                jTo = to[1]
                game_area[iTo][jTo] = game_area[iFr][jFr]
                game_area[iFr][jFr] = 0
                game_area[abs((iTo+iFr))//2][abs((jTo+jFr))//2] = 0

        else:
                return False

        return True

# print(move_user([5,0],[3,2]))
# for i in game_area:
#          print(i)


def move_bot(fr, to):
        if abs(fr[0]-to[0]) == 1 and abs(fr[1]-to[1]) == 1:
                iFr = fr[0]
                jFr = fr[1]
                iTo = to[0]
                jTo = to[1]
                game_area[iTo][jTo] = game_area[iFr][jFr]
                game_area[iFr][jFr] = 0


        elif abs(fr[0]-to[0]) == 2 and abs(fr[1]-to[1]) == 2:
                iFr = fr[0]
                jFr = fr[1]
                iTo = to[0]
                jTo = to[1]
                game_area[iTo][jTo] = game_area[iFr][jFr]
                game_area[iFr][jFr] = 0
                game_area[abs((iTo+iFr))//2][abs((jTo+jFr))//2] = 0

        if iTo == 0:
                game_area[iTo][jTo] = 11

        if iTo == 7:
                game_area[iTo][jTo] = 22

        return True

# Без учёта условия обязательного взятия

def bot_level_1(matrixArea):
        forLevel1 = []
        if taking == []:
                for i in range(len(matrixArea)):
                        for j in range(len(matrixArea[i])):
                                if matrixArea[i][j] != []:
                                        forLevel1.append([[i,j],matrixArea[i][j]])

                hod = random.choice(forLevel1)
                fr = hod[0]
                to = random.choice(hod[1])
                move_bot(fr,to)

# bot_level_1(matrixArea)
#
# for i in game_area:
#         print(i)




