
from ssl import VERIFY_CRL_CHECK_LEAF
import pygame, sys
from pygame.locals import *
import random, time, math


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

		width = 32
		height = 32

		def __init__(self, x ,y):
			Knockout.Entity.__init__(self)
			self.image = pygame.Surface((Knockout.Penguin.width, Knockout.Penguin.height))
			self.image.convert()
			self.image.fill(pygame.Color("#DDDDDD"))
			self.rect = pygame.Rect(x,y,Knockout.Penguin.width, Knockout.Penguin.height)

			self.x = x;
			self.y = y;

			# start with 0 velocity
			self.vx = 0
			self.vy = 0

			self.ex = 0

		def draw(self):
			

			pygame.draw.ellipse(Knockout.screen,"#DDAADD",(self.x*Knockout.SCALE - Knockout.Penguin.width,self.y*Knockout.SCALE - Knockout.Penguin.height,Knockout.Penguin.radius*Knockout.SCALE,Knockout.Penguin.radius*Knockout.SCALE),1)


		def update(self):

			# idea behind how it works
			# energy initial = 1/2 * m * v*v + Wother
			# energy final = 1/2 * m *v*v

			# Wother = force * distance, where force = mu*normal

			# handle x first


			theta = math.atan2(self.vy,self.vx)

			velocity = math.sqrt(self.vx*self.vx + self.vy*self.vy)

			initialEnergy = 1/2*Knockout.Penguin.mass * velocity * velocity

			work = velocity/Knockout.frameRate * Knockout.Penguin.mass * -9.8 * Knockout.Penguin.mu

			finalEnergy = initialEnergy + work

			if finalEnergy > 0:
				vel = math.sqrt(2*finalEnergy/Knockout.Penguin.mass)
			else:
				vel = 0

			self.vx = math.cos(theta)*vel
			self.vy = math.sin(theta)*vel


			self.x += self.vx/Knockout.frameRate
			self.y += self.vy/Knockout.frameRate




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
			e.update()

		# check for colissions
		for e in Knockout.entities:
			for e2 in Knockout.entities:
				if e == e2:
					continue

				dist = math.sqrt((e.x-e2.x)**2 + (e.y-e2.y)**2)
				if dist < Knockout.Penguin.radius:
					momentumInitialX = Knockout.Penguin.mass * e.vx + Knockout.Penguin.mass * e2.vx
					momentumInitialY = Knockout.Penguin.mass * e.vy + Knockout.Penguin.mass * e2.vy

					print("Collide!")
					#e.vx *= -1
					#e2.vx *= -1
				


		# draw them to the screen
		for e in Knockout.entities:
			e.draw()

		pygame.display.update()
		Knockout.FPS.tick(Knockout.frameRate)

	def simulate(self):
		while True:
			self.tick()

			

			# check if all entities have 0 velocity
			check = False
			for e in Knockout.entities:
				if e.vx != 0.0:
					check = True

			if check == False:
				return






def main():

	knockout = Knockout()

	knockout.addPenguin(Knockout.Penguin(5,5))
	knockout.addPenguin(Knockout.Penguin(6,4))


	knockout.setVel(0,1,0)

	knockout.simulate()

	knockout.setVel(0,0,-1)

	knockout.simulate()

	knockout.setVel(0,-1,0)

	knockout.simulate()

	knockout.setVel(0,0,1)

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