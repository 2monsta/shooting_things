import pygame

class SpriteSheet():
	def __init__(self, filename, cols, rows, screen):
		self.sheet = filename
		self.cols = cols #64px
		self.rows = rows #64px
		self.totalCellCount = cols * rows
		self.x = 600
		self.y = 350
		self.speed = 10;
		self.rect = self.sheet.get_rect();
		w = self.cellWidth = self.rect.width / cols
		h = self.cellHeight = self.rect.height / rows
		hw, hh = self.cellCenter = (w/2, h/2)
		self.should_move_up = False;
		self.should_move_down = False;
		self.should_move_left = False;
		self.should_move_right = False;
		self.screen = screen

		self.cells = list([(index % cols * w, index / cols * h,w,h) for index in range(self.totalCellCount)])
		self.handle = list([
			(0,0),(-hw, 0),(-w, -hh),
			(0, -hh),(-hw,-hh),(-w, -hh),
			(0, -h), (-hw, -h), (-w, -h)
		])
	def draw(self, surface, cellIndex, x ,y, handle=0):
		surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])

	def draw_me(self, surface, cellIndex, x ,y, handle=0):
		if(self.should_move_up):
			self.y -= self.speed;
		elif(self.should_move_down):
			self.y += self.speed;
		if(self.should_move_left):
			self.x -= self.speed;
		elif(self.should_move_right):
			self.x += self.speed;
		surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])

	def should_move(self, direction, yes_or_no):
		if(direction =="up"):
			self.should_move_up = yes_or_no; #the key is down, update itself;
		if(direction =="down"):
			self.should_move_down = yes_or_no;
		if(direction =="left"):
			self.should_move_left = yes_or_no;
		if(direction =="right"):
			self.should_move_right = yes_or_no;

	def jump(self, true_or_false, surface, cellIndex, x ,y, handle=0):
		if(true_or_false == True):
			self.y -=70
			surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])
		else:
			self.y +=70;
			surface.blit(self.sheet,(self.x+self.handle[handle][0], self.y + self.handle[handle][1]), self.cells[cellIndex])