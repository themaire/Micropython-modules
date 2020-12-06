
# -*- coding: utf-8 -*-

##### Variables #####

colorList = {
	'red': (255, 0, 0),
	'red light': (100, 0, 0),
	'red superlight': (50, 0, 0),
	'orange': (255, 60, 0),
	'citrus': (102, 68, 0),
	'brown light': (80, 78, 0),
	'skin': (120, 120, 0),
	'pink': (255, 51, 204),
	'pink flash': (255, 23, 120),
	'pink light': (255, 128, 223),
	'mouth': (255, 102, 102),

	'green': (0, 255, 0),
	'green light': (0, 102, 0),

	'blue': (0, 0, 255),
	'blue light': (0, 153, 255),
	'salopette': (0, 19, 127),

	'yellow': (255, 255, 51),
	'yellow pie': (255, 153, 0),
	'purple': (90, 0, 150),

	'white': (255, 255, 255),
	'white light': (30,30,30),
	'blank': (0, 0, 0)
	}

# ---->

##### Fonctions #####

def colors(color):
	return colorList[color]

def colorlist():
	for i in colorList:
		print (i, colorList[i], sep=" ")
	# ou bien sinon :
	#for key, elem in colorList.items():
		#print key, elem


# test des deux fonctions
if __name__ == "__main__":

	print ("Liste lisible des couleurs :")
	print (colorlist())
	
	print ('Appel de la couleur "orange" :')
	print (colors('orange'))
