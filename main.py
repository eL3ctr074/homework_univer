import pygame as pg
import colors as c
import random as rd
import math as m

pg.init()
clock = pg.time.Clock()
FPS = 30
speed = 10

def GameOverStatus():
    pass

def PosOverField_onX(posX):
    if posX > 800:
        posX -= 800
    if posX < 0:
        posX = 800
    return posX

def PosOverField_onY(posY):
    if posY > 500:
        posY -= 500
    if posY < 0:
        posY = 500
    return posY

def CollideAppleX(xp, yp, ax, ay):
    catX = abs(xp-ax)
    catY = abs(yp-ay)

    hyp = m.sqrt(catX**2 + catY**2)

    if hyp == 30:
        ax = rd.randint(0, 800)
        ay = rd.randint(0, 500)

    return ax, ay


if __name__ == "__main__":
    key = None
    screen = pg.display.set_mode([800, 500])
    pg.display.set_caption('змейка')
    x = 60
    y = 160
    running = True

    apX = rd.randint(0, 800)
    apY = rd.randint(0, 500)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                key = event.key

        screen.fill(c.WHITE)

        if key == pg.K_RIGHT:
            x += speed
        elif key == pg.K_LEFT:
            x -= speed
        elif key == pg.K_UP:
            y -= speed
        elif key == pg.K_DOWN:
            y += speed

        pg.draw.circle(screen, c.GREEN, (x, y), 15, 0)
        pg.draw.circle(screen, c.RED, (apX, apY), 15, 0)

        x = PosOverField_onX(x)
        y = PosOverField_onY(y)

        apX, apY = CollideAppleX(x, y, apX, apY)

        clock.tick(FPS)
        pg.display.flip()

    pg.quit()
