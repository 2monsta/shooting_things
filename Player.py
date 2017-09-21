import pygame
from pygame.sprite import Sprite

class Player(sprite):
	def __init__(self, start_x, start_y, screen):
		super(Player, self).__init();
		self.x = start_x
		self.y = start_y
		self.screen = screen
		self.speed = 10