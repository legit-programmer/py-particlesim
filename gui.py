import pygame

G2G = 0

# def CheckEvent():


# def ProcessGuiEvent(event:pygame.event.Event)
#     if event.type == pygame.MOUSEBUTTONDOWN:

def Slider(surface:pygame.Surface, label:str, value:float, x:int, y:int)->None:
    global G2G

    BASE_HEIGHT = 25
    BASE_WIDTH = 250

    SLIDER_HEIGHT = 25
    SLIDER_WIDTH = 75

    base = pygame.Rect(x, y, BASE_WIDTH, BASE_HEIGHT)
    pygame.draw.rect(surface, (255, 255, 255), base)

    slider = pygame.Rect(x+250/2 - SLIDER_WIDTH/2, y, SLIDER_WIDTH, SLIDER_HEIGHT)
    pygame.draw.rect(surface, (255, 255, 0), slider)

