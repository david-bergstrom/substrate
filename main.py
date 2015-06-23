# Lagg till djup i slutet

import pygame
from random import random, randrange, choice
import math

w = 640
h = 480
surface = pygame.display.set_mode((w, h))

background = pygame.Color('black')
white = pygame.Color('white')

def within_screen((x, y)):
    return 0 <= x and x < w and  0 <= y and y < h

def empty_pixel(p):
    return surface.get_at(p) == background

def hard_rime():
    x = randrange(w)
    y = randrange(h)
    radius = randrange(1, min(w, h))

    dx, dy = choice([(1, -1), (1, 1), (-1, 1), (-1, -1)])

    def f(t):
        return (x + dx + int(20 * math.cos(t / 10)),
                y + dy * t)

    return f

def random_point():
    return choice([squares, lines])()

def lines():
    x = randrange(w)
    y = randrange(h)

    dx, dy = choice([(1, -1), (1, 1), (-1, 1), (-1, -1)])

    def f(t):
        return (x + dx * t,
                y + dy * t)
    
    return f

def squares():
    x = randrange(w)
    y = randrange(h)

    width = randrange(1, 400)
    height = randrange(1, 400)

    radius = (width + height) * 2


    def f(t):
        t %= radius
        if (t < width): # Draw -
            return (x + t, y)
        elif (t < width + height): # Draw -|
            return (x + width, y + t - width)
        elif (t < width + height + width): # Draw =|
            return (x + width - t + width + height, y + height)
        else: # Draw |=|
            return (x, y + height - t + width + height + width)

    return f

def main():
    pygame.init()

    pygame.display.set_caption("Substrate")
    clock = pygame.time.Clock()
    
    # p = (t, \t -> (x, y))
    points = [(0, random_point(), [])]

    surface.fill(background)

    running = True
    
    while True:
        clock.tick(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    running != running

        if running:
            new_points = []
            for time, f, history in points:
                new_point = f(time + 1)
                if new_point in history:
                    new_points.append((time + 1, f, history))
                elif within_screen(new_point) and empty_pixel(new_point):
                    surface.set_at(new_point, white)
                    new_points.append((time + 1, f, history))
                else:
                    #print(new_point, 'was not accepted, within_screen:',
                    #      within_screen(new_point), 'empty_pixel:',
                    #      within_screen(new_point) and empty_pixel(new_point))
                    new_points.append((0, random_point(), []))
                points = new_points

                pygame.display.update()

def etch_a_sketch():
    x = randrange(w)
    y = randrange(h)

    width = randrange(1, 100)
    height = randrange(1, 100)

    radius = (width + height) * 2

    dx, dy = choice([(1, -1), (1, 1), (-1, 1), (-1, -1)])

    def f(t):
        t %= radius
        if (t < radius // 4):
            return (x + t, y) 
        elif (t < radius // 2):
            return (x + width, y + t)
        elif (t < 3 * radius // 4):
            return (x + t, y + height)
        else: 
            return (x, y + t)

    return f


if __name__ == '__main__':
    main()
