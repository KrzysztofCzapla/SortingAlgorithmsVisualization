import pygame, math
from settings import *
from data import *
from button import *

class Program():
	def __init__(self):
		# if game is supposed to run
		self.isRunning = True 
		# loading pygame
		pygame.init()
		# setting up screen
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		# setting clock for FPS and DeltaTime
		self.clock = pygame.time.Clock()

		self.objects = []

		# Data object with the list of values
		self.dataObject = DataObject(self)

		# Button for randomization
		self.buttonRandom = Button(self,WIDTH-300,20,"Randomize",200,40,self.dataObject.randomize)

		# Button for algorhitms to select
		self.buttonInsert = Button(self,10,20,"Insert Sort",270,40,self.dataObject.startInsert)
		self.buttonSelection = Button(self,10,80,"Selection Sort",270,40,self.dataObject.startSelect)
		self.buttonBubble = Button(self,300,20,"Bubble Sort",270,40,self.dataObject.startBubble)

		self.objects.append(self.dataObject)
		self.objects.append(self.buttonRandom)
		self.objects.append(self.buttonInsert)
		self.objects.append(self.buttonBubble)
		self.objects.append(self.buttonSelection)

	def checkEvents(self):
		# Checking every event for clicking X in top right corner
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					self.isRunning = False

	def update(self):
		# updating clock
		self.clock.tick(FPS)
		
		# fps meter
		pygame.display.set_caption(str(int(self.clock.get_fps())))

		for obj in self.objects:
			obj.update()

		
	def draw(self):
		self.screen.fill((0,0,0))

		for obj in self.objects:
			obj.draw()

		pygame.display.update()


	def run(self):
		self.checkEvents()
		self.update()
		self.draw()
		

if __name__ == "__main__":
	instance = Program()
	while instance.isRunning:
		instance.run()