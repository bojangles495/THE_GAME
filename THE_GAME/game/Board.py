import spyral
import random
import math
import Walls

WIDTH = 600
HEIGHT = 600
BG_COLOR = (255,255,255)
BLACK = (0, 0, 255)
SIZE = (WIDTH, HEIGHT)
SIZE2 = (WIDTH/2, HEIGHT/2)
WALL_LIST = []
class Board(spyral.Scene):
	text = '';
	def __init__(self, *args, **kwargs):
		#global manager
		#for x in range(0,9):
			
		spyral.Scene.__init__(self, SIZE)
		#self.walls = Walls.Walls(self)
		spyral.event.register("system.quit", spyral.director.pop) 
		spyral.event.register("input.keyboard.down.q", spyral.director.pop)

	def setText(self,string):
		self.text = string

	def getText(self):
		return self.text

	def setBackGround(self,imagePath):
		self.background = spyral.Image(filename=imagePath)
	def setWalls(self,quadrantRow,quadrantColumn):
		if(quadrantRow == 0 and quadrantColumn == 0):
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallTopFull())
			wall = Walls.Walls(self)
			WALL_LIST.append(wall.wallLeftFull())

		
