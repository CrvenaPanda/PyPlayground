# Problem: Find PI with uniform random
# python ver. 3.7.7

import pygame
from pygame.locals import *
import pygame.freetype
import random
import math

_pointsCount = 10000
_radius = 1.0

_windowWidth = 1200
_windowHeight = 800

_lineWidth = 4
_shapeLineWidth = 2
_pointRadius = 2

def WaitForInput():
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            return
        if event.type == KEYDOWN and event.key == K_RETURN:
            return

def Percent(size, value):
    return value / size

def PointToWindowPoint(point):
    percentX = (point[0] + 1.0) / 2.0
    percentY = (point[1] + 1.0) / 2.0

    return ((int)(800 * percentX), (int)(_windowHeight * percentY))

def DrawPoints(points, pi):
    pygame.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    window = pygame.display.set_mode((_windowWidth, _windowHeight))
    window.fill(pygame.Color("white"))
    
    # points
    for point in points:
        pygame.draw.circle(window, (35,55,255), PointToWindowPoint(point), _pointRadius)

    # x and y lines
    pygame.draw.line(window, (0, 0, 0), (400, 800), (400, 0), _lineWidth)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (800, 400), _lineWidth)

    # box and circle
    pygame.draw.rect(window, (144, 144, 89), Rect(0,0,800,800), _shapeLineWidth)
    pygame.draw.circle(window, (255,55,45), (400, 400), 400, _shapeLineWidth)

    # text
    text = font.render("PI = %.5f" % pi, False, (0, 0, 0))
    window.blit(text, (900, 400))

    pygame.display.update()
    WaitForInput()
    pygame.quit()

def GenerateRandomPoints(count):
    points = []
    for i in range(count):
        points.append((random.uniform(-1, 1), random.uniform(-1, 1)))

    return points

def PointsInCircle(points):
    count = 0
    for point in points:
        dstFromCenter = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
        if dstFromCenter < _radius:
            count += 1

    return count

def EstimatePi(points):
    return 4.0 * (PointsInCircle(points) / _pointsCount)

if __name__ == "__main__":
    points = GenerateRandomPoints(_pointsCount)
    pi = EstimatePi(points)
    DrawPoints(points, pi)