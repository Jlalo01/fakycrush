import pygame as P



def zero(wn, x, y, w, h, color):
    #P.draw.polygon(wn, color, [[x + (w*0.1), y], [x + (w*0.9), y], [x + w, y + (h*0.1)], [x + w, y + (h*0.9)], [x + (w*0.9), y + h], [x + (w*0.1), y + h], [x, y + (h*0.9)], [x, y + (h*0.1)]], 15)
    #P.draw.rect(wn, color, [x, y+5, w-10, h-10], 10)
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    P.draw.rect(wn, color, [x, y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True

def one(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    return True

def two(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h*0.5])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    P.draw.rect(wn, color, [x, y+(h*0.5), h*0.15, h*0.5])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True

def three(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True

def four(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, h*0.15, h*0.5])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    return True

def five(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x, y, h*0.15, h*0.5])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y+(h*0.5), h*0.15, h*0.5])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True

def six(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x, y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y+(h*0.5), h*0.15, h*0.5])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True

def seven(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    return True

def eight(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x, y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True

def nine(wn, x, y, w, h, color):
    P.draw.rect(wn, color, [x, y, w, h*0.15])
    P.draw.rect(wn, color, [x, y, h*0.15, h*0.5])
    P.draw.rect(wn, color, [x, y+(h*0.45), w, h*0.15])
    P.draw.rect(wn, color, [x+w-(h*0.15), y, h*0.15, h])
    P.draw.rect(wn, color, [x, y+(h*0.85), w, h*0.15])
    return True



def show(wn, x, y, w, h, color, s):
    if s//100 == 0:
        zero(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 1:
        one(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 2:
        two(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 3:
        three(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 4:
        four(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 5:
        five(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 6:
        six(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 7:
        seven(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 8:
        eight(wn, x-(w*1.1), y, w, h, (0,0,0))
    elif s//100 == 9:
        nine(wn, x-(w*1.1), y, w, h, (0,0,0))

    if s%100//10 == 0:
        zero(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 1:
        one(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 2:
        two(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 3:
        three(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 4:
        four(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 5:
        five(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 6:
        six(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 7:
        seven(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 8:
        eight(wn, x, y, w, h, (0,0,0))
    elif s%100//10 == 9:
        nine(wn, x, y, w, h, (0,0,0))

    if s%10 == 0:
        zero(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 1:
        one(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 2:
        two(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 3:
        three(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 4:
        four(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 5:
        five(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 6:
        six(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 7:
        seven(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 8:
        eight(wn, x+w+(w*0.1), y, w, h, (0,0,0))
    elif s%10 == 9:
        nine(wn, x+w+(w*0.1), y, w, h, (0,0,0))

    return True