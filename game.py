import pygame
from SpriteSheet import SpriteSheet
from pygame.sprite import Group, groupcollide
from Arrow import Arrow
from Enemy import Enemy


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
bird = Enemy(screen, 5, 4, 10, 100)
enemy_group = Group()
enemy_group.add(bird)

def check_collision():
	pygame.sprite.groupcollide(arrows, enemy_group, False, True)

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
		CENTER_HANDLE_BIRD = 0;
		index_bird +=1
		if len(enemy_group) ==0:
			s.count +=1
			new_bird = Enemy(screen, 5, 4, 40, 150)
			enemy_group.add(new_bird);
		else:
			for bir in enemy_group:
				bir.update(screen, index_bird%s.totalCellCount, CENTER_HANDLE_BIRD)
				bir.draw(screen, index_bird%s.totalCellCount, CENTER_HANDLE_BIRD)
		
		check_collision()
		if swinging == True:
			index +=1
			if index % 13 ==0:
				new_arrow = Arrow(screen, s)
				arrows.add(new_arrow)
		elif swinging == False:
			index = 0
		CENTER_HANDLE = 0;
		s.draw(screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
		s.draw_me(screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
		for arr in arrows:
			arr.draw_bullet()
			arr.update()
		pygame.display.flip()
			


