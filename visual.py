from global_variables import COORDS
from modules.bot import moves_bot


def checkers_board(canvas):
    canvas.delete("all")
    # ---------------------
    # COLUMN 1
    # ---------------------
    re1_coord = (40, 30, 90, 80)
    COORDS[0][0] = re1_coord
    re1 = canvas.create_rectangle(re1_coord, outline="tomato", fill="tomato", tags="red")
    bl2_coord = (40, 80, 90, 130)
    COORDS[1][0] = bl2_coord
    bl2 = canvas.create_rectangle(bl2_coord, outline="black", fill="black", tags="black")
    re3_coord = (40, 130, 90, 180)
    COORDS[2][0] = re3_coord
    re3 = canvas.create_rectangle(re3_coord, outline="tomato", fill="tomato", tags="red")
    bl4_coord = (40, 180, 90, 230)
    COORDS[3][0] = bl4_coord
    bl4 = canvas.create_rectangle(bl4_coord, outline="black", fill="black", tags="black")
    re5_coord = (40, 230, 90, 280)
    COORDS[4][0] = re5_coord
    re5 = canvas.create_rectangle(re5_coord, outline="tomato", fill="tomato", tags="red")
    bl6_coord = (40, 280, 90, 330)
    COORDS[5][0] = bl6_coord
    bl6 = canvas.create_rectangle(bl6_coord, outline="black", fill="black", tags="black")
    re7_coord = (40, 330, 90, 380)
    COORDS[6][0] = re7_coord
    re7 = canvas.create_rectangle(re7_coord, outline="tomato", fill="tomato", tags="red")
    bl8_coord = (40, 380, 90, 430)
    COORDS[7][0] = bl8_coord
    bl8 = canvas.create_rectangle(bl8_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 2
    # ---------------------
    bl9_coord = (90, 30, 140, 80)
    COORDS[0][1] = bl9_coord
    bl9 = canvas.create_rectangle(bl9_coord, outline="black", fill="black", tags="black")
    re10_coord = (90, 80, 140, 130)
    COORDS[1][1] = re10_coord
    re10 = canvas.create_rectangle(re10_coord, outline="tomato", fill="tomato", tags="red")
    bl11_coord = (90, 130, 140, 180)
    COORDS[2][1] = bl11_coord
    bl11 = canvas.create_rectangle(bl11_coord, outline="black", fill="black", tags="black")
    re12_coord = (90, 180, 140, 230)
    COORDS[3][1] = re12_coord
    re12 = canvas.create_rectangle(re12_coord, outline="tomato", fill="tomato", tags="red")
    bl13_coord = (90, 230, 140, 280)
    COORDS[4][1] = bl13_coord
    bl13 = canvas.create_rectangle(bl13_coord, outline="black", fill="black", tags="black")
    re14_coord = (90, 280, 140, 330)
    COORDS[5][1] = re14_coord
    re14 = canvas.create_rectangle(re14_coord, outline="tomato", fill="tomato", tags="red")
    bl15_coord = (90, 330, 140, 380)
    COORDS[6][1] = bl15_coord
    bl15 = canvas.create_rectangle(bl15_coord, outline="black", fill="black", tags="black")
    re16_coord = (90, 380, 140, 430)
    COORDS[7][1] = re16_coord
    re16 = canvas.create_rectangle(re16_coord, outline="tomato", fill="tomato", tags="red")

    # ---------------------
    # COLUMN 3
    # ---------------------
    re17_coord = (140, 30, 190, 80)
    COORDS[0][2] = re17_coord
    re17 = canvas.create_rectangle(re17_coord, outline="tomato", fill="tomato", tags="red")
    bl18_coord = (140, 80, 190, 130)
    COORDS[1][2] = bl18_coord
    bl18 = canvas.create_rectangle(bl18_coord, outline="black", fill="black", tags="black")
    re19_coord = (140, 130, 190, 180)
    COORDS[2][2] = re19_coord
    re19 = canvas.create_rectangle(re19_coord, outline="tomato", fill="tomato", tags="red")
    bl20_coord = (140, 180, 190, 230)
    COORDS[3][2] = bl20_coord
    bl20 = canvas.create_rectangle(bl20_coord, outline="black", fill="black", tags="black")
    re21_coord = (140, 230, 190, 280)
    COORDS[4][2] = re21_coord
    re21 = canvas.create_rectangle(re21_coord, outline="tomato", fill="tomato", tags="red")
    bl22_coord = (140, 280, 190, 330)
    COORDS[5][2] = bl22_coord
    bl22 = canvas.create_rectangle(bl22_coord, outline="black", fill="black", tags="black")
    re23_coord = (140, 330, 190, 380)
    COORDS[6][2] = re23_coord
    re23 = canvas.create_rectangle(re23_coord, outline="tomato", fill="tomato", tags="red")
    bl24_coord = (140, 380, 190, 430)
    COORDS[7][2] = bl24_coord
    bl24 = canvas.create_rectangle(bl24_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 4
    # ---------------------
    bl25_coord = (190, 30, 240, 80)
    COORDS[0][3] = bl25_coord
    bl25 = canvas.create_rectangle(bl25_coord, outline="black", fill="black", tags="black")
    re26_coord = (190, 80, 240, 130)
    COORDS[1][3] = re26_coord
    re26 = canvas.create_rectangle(re26_coord, outline="tomato", fill="tomato", tags="red")
    bl27_coord = (190, 130, 240, 180)
    COORDS[2][3] = bl27_coord
    bl27 = canvas.create_rectangle(bl27_coord, outline="black", fill="black", tags="black")
    re28_coord = (190, 180, 240, 230)
    COORDS[3][3] = re28_coord
    re28 = canvas.create_rectangle(re28_coord, outline="tomato", fill="tomato", tags="red")
    bl29_coord = (190, 230, 240, 280)
    COORDS[4][3] = bl29_coord
    bl29 = canvas.create_rectangle(bl29_coord, outline="black", fill="black", tags="black")
    re30_coord = (190, 280, 240, 330)
    COORDS[5][3] = re30_coord
    re30 = canvas.create_rectangle(re30_coord, outline="tomato", fill="tomato", tags="red")
    bl31_coord = (190, 330, 240, 380)
    COORDS[6][3] = bl31_coord
    bl31 = canvas.create_rectangle(bl31_coord, outline="black", fill="black", tags="black")
    re32_coord = (190, 380, 240, 430)
    COORDS[7][3] = re32_coord
    re32 = canvas.create_rectangle(re32_coord, outline="tomato", fill="tomato", tags="red")

    # ---------------------
    # COLUMN 5
    # ---------------------
    re33_coord = (240, 30, 290, 80)
    COORDS[0][4] = re33_coord
    re33 = canvas.create_rectangle(re33_coord, outline="tomato", fill="tomato", tags="red")
    bl34_coord = (240, 80, 290, 130)
    COORDS[1][4] = bl34_coord
    bl34 = canvas.create_rectangle(bl34_coord, outline="black", fill="black", tags="black")
    re35_coord = (240, 130, 290, 180)
    COORDS[2][4] = re35_coord
    re35 = canvas.create_rectangle(re35_coord, outline="tomato", fill="tomato", tags="red")
    bl36_coord = (240, 180, 290, 230)
    COORDS[3][4] = bl36_coord
    bl36 = canvas.create_rectangle(bl36_coord, outline="black", fill="black", tags="black")
    re37_coord = (240, 230, 290, 280)
    COORDS[4][4] = re37_coord
    re37 = canvas.create_rectangle(re37_coord, outline="tomato", fill="tomato", tags="red")
    bl38_coord = (240, 280, 290, 330)
    COORDS[5][4] = bl38_coord
    bl38 = canvas.create_rectangle(bl38_coord, outline="black", fill="black", tags="black")
    re39_coord = (240, 330, 290, 380)
    COORDS[6][4] = re39_coord
    re39 = canvas.create_rectangle(re39_coord, outline="tomato", fill="tomato", tags="red")
    bl40_coord = (240, 380, 290, 430)
    COORDS[7][4] = bl40_coord
    bl40 = canvas.create_rectangle(bl40_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 6
    # ---------------------
    bl41_coord = (290, 30, 340, 80)
    COORDS[0][5] = bl41_coord
    bl41 = canvas.create_rectangle(bl41_coord, outline="black", fill="black", tags="black")
    re42_coord = (290, 80, 340, 130)
    COORDS[1][5] = re42_coord
    re42 = canvas.create_rectangle(re42_coord, outline="tomato", fill="tomato", tags="red")
    bl43_coord = (290, 130, 340, 180)
    COORDS[2][5] = bl43_coord
    bl43 = canvas.create_rectangle(bl43_coord, outline="black", fill="black", tags="black")
    re44_coord = (290, 180, 340, 230)
    COORDS[3][5] = re44_coord
    re44 = canvas.create_rectangle(re44_coord, outline="tomato", fill="tomato", tags="red")
    bl45_coord = (290, 230, 340, 280)
    COORDS[4][5] = bl45_coord
    bl45 = canvas.create_rectangle(bl45_coord, outline="black", fill="black", tags="black")
    re46_coord = (290, 280, 340, 330)
    COORDS[5][5] = re46_coord
    re46 = canvas.create_rectangle(re46_coord, outline="tomato", fill="tomato", tags="red")
    bl47_coord = (290, 330, 340, 380)
    COORDS[6][5] = bl47_coord
    bl47 = canvas.create_rectangle(bl47_coord, outline="black", fill="black", tags="black")
    re48_coord = (290, 380, 340, 430)
    COORDS[7][5] = re48_coord
    re48 = canvas.create_rectangle(re48_coord, outline="tomato", fill="tomato", tags="red")
    canvas.pack()

    # ---------------------
    # COLUMN 7
    # ---------------------
    re49_coord = (340, 30, 390, 80)
    COORDS[0][6] = re49_coord
    re49 = canvas.create_rectangle(re49_coord, outline="tomato", fill="tomato", tags="red")
    bl50_coord = (340, 80, 390, 130)
    COORDS[1][6] = bl50_coord
    bl50 = canvas.create_rectangle(bl50_coord, outline="black", fill="black", tags="black")
    re51_coord = (340, 130, 390, 180)
    COORDS[2][6] = re51_coord
    re51 = canvas.create_rectangle(re51_coord, outline="tomato", fill="tomato", tags="red")
    bl52_coord = (340, 180, 390, 230)
    COORDS[3][6] = bl52_coord
    bl52 = canvas.create_rectangle(bl52_coord, outline="black", fill="black", tags="black")
    re53_coord = (340, 230, 390, 280)
    COORDS[4][6] = re53_coord
    re53 = canvas.create_rectangle(re53_coord, outline="tomato", fill="tomato", tags="red")
    bl54_coord = (340, 280, 390, 330)
    COORDS[5][6] = bl54_coord
    bl54 = canvas.create_rectangle(bl54_coord, outline="black", fill="black", tags="black")
    re55_coord = (340, 330, 390, 380)
    COORDS[6][6] = re55_coord
    re55 = canvas.create_rectangle(re55_coord, outline="tomato", fill="tomato", tags="red")
    bl56_coord = (340, 380, 390, 430)
    COORDS[7][6] = bl56_coord
    bl56 = canvas.create_rectangle(bl56_coord, outline="black", fill="black", tags="black")

    # ---------------------
    # COLUMN 8
    # ---------------------
    bl57_coord = (390, 30, 440, 80)
    COORDS[0][7] = bl57_coord
    bl57 = canvas.create_rectangle(bl57_coord, outline="black", fill="black", tags="black")
    re58_coord = (390, 80, 440, 130)
    COORDS[1][7] = re58_coord
    re58 = canvas.create_rectangle(re58_coord, outline="tomato", fill="tomato", tags="red")
    bl59_coord = (390, 130, 440, 180)
    COORDS[2][7] = bl59_coord
    bl59 = canvas.create_rectangle(bl59_coord, outline="black", fill="black", tags="black")
    re60_coord = (390, 180, 440, 230)
    COORDS[3][7] = re60_coord
    re60 = canvas.create_rectangle(re60_coord, outline="tomato", fill="tomato", tags="red")
    bl61_coord = (390, 230, 440, 280)
    COORDS[4][7] = bl61_coord
    bl61 = canvas.create_rectangle(bl61_coord, outline="black", fill="black", tags="black")
    re62_coord = (390, 280, 440, 330)
    COORDS[5][7] = re62_coord
    re62 = canvas.create_rectangle(re62_coord, outline="tomato", fill="tomato", tags="red")
    bl63_coord = (390, 330, 440, 380)
    COORDS[6][7] = bl63_coord
    bl63 = canvas.create_rectangle(bl63_coord, outline="black", fill="black", tags="black")
    re64_coord = (390, 380, 440, 430)
    COORDS[7][7] = re64_coord
    re64 = canvas.create_rectangle(re64_coord, outline="tomato", fill="tomato", tags="red")


def draw(lst, CANVAS):
    CANVAS.update()
    w_c = []
    b_c = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 2:
                b_c.append(CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5, COORDS[i][j][3] - 5, outline="yellow", fill="yellow", tags="yellow"))
            elif lst[i][j] == 1:
                ci = CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5, COORDS[i][j][3] - 5, outline="white", fill="white", tags="white")
                w_c.append(ci)
            elif lst[i][j] == 22:
                b_c.append(CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5, COORDS[i][j][3] - 5, outline="red", fill="yellow", tags="yellow"))
            elif lst[i][j] == 11:
                ci = CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5,
                                        COORDS[i][j][3] - 5, outline="red", fill="white", tags="white")
                w_c.append(ci)
    CANVAS.update()

def draw_reversed(lst, CANVAS):
    w_c = []
    b_c = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 2:
                b_c.append(CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5, COORDS[i][j][3] - 5, outline="white", fill="white", tags="white"))
            elif lst[i][j] == 1:
                ci = CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5, COORDS[i][j][3] - 5, outline="yellow", fill="yellow", tags="yellow")
                w_c.append(ci)
            elif lst[i][j] == 22:
                b_c.append(CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5, COORDS[i][j][3] - 5, outline="red", fill="white", tags="white"))
            elif lst[i][j] == 11:
                ci = CANVAS.create_oval(COORDS[i][j][0] + 5, COORDS[i][j][1] + 5, COORDS[i][j][2] - 5,
                                        COORDS[i][j][3] - 5, outline="red", fill="yellow", tags="yellow")
                w_c.append(ci)
    CANVAS.update()
    
