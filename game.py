import pygame
from SpriteSheet import SpriteSheet

pygame.init()

W,H = 800, 500
HW, HH, = W/2, H/2
Area = W * H


screen = pygame.display.set_mode((W,H))


background_image_original = pygame.image.load("./images/background3.png")
background_image = pygame.transform.scale(background_image_original, [800, 500])


def event_handle():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

def game_loop():
	game_on = True
	s_original = pygame.image.load("./images/archer2.png")
	s_resize = pygame.transform.scale(s_original, [300, 200])
	s = SpriteSheet(s_resize, 4, 2)
	CENTER_HANDLE = 0;
	index = 6;

	while game_on:
		event_handle();
		screen.blit(background_image, [0,0])
		s.draw(screen, index%s.totalCellCount, HW, HH, CENTER_HANDLE)
		index +=1
		pygame.display.flip();

game_loop();
