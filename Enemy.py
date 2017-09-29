import pygame
from pygame.sprite import Sprite
import random

class Enemy(Sprite):
	def __init__(self, screen, cols, rows, x):
		super(Enemy, self).__init__()
		self.screen = screen
		self.x = x
		self.y = random.randint(100,300)
		self.speed = 5
		self.sheet_orginal=pygame.image.load("./images/bird.png")
		self.sheet = pygame.transform.scale(self.sheet_orginal, [200,200])
		self.cols= cols
		self.rows = rows
		self.rect = self.sheet.get_rect()
		w = self.cellWidth = self.rect.width  / cols
		h = self.cellHeight = (self.rect.height - 3)  / rows
		hw, hh = self.cellCenter = (w/2, h/2)
		self.totalCellCount = rows * cols
		self.cells = list([(index % cols * w, index / cols * h,w,h) for index in range(self.totalCellCount)])
		self.handle = list([
			(0,0),(-hw, 0),(-w, -hh),
			(0, -hh),(-hw,-hh),(-w, -hh),
			(0, -h), (-hw, -h), (-w, -h)
		])
		self.rect = pygame.Rect(self.x, self.y, 50, 50)
	def fly_right(self, surface, cellIndex, handle=0):
		self.x += self.speed
		surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])
		self.rect = pygame.Rect(self.x, self.y, 50, 50)
		if self.x > 800:
			self.x =0
	def fly_left(self, surface, cellIndex, handle =0):
		self.x -= self.speed
		surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])
		self.rect = pygame.Rect(self.x, self.y, 50, 50)
		if self.x < 0 :
			self.x = 750

	def draw(self, surface, cellIndex, handle=0):
		surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])
		self.rect = pygame.Rect(self.x, self.y, 50, 50)