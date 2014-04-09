import spyral
import random
import math

WIDTH = 600
HEIGHT = 600
BLACK = (0,0,0)
class Walls(spyral.Sprite):
	def __init__(self, scene):
        	spyral.Sprite.__init__(self, scene)
	
	def wallTopFull(self):
		self.image = spyral.Image(size=(WIDTH, 30)).fill(BLACK)
		#self.image = spyral.Image(size=(WIDTH/2, 30)).fill(BLACK)
		#self.x = WIDTH / 2
		#self.y = HEIGHT - 20
	
	def wallLeftFull(self):	
		self.image = spyral.Image(size=(30, HEIGHT)).fill(BLACK)
