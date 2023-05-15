import math, random, time
from settings import *

class DataObject():
	"""docstring for DataObject"""
	def __init__(self, program):
		self.program = program
		self.list = [0]
		
		self.minElements, self.maxElements = 10,20
		self.minValue, self.maxValue = 1,100

		self.color = (0,0,0)


		# time stuff
		self.sortingCooldown = 0.1
		self.sortingTime = 0

		# instert
		self.isInserting = False
		# iterations
		self.insertIteration = 1
		# which element is looked at basically
		self.j = 1

		# select
		self.isSelecting = False
		# iterations
		self.selectIteration = 0
		# which element is looked at basically
		self.s = 1

		# bubble
		self.isBubble = False
		# iterations
		self.bubbleIteration = 0
		# which element is looked at basically
		self.b = 0
		
		self.randomize()

	def randomize(self):
		# randomize list
		self.list = []
		numberOfElement = random.randint(self.minElements,self.maxElements)
		for element in range(numberOfElement):
			self.list.append(["Idle",random.randint(self.minValue,self.maxValue)])

	def startInsert(self):
		self.isInserting = True

	def insertionSort(self):
		

		# if inserting is true and cooldown isnt down		
		if self.isInserting == True and time.time() >= self.sortingTime+self.sortingCooldown:
			# j has to be bigger than zero so we can go thru the list			
			if self.j > 0:
				self.list[0][0] = "Idle"
				# sawp the elements if he one were looking at is lower
				if self.list[self.j][1] < self.list[self.j-1][1]:
					self.list[self.j][1], self.list[self.j-1][1] = self.list[self.j-1][1], self.list[self.j][1]

				# set the names so we can color acordingly
				self.list[self.j-1][0] = "Lower"
				self.list[self.j][0] = "Idle"

				# lower j so next tiem were looking at the next element
				self.j -= 1

			self.sortingTime = time.time()

			if self.insertIteration < len(self.list):
				# start another iteration if one is over
				if self.j == 0:
					self.insertIteration += 1
					
					if self.insertIteration < len(self.list):
						self.j = self.insertIteration
						
			else:
				self.isInserting = False
				self.insertIteration = 1
				self.list[0][0] = "Idle"
		#print(self.list)

	def startSelect(self):
		self.isSelecting = True
	
	def selectionSort(self):
		
		if self.isSelecting == True and time.time() >= self.sortingTime+self.sortingCooldown:
			if self.s < len(self.list):

				# set em to green color so everything isnt red
				self.list[self.s-1][0] = "Idle"
				self.list[self.s-2][0] = "Idle"
					
				# select minimum index
				min_index = self.selectIteration
				
				self.list[min_index][0] = "Lower"

				# if current is minimum, set minimum to that	
				if self.list[self.s][1] < self.list[min_index][1]:
					min_index = self.s

				# swap em(if minimum isnt change, nothing will happen)		
				self.list[self.selectIteration][1], self.list[min_index][1] = self.list[min_index][1], self.list[self.selectIteration][1]
				self.list[len(self.list)-1][0] = "Idle"


				if self.s == 1:
					self.list[0][0] = "Lower"
				self.list[self.s][0] = "Lower"

				self.list[min_index][0] = "Lower"
				print(min_index)
				
				self.s += 1

				self.sortingTime = time.time()
			

			# Check if we arent out of range
			if self.selectIteration < len(self.list):
			# start another iteration if one is over
				if self.s == len(self.list):
					self.selectIteration += 1
					
					if self.selectIteration < len(self.list):
						self.s = self.selectIteration+1
					
			else:
				self.isSelecting = False
				self.selectIteration = 0
				self.s = 1
				self.list[0][0] = "Idle"
				
	def startBubble(self):
		self.isBubble = True

	def bubbleSort(self):
		

		# if inserting is true and cooldown isnt down		
		if self.isBubble == True and time.time() >= self.sortingTime+self.sortingCooldown:
			# j has to be bigger than zero so we can go thru the list			
			self.list[self.b][0] = "Idle"

			# check if we arent out of range
			if self.bubbleIteration > 0:
				self.list[len(self.list)-self.bubbleIteration][0] = "Idle"
			# ^
			if self.b <= len(self.list)-1-self.bubbleIteration:

				# check if the element is bigger
				if self.list[self.b][1] > self.list[self.b + 1][1]:

					# swapping elements if elements
					# are not in the intended order
					temp = self.list[self.b][1]
					self.list[self.b][1] = self.list[self.b+1][1]
					self.list[self.b+1][1] = temp
				self.list[self.b+1][0] = "Lower"

				self.b += 1

				self.sortingTime = time.time()


			# check if nothing si out of range, otherwise end the loop
			if self.bubbleIteration < len(self.list):
				# start another iteration if one is over
				if self.b == len(self.list)-1-self.bubbleIteration:
					self.bubbleIteration += 1
					
					if self.bubbleIteration < len(self.list):
						self.b = 0
						
			else:
				self.isBubble = False
				self.bubbleIteration = 0
				self.list[0][0] = "Idle"			

	def draw(self):
		# Getting the biggest element to properly scale #
		biggest = 0
		for element in self.list:
			if element[1] > biggest:
				biggest = element[1]
		#################################################

		# Calculating spacing between	
		spacing = int(WIDTH/(len(self.list)+1))

		# Getting the cords
		x = int(spacing)
		y = int(HEIGHT*9/10)


		# Getting basic data heights and widths
		dataHeight = int(HEIGHT*6/10)
		dataWidth = int(WIDTH*1/len(self.list)/4)

		for element in self.list:
			# setting individual heights based on number
			elementHeight = dataHeight*element[1]/biggest
			elementWidth = dataWidth

			# drawing rect (screen,color,(x,y,width,height))
			#print(element[0])
			if element[0] == "Idle":
				self.color = COLOR
			else:
				self.color = COLOR_ELEMENT

			pygame.draw.rect(self.program.screen,self.color,(x-elementWidth,y-elementHeight,elementWidth,elementHeight))
			# spacing
			x += spacing

		
		

	def update(self):
		self.insertionSort()
		self.selectionSort()
		self.bubbleSort()
		#print(self.isSelecting)
		#print(f"j {self.j}")
		#print(f"i {self.insertIteration}")
		#pass


