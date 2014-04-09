import spyral
import Main

def main():
	scene_matrix = [[0 for x in xrange(5)] for x in xrange(5)]#sets up the 4x4 game board
	backGroundImage = 1
	for i in range(5):
		for j in range(5):
			gameBoard = Board.Board()
			gameBoard.setBackGround("game/sceneImages/1.jpg")
			gameBoard.setWalls(i,j)
			scene_matrix[i][j] = gameBoard
			#once everything works uncomment these and fix images sizes
			#gameBoard.setBackGround("game/sceneImages/"+str(backGroundImage)+".jpg")
			#backGroundImage = backGroundImage + 1
	spyral.director.init(size=(0, 0), max_ups=30, max_fps=30, fullscreen=False, caption='The Game')
	spyral.director.push(Main.Main())
	#gameBoard = Board.Board()
	#gameBoard.setBackGround("game/sceneImages/1.jpg")
	spyral.director.push(scene_matrix[0][0])
	print gameBoard.getText()
	#spyral.event.register("input.keyboard.down.r", spyral.director.push(self.scene2))
	#self.sene2 = spyral.Scene.__init__(self,SIZE2)
