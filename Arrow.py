import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
	def __init__(self, screen, spritesheet):
		super(Arrow, self).__init__();
		self.screen = screen
		