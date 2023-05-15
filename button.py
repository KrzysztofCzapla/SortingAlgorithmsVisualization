import math,time 
from settings import *
import pygame
pygame.init()



class Button():
	"""docstring for DataObject"""
	def __init__(self, program,x,y,text,width=100,height=50,function=None):
		self.program = program
		self.x, self.y = x,y
		self.height,self.width = height,width
		self.text = text
		self.alreadyPressed = False
		self.colorBackground = COLOR_BACKGROUND
		self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.function = function
		self.time = 0
		self.cooldown = 0.3

	def draw(self):

		pygame.draw.rect(self.program.screen,self.colorBackground,(self.x,self.y,self.width,self.height))

		text_surface = FONT.render(self.text, False, COLOR)
		self.program.screen.blit(text_surface, (self.x+self.width*1/50,self.y))

		

	def update(self):
		#print(self.alreadyPressed)
		mousePos = pygame.mouse.get_pos()
		# if mosue collides
		if self.buttonRect.collidepoint(mousePos):
			self.colorBackground = (205,240,255)
			# if mouse is pressed and button isnt pressed and cooldown is over
			if pygame.mouse.get_pressed(num_buttons=3)[0] and self.alreadyPressed == False and (time.time()-self.cooldown)>self.time:
				if self.function != None:
					self.function()
				self.alreadyPressed = True
				# update time
				self.time = time.time()
			else:
				self.alreadyPressed = False
		else:
			self.colorBackground = COLOR_BACKGROUND