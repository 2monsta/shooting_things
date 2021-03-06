import pygame
from SpriteSheet import SpriteSheet
from pygame.sprite import Group, groupcollide
from Arrow import Arrow
from Enemy import Enemy
import random


#TODO: render a play page and then add scores on top
#TODO: add new enemy when it hits at random locations
#TODO: add power ups after hitting power ups, speed goes up by 5

pygame.init()

W,H = 800, 500
HW, HH, = W/2, H/2
Area = W * H

screen = pygame.display.set_mode((W,H))
background_image_original = pygame.image.load("./images/background3.png")
background_image = pygame.transform.scale(background_image_original, [800, 500])
s_original = pygame.image.load("./images/archer.png")
s = SpriteSheet(s_original, 13, 1, screen)
arrows = Group()
bird = Enemy(screen, 5, 4, 10)
bird_two = Enemy(screen, 5, 4, 650)
enemy_group_left = Group()
enemy_group_right = Group()
enemy_group_left.add(bird)
enemy_group_right.add(bird_two)

def check_collision():
	pygame.sprite.groupcollide(arrows, enemy_group_left, False, True)
	pygame.sprite.groupcollide(arrows, enemy_group_right, False, True)

def message_players_name(text, name):
	largeText = pygame.font.Font(None ,30)
	story = largeText.render(text, True, (0, 0, 0));
	start_text = largeText.render(name, True, (0, 0, 0));
	screen.blit(start_text, [300, 300]);
	screen.blit(story, [300, 200]);
	pygame.display.update()
def message_display(text): 
	largeText = pygame.font.Font(None ,30)
	start_text = largeText.render(text, True, (0, 0, 0));
	screen.blit(start_text, [300, 100]);
	pygame.display.update()

def health():
	text = pygame.font.Font(None, 20);
	monster_killed = text.render("Monster Killed: %d" %s.count, True, (0, 0, 0));
	screen.blit(monster_killed, [100, 70])
def double_enemy():
	x = random.randint(100,500)
	y = random.randint(350, 450)
	new_bird_two = Enemy(screen, 5, 4, x, y)
	enemy_group_left.add(new_bird_two);

game_on = True
index = 0;
index_bird = 0
tick = 0
swinging = False;
starting_text = True;
while game_on:
	tick +=1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				s.should_move("left", True)
			elif event.key == pygame.K_d:
				s.should_move("right", True)
			if event.key == pygame.K_s:
				s.should_move("down", True)
			elif event.key == pygame.K_w:
				s.should_move("up", True)
			elif event.key == 32:
				swinging = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				s.should_move("left", False)
			elif event.key == pygame.K_d:
				s.should_move("right", False)
			if event.key == pygame.K_s:
				s.should_move("down", False)
			elif event.key == pygame.K_w:
				s.should_move("up", False)
			elif event.key == 32:
				swinging = False

	screen.blit(background_image, [0,0])
	if(starting_text == True):
		message_display("WELCOME PLAYER");
		message_players_name("Welcome Brave Adventurer", "Zack")
		if(tick % 60 == 0):	
			starting_text = False;
	else:
		health();
		# ADDS NEW ENEMY WHEN IT DIES
		CENTER_HANDLE_BIRD = 0;
		index_bird +=1
		if len(enemy_group_left)==0 or len(enemy_group_right) ==0:
			s.count +=1
			new_bird_left = Enemy(screen, 5, 4, 40)
			new_bird_right = Enemy(screen, 5, 4, 600)
			enemy_group_left.add(new_bird_left)
			enemy_group_right.add(new_bird_right)
			counter = True
			# WORK ON PAUSING SCREEN WHEN HIT 5
			# if(s.count == 5 and counter == True):
			# 	message_display("WELCOME PLAYER");
			# 	message_players_name("Welcome Brave Adventurer", "Zack")
			# 	if(tick % 60 == 0):	
			# 		counters = False;
		else:
			for bird in enemy_group_left:
				bird.fly_right(screen, index_bird%s.totalCellCount, CENTER_HANDLE_BIRD)
				bird.draw(screen, index_bird%s.totalCellCount, CENTER_HANDLE_BIRD)
			for bird in enemy_group_right:
				bird.fly_left(screen, index_bird%s.totalCellCount, CENTER_HANDLE_BIRD)
				bird.draw(screen, index_bird%s.totalCellCount, CENTER_HANDLE_BIRD)
		check_collision()
		# MOVES ARROW
		if swinging == True:
			index +=1
			if index % 13 ==0:
				new_arrow = Arrow(screen, s)
				arrows.add(new_arrow)
		elif swinging == False:
			index = 0
		#MOVES THE HERO
		CENTER_HANDLE = 0;
		s.draw(screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
		s.draw_me(screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
		for arr in arrows:
			arr.draw_bullet()
			arr.update()
		pygame.display.flip()