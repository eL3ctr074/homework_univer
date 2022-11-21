import pygame as pg
import colors as c
import random as rd
import math as m

pg.init()
clock = pg.time.Clock()
FPS = 30

HEIGHT = 600
WIDTH = 800

APPLE_RADIUS = 15
SNAKE_RADIUS = 15
SPEED = 10



class Circle:
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        
    def is_collide(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 < (self.radius + other.radius)
    
    def draw(self):
        pg.draw.circle(self.screen, c.GREEN, (self.x, self.y), self.radius, 0)
    

class Apple:
    def __init__(self, x, y, screen):
        self.circle = Circle(x, y, APPLE_RADIUS, screen)
    
    def create_new(self, snake):
        while True:
            self.x, self.y = rd.randint(0, WIDTH), rd.randint(0, HEIGHT)
            
            if not snake.collide(self):
                break
    
    def draw(self):
        self.circle.draw()
        
            
class Snake:
    def __init__(self, x, y, screen):
        self.circle = Circle(x, y, SNAKE_RADIUS, screen)
        self.direction = pg.K_RIGHT
        
    def collide(self, apple):
        return self.circle.is_collide(apple.cirle) 
    
    def go(self):
        speed = SPEED
        if key == pg.K_RIGHT:
            self.circle.x += speed
        elif key == pg.K_LEFT:
            self.circle.x -= speed
        elif key == pg.K_UP:
            self.circle.y -= speed
        elif key == pg.K_DOWN:
            self.circle.y += speed
            
        if self.circle.x > WIDTH:
            self.circle.x -= WIDTH
        if self.circle.x < 0:
            self.circle.x = WIDTH

        if self.circle.y > HEIGHT:
            self.circle.y -= HEIGHT
        if self.circle.y < 0:
            self.circle.y = HEIGHT


            
        
        
            
    def draw(self):
        self.circle.draw()
        
        
                


def GameOverStatus():
    pass



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
    screen = pg.display.set_mode([WIDTH, HEIGHT])
    pg.display.set_caption('змейка')
    x = 60
    y = 160
    running = True

    apX = rd.randint(0, 800)
    apY = rd.randint(0, 500)


    snake = Snake(x, y, screen)
    apple = Apple(apX, apY, screen)
    apple.create_new(snake)
    


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                snake.direction = event.key

        screen.fill(c.WHITE)


        snake.go()
        
        if snake.collide(apple):
            apple.create_new(snake)
        
        snake.draw()
        apple.draw()
        

        
        clock.tick(FPS)
        pg.display.flip()

    pg.quit()
