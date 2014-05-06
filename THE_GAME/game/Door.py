import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

class Door(spyral.Sprite):
    def __init__(self):
        '''self.image = spyral.Image(size=(5, 20)).fill((0, 0, 0))
                                self.anchor = "midleft"
                                self.x = WIDTH - 200
                                self.y = 60
                                self.health = 150'''


    def setScene(self,scene):
        super(Door,self).__init__(scene)
        print("testing door")
            
    def setImage(self):
        self.image = spyral.Image(size=(500, 200)).fill((0, 0, 200))#spyral.Image(filename="game/images/door2.png")
        self.anchor = "center"
        self.x = WIDTH/2
        self.y = 360
        print("testing door")
        
    def setUpdate(self,scene):
        spyral.event.register('director.update', self.update)


    