import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
	def __init__(self, screen, spritesheet):
		super(Arrow, self).__init__();
		self.image_original = pygame.image.load("./images/arrow1b.png")
		self.image = pygame.transform.scale(self.image_original, [70,70])
		self.screen = screen
		self.rect = pygame.Rect(0,0,10,10)
		self.rect.centerx = spritesheet.x
		self.rect.top = spritesheet.y
		self.x = self.rect.x
		self.y = self.rect.y
		self.direction = 1
		self.speed = 15
		self.color= (0,0,0)
	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
		elif self.direction == 3: #down
			self.y += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		else: #left
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
	def draw_bullet(self):
		# pygame.draw.rect(self.screen, self.color, self.rect)
		self.rect = pygame.Rect(self.x, self.y,10,10)
		self.screen.blit(self.image, [self.x -15, self.y - 15])