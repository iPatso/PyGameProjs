import pygame, sys, os
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (700,700)
FPS = 60

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)

bg_path = os.path.join('data','Forest_2.png')
npc_on_borad_path = os.path.join('data','NPCpose1.png')
npc_image_path = os.path.join('data','NPC.png')
dialogue_box_path = os.path.join('data','dialogue_box.png')
player_image_path = os.path.join('data','main.png')

class Map(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(bg_path).convert()
		self.rect = self.image.get_rect()
		self.rect.center = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)
		self.x, self.y = self.rect.topleft
		
		self.player_rect = pygame.Rect(335,335,35,35)
		
		self.npc_on_board = pygame.image.load(npc_on_borad_path).convert_alpha()
		self.npc_rect = self.npc_on_board.get_rect()
		self.npc_pos = (self.x+900, self.y+830)
		
		self.npc_image = pygame.image.load(npc_image_path).convert_alpha()
		self.npc_image = pygame.transform.scale(self.npc_image, 
						(self.npc_image.get_width()/2, self.npc_image.get_height()/2))
		self.dialog_box = pygame.image.load(dialogue_box_path).convert_alpha()
		
		self.player_image = pygame.image.load(player_image_path).convert_alpha()
		self.player_image = pygame.transform.scale(self.player_image,
						(self.player_image.get_width()/2, self.player_image.get_height()/2))

				
		self.dia_boxes = arrayImgNonSquare(self.dialog_box, 208, 95)
		
	def checkCollision(self, collider, isNPC = False):
		if self.player_rect.colliderect(collider.right_wall):
			self.x = self.x - 2
			print "RIGHT WALL COLLIDED!!!"
			self.popUpDialogue(isNPC)
		elif self.player_rect.colliderect(collider.left_wall):
			self.x = self.x + 2
			print "LEFT WALL COLLIDED!!!"
			self.popUpDialogue(isNPC)
		elif self.player_rect.colliderect(collider.top_wall):
			self.y = self.y + 2
			print "TOP WALL COLLIDED!!!"
			self.popUpDialogue(isNPC)
		elif self.player_rect.colliderect(collider.bottom_wall):
			self.y = self.y - 2
			print "BOTTOM WALL COLLIDED!!!"
			self.popUpDialogue(isNPC)
			
	def popUpDialogue(self, isNPC):
		if isNPC:
			isTalking = True
			dialog_pos = 0
			dialog_MAX = 2
			while isTalking:
				pygame.display.update()
				screen.blit(self.dia_boxes[dialog_pos], (246, 590))
				screen.blit(self.npc_image, (510,275))
				screen.blit(self.player_image, (0,275))
				
				for event in pygame.event.get():
					if event.type == KEYDOWN and event.key == K_SPACE:
						dialog_pos += 1
				
				if dialog_pos == dialog_MAX:
					isTalking = False
					
	def update(self):
		self.rect.topleft = (self.x, self.y)
		if self.y >= -250:
			self.y = -250
		if self.rect.bottom <= WINDOW_SIZE[1]+225:
			self.rect.bottom = WINDOW_SIZE[1]+225
			self.y = self.rect.top
		if self.x >= -160:
			self.x = -160
		if self.rect.right <= WINDOW_SIZE[0]+230:
			self.rect.right = WINDOW_SIZE[0]+230
			self.x = self.rect.left
			
		# Collision checking (NOTE: we are hard coding all collision
		# for simple example purposes
		tree1 = Collider((self.x+560,self.y+755),45,45)
		tree2 = Collider((self.x+786,self.y+655),45,45)
		tree3 = Collider((self.x+865,self.y+540),45,45)
		tree4 = Collider((self.x+915,self.y+610),45,45)
		bush = Collider((self.x+850, self.y+650), 40, 40)
		log = Collider((self.x+640, self.y+760), 10, 10)
		sign = Collider((self.x+815, self.y+800), 15, 15)
		stump1 = Collider((self.x+900, self.y+795), 10, 5)
		stump2 = Collider((self.x+933, self.y+810), 10, 5)
		tallTree1 = Collider((self.x+975, self.y+770), 10, 38)
		tallTree2 = Collider((self.x+990, self.y+880), 10, 38)
		bucket = Collider((self.x+931, self.y+885), 5, 5)
		npc = Collider((self.x+900, self.y+830), 5, 5)
		
		self.checkCollision(tree1)
		self.checkCollision(tree2)
		self.checkCollision(tree3)
		self.checkCollision(tree4)
		self.checkCollision(bush)
		self.checkCollision(log)
		self.checkCollision(sign)
		self.checkCollision(stump1)
		self.checkCollision(stump2)
		self.checkCollision(tallTree1)
		self.checkCollision(tallTree2)
		self.checkCollision(bucket)
		self.checkCollision(npc, True)
		
			
class Collider():
	def __init__(self, (posx, posy), width, height):
		self.left_wall = pygame.Rect(posx, posy, 1, height)
		self.right_wall = pygame.Rect(posx+width, posy, 1, height)
		self.top_wall = pygame.Rect(posx, posy, width, 1)
		self.bottom_wall = pygame.Rect(posx, posy+height, width, 1)

class Player():
	def __init__(self):
		self.walk_L = pygame.image.load(os.path.join('data','sideleft.png')).convert_alpha()
		self.walk_R = pygame.image.load(os.path.join('data','sideright.png')).convert_alpha()
		self.walk_U = pygame.image.load(os.path.join('data','backside.png')).convert_alpha()
		self.walk_D = pygame.image.load(os.path.join('data','forward.png')).convert_alpha()
		self.stand_B = pygame.image.load(os.path.join('data','player_stand_back.png')).convert_alpha()
		self.stand_F = pygame.image.load(os.path.join('data','player_stand_front.png')).convert_alpha()
		self.stand_L = pygame.image.load(os.path.join('data','player_stand_left.png')).convert_alpha()
		self.stand_R = pygame.image.load(os.path.join('data','player_stand_right.png')).convert_alpha()
		
		self.x, self.y = (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
		
		self.ani_speed_init = 10
		self.ani_speed = self.ani_speed_init
		
		self.ani_L = arrayImg(self.walk_L, 35)
		self.ani_R = arrayImg(self.walk_R, 35)
		self.ani_U = arrayImg(self.walk_U, 35)
		self.ani_D = arrayImg(self.walk_D, 35)
		
		self.ani_pos = 0
		self.ani_max = 1 				# each animation has 2 frames
		self.img = self.ani_L[0]
		self.update(0, "sF")
		
	def update(self, pos, walk_stand_dir):
		if pos != 0:
			self.ani_speed -= 1
			if self.ani_speed == 0:
				if walk_stand_dir == "wL":
					self.img = self.ani_L[self.ani_pos]
				elif walk_stand_dir == "wR":
					self.img = self.ani_R[self.ani_pos]
				elif walk_stand_dir == "wU":
					self.img = self.ani_U[self.ani_pos]
				elif walk_stand_dir == "wD":
					self.img = self.ani_D[self.ani_pos]
				elif walk_stand_dir == "sL":
					self.img = self.stand_L
				elif walk_stand_dir == "sR":
					self.img = self.stand_R
				elif walk_stand_dir == "sF":
					self.img = self.stand_F
				elif walk_stand_dir == "sB":
					self.img = self.stand_B
					
				self.ani_speed = self.ani_speed_init
				if self.ani_pos == self.ani_max:
					self.ani_pos = 0
				else:
					self.ani_pos += 1
		screen.blit(self.img, (self.x, self.y))


def arrayImgNonSquare(image, width, height):
	sub = image.get_rect()
	subx = sub[2]/width
	suby = sub[3]/height
	dummy = (0,0)
	images = []
	while dummy[0] < suby:
		while dummy[1] < subx:
			newrect = (dummy[1]*width,
                       dummy[0]*height,
                       width, height)
			images.append(image.subsurface(newrect))
			dummy = (dummy[0], dummy[1]+1)
		dummy = (dummy[0]+1, 0)
	return images


def arrayImg(image, size):
	sub = image.get_rect()
	subx = sub[2]/size
	suby = sub[3]/size
	dummy = (0,0)
	images = []
	while dummy[0] < suby:
		while dummy[1] < subx:
			newrect = (dummy[1]*size,
                       dummy[0]*size,
                       size, size)
			images.append(image.subsurface(newrect))
			dummy = (dummy[0], dummy[1]+1)
		dummy = (dummy[0]+1, 0)
	return images


def main():
	player1 = Player()
	pos = 0
	
	town = Map()
	townSprite = pygame.sprite.RenderPlain((town))
	walk_stand_dir = ""
	while True:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if event.key == K_RIGHT:
					pos = 0
					walk_stand_dir = "sR"
				if event.key == K_LEFT:
					pos = 0
					walk_stand_dir = "sL"
				if event.key == K_UP:
					pos = 0
					walk_stand_dir = "sF"
				if event.key == K_DOWN:
					pos = 0
					walk_stand_dir = "sB"
				
		key = pygame.key.get_pressed()
		if key[K_LEFT]:
			town.x += 2
			pos = 1
			walk_stand_dir = "wL"		
		elif key[K_RIGHT]:
			town.x -= 2
			pos = 1
			walk_stand_dir = "wR"
		elif key[K_UP]:
			town.y += 2
			pos = 1
			walk_stand_dir = "wU"
		elif key[K_DOWN]:
			town.y -= 2
			pos = 1
			walk_stand_dir = "wD"
				
				
				
		townSprite.update()
		townSprite.draw(screen)		
				
		screen.blit(town.npc_on_board, (town.x+900, town.y+830))
		
		player1.update(pos, walk_stand_dir)
		pygame.display.update()
	
	
	
if __name__ == '__main__':
	main()
