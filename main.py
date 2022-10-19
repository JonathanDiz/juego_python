import pygame, sys
from player import Player
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Little While')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('./layout/audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

	def intro_screen(self):
		intro = True
		ruta_intro_background = './layout/graphics/start screen/beansjam_startscreen.png'
		new_ancho = WIDTH / 2
		new_alto = HEIGTH
		imagen_original = pygame.image.load(ruta_intro_background)
		imagen_redimensionada = pygame.transform.scale(imagen_original, (new_ancho,new_alto))
		
		
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro = False
					self.running = False
				
			self.screen.blit(imagen_redimensionada, (320,0))
			
			pygame.display.update()
			self.clock.tick(FPS)
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER:
					intro = True
					self.running = True
					game.run()

def game_over(self):
		game_over = True
		ruta_game_over = './layout/graphics/game over/game_over.png'
		ancho = WIDTH
		alto = HEIGTH
		img_original = pygame.image.load(ruta_game_over)
		img_redimensionada = pygame.transform.scale(img_original, (ancho,alto))

		while game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_over = False
				
			self.screen.blit(img_redimensionada, (0,0))
			
			pygame.display.update()
			self.clock.tick(FPS)

			if Player.health == Player.kill:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_KP_ENTER:
						game_over = True
						game.run()

if __name__ == '__main__':
	game = Game()
	game.intro_screen()
