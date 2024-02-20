import random
import pygame as P
import time
import gen_num as num

BG = (135, 206, 250)
RED = (200, 0, 0)
L_RED = (250, 50, 50)
D_RED = (100, 0, 0)
M_RED = (150, 0, 0)
BLUE = (0, 0, 200)
L_BLUE = (50, 50, 250)
D_BLUE = (0, 0, 100)
M_BLUE = (0, 0, 150)
ORANGE = (255, 165, 0)
L_ORANGE = (255, 215, 50)
D_ORANGE = (155, 65, 0)
M_ORANGE = (205, 115, 0)
GREEN = (0, 200, 0)
L_GREEN = (50, 250, 50)
D_GREEN = (0, 100, 0)
M_GREEN = (0, 150, 0)
PURPLE = (106, 13, 173)
L_PURPLE = (156, 63, 223)
D_PURPLE = (6, 0, 73)
M_PURPLE = (56, 0, 123)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class candy:
    def __init__(self, v):
        self.value = v
        self.selected = False


class board:
    def __init__(self, a, b):
        self.area = a * b
        self.width = a
        self.height = b
        self.selected = [-1, -1]
        self.viz = []
        for i in range(b):
            row = []
            for j in range(a):
                row.append(-1)
            self.viz.append(row)

    
    def fill(self):
        for i in range(self.height):
            for j in range(self.width):
                self.viz[i][j] = candy(random.randint(0, 4))

    def displayB(self):
        for i in range(self.height):
            print(self.viz[i])
    
    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.viz[i][j].value, end=" ")
            print()

    def at(self, x, y):
        try:
            return self.viz[y][x]
        except:
            return -2
    
    
    def valAt(self, x, y):
        try:
            return self.at(x, y).value
        except:
            return -2
    
    def change(self, x, y, val):
        self.viz[y][x].value = val
        return True
    
    def reduce(self):
        changed = False
        for i in range(self.height):
            for j in range(self.width):
                on = self.valAt(j ,i)
                if on == -1:
                    continue
                if on == self.valAt(j + 1, i) and on == self.valAt(j - 1, i) and j - 1 >= 0 and j + 1 < self.height:
                    self.change(j, i, -1)
                    self.change(j + 1, i, -1)
                    self.change(j - 1, i, -1)
                    changed = True
                elif on == self.valAt(j + 1, i) and on == self.valAt(j + 2, i) and j + 2 < self.height:
                    self.change(j, i, -1)
                    self.change(j + 1, i, -1)
                    self.change(j + 2, i, -1)
                    changed = True
                elif on == self.valAt(j - 1, i) and on == self.valAt(j - 2, i) and j - 2 >= 0:
                    self.change(j, i, -1)
                    self.change(j - 1, i, -1)
                    self.change(j - 2, i, -1)
                    changed = True
                elif on == self.valAt(j, i + 1) and on == self.valAt(j, i - 1) and i - 1 >= 0 and i + 1 < self.width:
                    self.change(j, i, -1)
                    self.change(j, i + 1, -1)
                    self.change(j, i - 1, -1)
                    changed = True
                elif on == self.valAt(j, i + 1) and on == self.valAt(j, i + 2) and i + 2 < self.width:
                    self.change(j, i, -1)
                    self.change(j, i + 1, -1)
                    self.change(j, i + 2, -1)
                    changed = True
                elif on == self.valAt(j, i - 1) and on == self.valAt(j, i - 2) and i - 2 >= 0:
                    self.change(j, i, -1)
                    self.change(j, i - 1, -1)
                    self.change(j, i - 2, -1)
                    changed = True
        return changed

    def shift(self):
        for times in range(self.height):
            for i in range(self.height):
                for j in range(self.width):
                    if self.valAt(j, i + 1) == -1:
                        self.change(j, i + 1, self.valAt(j, i))
                        self.change(j, i, -1)
    
    def drawSquare(self, c, l, d, m, x, y):
        px = x*100
        py = y*100
        P.draw.rect(win, m, [px + 10, py + 10, 80, 80])
        P.draw.rect(win, c, [px + 20, py + 20, 60, 60])
        P.draw.polygon(win, l, [[px + 10, py + 10], [px + 89, py + 10], [px + 80, py + 20], [px + 20, py + 20]], 0)
        P.draw.polygon(win, d, [[px + 20, py + 80], [px + 80, py + 80], [px + 89, py + 90], [px + 10, py + 90]], 0)
    
    def drawCircle(self, c, l, d, m, x, y):
        px = x * 100
        py = y * 100
        P.draw.polygon(win, m, [[px+50, py+10], [px+90, py+50], [px+50, py+90], [px+10, py+50]], 0)
        P.draw.polygon(win, c, [[px+50, py+20], [px+80, py+50], [px+50, py+80], [px+20, py+50]], 0)
        P.draw.polygon(win, l, [[px+50, py+10], [px+50, py+20], [px+20, py+50], [px+10, py+50]], 0)
        P.draw.polygon(win, d, [[px+80, py+50], [px+90, py+50], [px+50, py+90], [px+50, py+80]], 0)
        #P.draw.circle(win, m, [px + 50, py + 50], 40, 0)
        #P.draw.circle(win, c, [px + 50, py + 50], 33, 0)

    def drawTriangle(self, c, l, d, m, x, y):
        px = x * 100
        py = y * 100
        P.draw.polygon(win, m, [[px + 50, py + 15], [px + 90, py + 85], [px + 10, py + 85]], 0)
        P.draw.polygon(win, c, [[px + 50, py + 25], [px + 80, py + 80], [px + 20, py + 80]], 0)
        P.draw.polygon(win, l, [[px + 50, py + 15], [px + 50, py + 25], [px + 20, py + 80], [px + 10, py + 85]], 0)
        P.draw.polygon(win, d, [[px + 20, py + 80], [px + 80, py + 80], [px + 89, py + 85], [px + 10, py + 85]], 0)
        
    def drawRect(self, c, l, d, m, x, y):
        px = x * 100
        py = y * 100
        P.draw.rect(win, m, [px + 20, py + 10, 60, 80])
        P.draw.rect(win, c, [px + 30, py + 20, 40, 60])
        P.draw.polygon(win, l, [[px + 20, py + 10], [px + 79, py + 10], [px + 70, py + 20], [px + 30, py + 20]], 0)
        P.draw.polygon(win, d, [[px + 30, py + 80], [px + 70, py + 80], [px + 79, py + 90], [px + 20, py + 90]], 0)

    def drawRect2(self, c, l, d, m, x ,y):
        px = x * 100
        py = y * 100
        P.draw.rect(win, m, [px + 10, py + 20, 80, 60])
        P.draw.rect(win, c, [px + 20, py + 30, 60, 40])
        P.draw.polygon(win, l, [[px + 10, py + 20], [px + 90, py + 20], [px + 80, py + 30], [px + 20, py + 30]], 0)
        P.draw.polygon(win, d, [[px + 20, py + 70], [px + 80, py + 70], [px + 89, py + 80], [px + 10, py + 80]], 0)

    def paint(self):
        for i in range(self.height):
            for j in range(self.width):
                P.draw.rect(win, BG, [j * 100, i * 100, 100, 100])
                if self.at(j, i).value == 0:
                    self.drawSquare(RED, L_RED, D_RED, M_RED, j, i)
                elif self.at(j, i).value == 1:
                    self.drawCircle(BLUE, L_BLUE, D_BLUE, M_BLUE, j, i)
                elif self.at(j, i).value == 2:
                    self.drawTriangle(GREEN, L_GREEN, D_GREEN, M_GREEN, j, i)
                elif self.at(j, i).value == 3:
                    self.drawRect(ORANGE, L_ORANGE, D_ORANGE, M_ORANGE, j, i)
                elif self.at(j, i).value == 4:
                    self.drawRect2(PURPLE, L_PURPLE, D_PURPLE, M_PURPLE, j, i)
                elif self.at(j, i).value == -1:
                    P.draw.rect(win, BG, [j*100, i*100, 100, 100])
                P.draw.rect(win, BLACK, [j*100, i*100, 100, 100], 2)

    def refill(self):
        changed = False
        for i in range(self.height):
            for j in range(self.width):
                if self.valAt(j, i) == -1:
                    self.change(j, i, random.randint(0, 4))
                    changed = True
        return changed

    def canReduce(self):
        for i in range(self.height):
            for j in range(self.width):
                cur = self.valAt(j, i)
                if cur == self.valAt(j + 1, i + 1) and cur == self.valAt(j - 1, i + 1) and j + 1 < self.width and j - 1 >= 0 and i + 1 < self.height:
                    return True
                elif cur == self.valAt(j + 1, i - 1) and cur == self.valAt(j - 1, i - 1) and j + 1 < self.width and j - 1 >= 0 and i - 1 >= 0:
                    return True
                elif cur == self.valAt(j + 1, i + 1) and cur == self.valAt(j + 2, i + 1) and j + 2 < self.width and i + 1 < self.height:
                    return True
                elif cur == self.valAt(j + 1, i - 1) and cur == self.valAt(j + 2, i - 1) and j + 2 < self.width and i - 1 >= 0:
                    return True
                elif cur == self.valAt(j - 1, i + 1) and cur == self.valAt(j - 2, i + 1) and j - 2 >= 0 and i + 1 < self.height:
                    return True
                elif cur == self.valAt(j - 1, i - 1) and cur == self.valAt(j - 2, i - 1) and j - 2 >= 0 and i - 1 >= 0:
                    return True
                elif cur == self.valAt(j - 1, i - 1) and cur == self.valAt(j - 1, i + 1) and j - 1 >= 0 and i + 1 < self.height and i - 1 >= 0:
                    return True
                elif cur == self.valAt(j + 1, i - 1) and cur == self.valAt(j + 1, i + 1) and j + 1 < self.width and i + 1 < self.height and i - 1 >= 0:
                    return True
                elif cur == self.valAt(j - 1, i - 2) and cur == self.valAt(j - 1, i - 1) and j - 1 >= 0 and i - 2 >= 0:
                    return True
                elif cur == self.valAt(j - 1, i + 1) and cur == self.valAt(j - 1, i + 2) and j - 1 >= 0 and i + 2 < self.height:
                    return True
                elif cur == self.valAt(j + 1, i - 2) and cur == self.valAt(j + 1, i - 1) and j + 1 < self.width and i - 2 >= 0:
                    return True
                elif cur == self.valAt(j + 1, i + 1) and cur == self.valAt(j + 1, i + 2) and j + 1 < self.width and i + 2 < self.height:
                    return True
                elif cur == self.valAt(j - 3, i) and cur == self.valAt(j - 2, i) and j - 3 >= 0:
                    return True
                elif cur == self.valAt(j + 2, i) and cur == self.valAt(j + 3, i) and j + 3 < self.width:
                    return True
                elif cur == self.valAt(j, i - 3) and cur == self.valAt(j, i - 2) and i - 3 >= 0:
                    return True
                elif cur == self.valAt(j, i + 2) and cur == self.valAt(j, i + 3) and i + 3 < self.height:
                    return True

        return False

    def reduces(self, j, i, px, py):
        on = self.valAt(px, py)
        if on == self.valAt(j + 1, i) and on == self.valAt(j - 1, i) and j - 1 >= 0 and j + 1 < self.width and not(px == j + 1 or px == j - 1):
            print("1")
            return True
        elif on == self.valAt(j + 1, i) and on == self.valAt(j + 2, i) and j + 2 < self.width and not(px == j + 1 or px == j + 2):
            print("2")
            return True
        elif on == self.valAt(j - 1, i) and on == self.valAt(j - 2, i) and j - 2 >= 0 and not(px == j - 1 or px == j - 2):
            print("3")
            return True
        elif on == self.valAt(j, i + 1) and on == self.valAt(j, i - 1) and i - 1 >= 0 and i + 1 < self.height and not(py == i + 1 or py == i - 1):
            print("4")
            return True
        elif on == self.valAt(j, i + 1) and on == self.valAt(j, i + 2) and i + 1 < self.height and not(py == i + 1 or py == i + 2):
            print("5")
            return True
        elif on == self.valAt(j, i - 1) and on == self.valAt(j, i - 2) and i - 2 >= 0 and not(py == i - 1 or py == i - 2):
            print("6")
            return True
        return False



                


t = candy(random.randint(0,4))
x = board(5, 4)
x.fill()
score = 000

P.init()
win = P.display.set_mode((1200, 900))
P.display.set_caption("Game")
win.fill(BG)
exit = False
x.paint()

while not exit:
    if x.reduce():
        score += 1
        x.shift()
        x.paint()
        P.display.update()
        time.sleep(1/2)
    elif x.refill():
        x.paint()
        P.display.update()
        time.sleep(1/2)
    else:
        if not x.canReduce():
            P.draw.rect(win, RED, [800, 800, 100, 100])
            #break
    
    for event in P.event.get():
        if event.type == P.QUIT:
            exit = True
        if event.type == P.MOUSEBUTTONDOWN:
            pos = P.mouse.get_pos()
            px = pos[0] // 100
            py = pos[1] // 100
            if px >= x.width or py >= x.height:
                continue
            P.draw.rect(win, WHITE, [px * 100, py * 100, 100, 100], 2)
            if x.selected[0] != -1:
                if not x.reduces(px, py, x.selected[0], x.selected[1]):
                    x.paint()
                    x.selected = [-1, -1]
                    break
                elif px > x.selected[0] + 1 or px < x.selected[0] - 1 or py > x.selected[1] + 1 or py < x.selected[1] - 1 or (px != x.selected[0] and py != x.selected[1]):
                    x.paint()
                    x.selected = [-1, -1]
                    break
                
                one = x.valAt(px, py)
                two = x.valAt(x.selected[0], x.selected[1])
                x.change(px, py, two)
                x.change(x.selected[0], x.selected[1], one)
                #P.draw.rect(win, BLACK, P.Rect(x.selected[0] * 100, x.selected[1] * 100, 100, 100), 2)
                x.paint()
                P.display.update()
                time.sleep(1/4)
                x.selected = [-1, -1]
            else:
                x.selected = [px, py]
        if event.type == P.KEYDOWN:
            if event.key == P.K_q:
                exit = True

    P.draw.rect(win, BG, [840, 100, 150, 80])
    num.show(win, 900, 100, 40, 80, BLACK, score)
    P.display.update()


        

    

