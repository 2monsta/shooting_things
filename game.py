import pygame
from SpriteSheet import SpriteSheet

pygame.init()

W,H = 800, 500
HW, HH, = W/2, H/2
Area = W * H

screen = pygame.display.set_mode((W,H))
background_image_original = pygame.image.load("./images/background3.png")
background_image = pygame.transform.scale(background_image_original, [800, 500])
s_original = pygame.image.load("./images/archer.png")
# s_resize = pygame.transform.scale(s_original, [600, 470])
s = SpriteSheet(s_original, 13, 1, screen)
def event_handle():
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
				index = 5
				CENTER_HANDLE = 0;
				s.jump(True, screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
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
				index = 5
				CENTER_HANDLE = 0;
				s.jump(False,screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)

game_on = True
index = 0;
tick = 0
while game_on:
	tick +=1
	event_handle();
	screen.blit(background_image, [0,0])
	if tick % 10 == 0:
		index +=1;
	CENTER_HANDLE = 0;
	s.draw(screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
	s.draw_me(screen, index%s.totalCellCount, 600, 350, CENTER_HANDLE)
	
	pygame.display.flip()
