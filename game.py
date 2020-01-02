import pygame
import random
import time
import q_l


pygame.init()

game_width = 800
game_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

game_disp = pygame.display.set_mode((game_width,game_height))
clock = pygame.time.Clock()

def player(start_x,start_y):
	pygame.draw.rect(game_disp,red,[start_x,start_y,100,100],0)

def obstracles(start_ox,start_oy):
	pygame.draw.rect(game_disp,blue,[start_ox,start_oy,100,100],0)

def crash(x,y,o_x,o_y):
	if x < 0 or x > game_width-100:
		return False
	if y < o_y+100:
		if (o_x > x and o_x < x+100) or (o_x < x and o_x+100 > x):
			return False
		else:
			return True
	else:
		return True

def scores(c):
	font = pygame.font.SysFont(None,25)
	text = font.render('score : ' + str(c),True,white)
	game_disp.blit(text,(0,0))

def msg_disp():
	font = pygame.font.SysFont(None,55)
	text = font.render('GAME OVER',True,white)
	game_disp.blit(text,(290,280))
	pygame.display.update()
	time.sleep(2)

def game_loop():
	game_ext = True
	x = (game_width /2) -50
	y = game_height * (5/6)
	obstarcle_speed = 5
	sx = random.randint(0,game_width-100)
	sy = -100
	x_c = 0
	count = 1
	i = 5
	while game_ext:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
			#if event.type == pygame.KEYDOWN:
			#	if event.key == pygame.K_LEFT:
			#		x_c = -4
			#	elif event.key == pygame.K_RIGHT:
			#		x_c = 4
			#if event.type == pygame.KEYUP:
			#	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			#		x_c = 0
		d = [[x,400-x,sx,sy]]
		x_c = q_l.my_agent(d)
		x += x_c
		sy += obstarcle_speed
		#if i % 5 == 0:
		#	q_l.data_to_train(x,sx,sy,x_c)
		#	i += 1
		#else:
		#	i += 1
		if count % 10 == 0:
			obstarcle_speed += 0.01
		game_l_ext = crash(x,y,sx,sy)
		game_disp.fill(black)
		player(x,y)
		obstracles(sx,sy)
		if game_l_ext == False:
			msg_disp()
			game_ext = False
		if sy > game_height:
			sx = random.randint(0,game_width-100)
			sy = -100
			count += 1
		scores(count)
		pygame.display.update()
		clock.tick(60)


def main():
	while True:
		game_loop()
		#print(q_l.train_data)
		#q_l.cvt_train_data_to_csv(q_l.train_data)


main()










