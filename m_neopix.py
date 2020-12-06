

from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

from utils.m_color_list import *

class ledRing:
	def __init__(self, pin, nb, no = 0):
		self.no = no
		self.nb = nb

		self.np = NeoPixel(Pin(pin), self.nb)

	def cycle(self, color, full = 0):
		for i in range(4 * self.nb):
			for j in range(self.nb):
				self.np[j] = (0, 0, 0)
			self.np[i % self.nb] = colors(color)
			self.np.write()
			sleep_ms(25)

	def cycleFull(self):
		for color in colorList:
			self.cycle(color)

	def bounce(self):
		for i in range(4 * self.nb):
			for j in range(self.nb):
				self.np[j] = (0, 0, 128)
			if (i // self.nb) % 2 == 0:
				self.np[i % self.nb] = (0, 0, 0)
			else:
				self.np[self.nb - 1 - (i % self.nb)] = (0, 0, 0)
			self.np.write()
			sleep_ms(60)

	def fade(self,div=8):
		for i in range(0, 4 * 256, div): # Puissance progressive jusqu'a 256 avec un pas de 8.
			for j in range(self.nb): # Boucle sur chaque LED
				if (i // 256) % 2 == 0: # Un coup 0 < 256 ... puis 1 > 512 ...
					val = i & 0xff # Si i dépasse 256, i vaudra la valeur dépassée
				else:
					val = 255 - (i & 0xff)
				self.np[j] = (val, 0, 0)
			self.np.write()
		self.clear()

	def clear(self):
		for i in range(self.nb):
			self.np[i] = (0, 0, 0)
		self.np.write()
