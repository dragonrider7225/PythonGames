from pygame.constants import *
import pygame as pyg

def draw_card_base(surf, rect):

    """draw_card_base(surf, rect) -> pygame.Rect

Draw a blank card in the given Rect and blit it to the given surface.

Written by josmiley and obtained from http://www.pygame.org/project-AAfilledRoundedRect-2349-.html
Modified by Kevin Moonen
"""
    radius = 0.15
    rect = pyg.Rect(rect)
    color = pyg.Color("white")
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pyg.Surface(rect.size, SRCALPHA)

    circle = pyg.Surface([min(rect.size) * 3] * 2, SRCALPHA)
    pyg.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = pyg.transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

    return surf.blit(rectangle, pos)
