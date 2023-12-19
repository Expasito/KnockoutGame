
from math import sqrt
import pygame, sys
from pygame.locals import *
import random, time


class Knockout:
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 800

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	FPS = pygame.time.Clock()

	bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

	frameRate = 240.0

	SCALE = 64

	entities = []


	def __init__(self):
		pygame.init()
		Knockout.FPS.tick(Knockout.frameRate)
		pygame.display.set_caption("Knockout")

	
	class Entity(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)



	class Penguin(Entity):

		# half a meter
		radius = 1

		# in kilograms
		mass = 18.0

		mu = 0.1

		def __init__(self, x ,y):
			Knockout.Entity.__init__(self)
			self.image = pygame.Surface((32,32))
			self.image.convert()
			self.image.fill(pygame.Color("#DDDDDD"))
			self.rect = pygame.Rect(x,y,32,32)

			self.x = x;
			self.y = y;

			# start with 0 velocity
			self.vx = 0
			self.vy = 0

			self.ex = 0

		def draw(self):
			pygame.draw.ellipse(Knockout.screen,"#DDAADD",(self.x*Knockout.SCALE,self.y*Knockout.SCALE,Knockout.Penguin.radius*Knockout.SCALE,Knockout.Penguin.radius*Knockout.SCALE),1)

		def update(self, entities):
		
			#self.y += self.vy - self.vx * .8

		
			#self.vx = self.vx 

			# energy initial = 1/2 * m * v*v + Wother
			# energy final = 1/2 * m *v*v

			# Wother = force * distance, where force = mu*normal

			# figure out how much energy was lost
			wOther = self.vx/Knockout.frameRate * Knockout.Penguin.mass * -9.8 * Knockout.Penguin.mu


			eInitial = 1/2 * Knockout.Penguin.mass * self.vx *self.vx

			eFinal = eInitial + wOther

			if(eFinal >= 0):
				self.vx = sqrt(2 * eFinal/Knockout.Penguin.mass)
			else:
				self.vx = 0

			self.x += self.vx/Knockout.frameRate
			


			print("Energy: ", eFinal)


	def addPenguin(self, penguin):
		self.entities.append(penguin)

	def setVel(self, index, vx, vy):
		self.entities[index].vx = vx
		self.entities[index].vy = vy


	def tick(self):
		for event in pygame.event.get():
			print("Event: ", event)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		Knockout.screen.fill((255,255,255))

		# simulate physics first
		for e in Knockout.entities:
			e.update(Knockout.entities)


		# draw them to the screen
		for e in Knockout.entities:
			e.draw()

		pygame.display.update()
		Knockout.FPS.tick(Knockout.frameRate)

	def simulate(self):
		while True:
			self.tick()

			check = False
			for e in Knockout.entities:
				if e.vx != 0.0:
					check = True

			if check == False:
				return






def main():

	knockout = Knockout()

	knockout.addPenguin(Knockout.Penguin(1,1))

	knockout.setVel(0,1,1)

	knockout.simulate()

	knockout.setVel(0,-1,-1)

	knockout.simulate()



	#print("Does this work?")

	#entities = []
	#entities.append(Penguin(1,1))
	#entities.append(Penguin(2,2))
	#entities.append(Penguin(3,3))
	#entities.append(Penguin(4,4))
	#entities.append(Penguin(5,5))
	#entities.append(Penguin(6,6))

	##entities.append(p2)

	#entities[0].vx = 6

	##p.vx = 1

	#while True:
	#	for event in pygame.event.get():
	#		print("Event: ", event)
	#		if event.type == QUIT:
	#			pygame.quit()
	#			sys.exit()

	#	screen.fill((255,255,255))

	#	# simulate physics first
	#	for e in entities:
	#		e.update(entities)


	#	# draw them to the screen
	#	for e in entities:
	#		e.draw()

	#	pygame.display.update()
	#	FPS.tick(frameRate)



if __name__ == __name__:
	main()