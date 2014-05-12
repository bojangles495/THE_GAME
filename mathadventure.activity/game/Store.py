import spyral
import random
import math
import Item
import Board

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
FONT_PATH = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
ITEM_BOUGHT_LIST = []

class ItemSprite(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = spyral.Image(filename=img)
		self.x = x
		self.y = y

class ItemText(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y

class PurchaseText(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y

class Store(spyral.Scene):
	def __init__(self,character):
		spyral.Scene.__init__(self, SIZE)
		self.background = spyral.Image(size=SIZE).fill((255,255,255))
		spyral.event.register("system.quit", spyral.director.pop)
		spyral.event.register("input.keyboard.down.x", self.closeStore)
		spyral.event.register('director.update', self.update)
		self.message = ''
		spyral.event.register("input.keyboard.down.a", self.buyHealth)#buy health
		spyral.event.register("input.keyboard.down.b", self.buyGem)#buy gem
		spyral.event.register("input.keyboard.down.c", self.buyChest)#buy gem
		spyral.event.register("input.keyboard.down.e", self.buySprite1)#buy sprite1
		spyral.event.register("input.keyboard.down.f", self.buySprite2)#buy sprite1
		self.shopFont = spyral.Font(FONT_PATH,24,(0,0,0))#font used for header
		self.itemFont = spyral.Font(FONT_PATH,14,(0,0,0))#font used for prices
		self.purchaseFont = spyral.Font(FONT_PATH,18,(255,0,0))#font used for purchase status
		self.storeHeaderFont = spyral.Font(FONT_PATH,80,(0,0,0))#font used for purchase status
		storeHeaderImg = self.storeHeaderFont.render("STORE")
		itemSelectionText = ItemText(self,storeHeaderImg,(WIDTH/3),(20))
		self.storeQuitFont = spyral.Font(FONT_PATH,18,(0,0,0))#font used for purchase status
		storeInstImg1 = self.storeQuitFont.render("Press the key next to")
		storeInstImg2 = self.storeQuitFont.render("the item to purchase it.")
		storeInstImg3 = self.storeQuitFont.render("Press x to exit the store")
		itemInstText1 = ItemText(self,storeInstImg1,20,20)
		itemInstText2 = ItemText(self,storeInstImg2,20,50)
		itemInstText3 = ItemText(self,storeInstImg3,20,80)
		self.purchaseMessage = ''
		row_val = [(HEIGHT/4.5),(HEIGHT/2),(HEIGHT/1.286)]
		column_val = [0,(WIDTH/4),(WIDTH/2),(WIDTH/1.34)]
		itemSelection = ["a)","b)","c)","d)","e)","f)","g)","h)","i)","j)","k)","l)"]
		itemPrice = ["10","20","20","90","Free","120","N/A","N/A","N/A","N/A","N/A","N/A"]
		itemImageArray = self.setItemImgArray("game/store/imgFile.txt")
		itemDescrip = self.setItemImgArray("game/store/itemText.txt")
		itemSelectionIndex = 0
		self.player = character

		for row_value in row_val:
			for column_value in column_val:
				itemString = self.itemFont.render(itemSelection[itemSelectionIndex])
				itemSelectionText = ItemText(self,itemString,(column_value + 10),row_value)
				itemImg = ItemSprite(self,itemImageArray[itemSelectionIndex],(column_value + 70),row_value)
				itemPriceImg = self.itemFont.render("Price: " + itemPrice[itemSelectionIndex])
				itemPriceImgText = ItemText(self,itemPriceImg,(column_value + 70),(row_value + 110))
				itemDescription = self.itemFont.render(itemDescrip[itemSelectionIndex])
				itemSelectionDescription = ItemText(self,itemDescription,(column_value + 70),(row_value + 140))
				itemSelectionIndex += 1

	def setItemImgArray(self,animationPath):
		data=[]                               # will hold the lines of the file
		with open(animationPath,'rU') as fin:
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
					data.append(line)
		return data

	def update(self,delta):
		if(self.message != ''):
			if(self.purchaseMessage == ''):
				img = self.purchaseFont.render(self.message)
				self.purchaseMessage = PurchaseText(self,img,(WIDTH/1.34),50)
				self.message = ''
			else:
				self.purchaseMessage.kill()
				img = self.purchaseFont.render(self.message)
				self.purchaseMessage = PurchaseText(self,img,(WIDTH/1.34),50)
				self.message = ''
						
	def closeStore(self):
		self.player.vel = 100
		self.sceneReturn.setCharacter(self.player,self.player.ani_array)
		
		spyral.director.pop()

		spyral.director.get_scene().defreezeMonster()
					
				
	def buyHealth(self):
		#need to check if if player has enough points
		if(self.player.totalScore >= 10):
			self.player.health = 150
			self.player.totalScore -= 10
			self.message = "Health was replenished!"
		else:
			self.message = "You don't have a enough points!"

	def buyGem(self):
		if(self.player.totalScore >= 20):
			self.sceneReturn.addGem()
			self.player.totalScore -= 20
			self.message = "A Gem was added to the Map!"
		else:
			self.message = "You don't have a enough points!"

	def buyChest(self):
		if(self.player.totalScore >= 20):
			self.sceneReturn.addChest()
			self.player.totalScore -= 20
			self.message = "A Chest was added to the Map!"
		else:
			self.message = "You don't have a enough points!"

	def buySprite1(self):
		self.player.ani_array = ["game/images/Animations/rightanimation.txt","game/images/Animations/stop2.bmp","game/images/Animations/leftanimation.txt","game/images/Animations/stop2l.bmp","game/images/Animations/upanimation.txt","game/images/Animations/stop2.bmp","game/images/Animations/downanimation.txt","game/images/Animations/stop2.bmp"]
		self.player.setStopImage("game/images/Animations/stop2l.bmp")
		self.message = "You changed your character!"	

	def buySprite2(self):
		if(self.player.totalScore >= 120):
			self.player.ani_array = ["game/images/Animations/linkAnimation/linkanimationright.txt","game/images/Animations/linkAnimation/linkright.bmp","game/images/Animations/linkAnimation/linkanimationleft.txt","game/images/Animations/linkAnimation/linkleft.bmp","game/images/Animations/linkAnimation/linkanimationup.txt","game/images/Animations/linkAnimation/linkup.bmp","game/images/Animations/linkAnimation/linkanimationdown.txt","game/images/Animations/linkAnimation/linkdown.bmp"]
			self.player.setStopImage("game/images/Animations/linkAnimation/linkdown.bmp")
			self.player.totalScore -= 120
			self.message = "You changed your character!"
		else:
			self.message = "You don't have enough points!"
		

	def setSceneReturn(self,scene):
		self.sceneReturn = scene

