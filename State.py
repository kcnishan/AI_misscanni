_author__="Nishan and Rishika"


from anytree import *
import pygame
from pygame.locals import *

#background
window = 750, 580
background_image = pygame.image.load('River.jpg')
background_image = pygame.transform.scale(background_image, window)
screen = pygame.display.set_mode(window, HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption("Missionaries and Cannibals Problem")

#images
missi = pygame.image.load('ram.png')
missi = pygame.transform.scale(missi, (70, 90))
canni = pygame.image.load('ravan.png')
canni = pygame.transform.scale(canni, (100, 120))
carrier = pygame.image.load('turtle.png')
carrier = pygame.transform.scale(carrier, (140, 100))

class State():
	def __init__(self, left_canni, left_missi, turtle, right_canni, right_missi):
		self.left_canni = left_canni
		self.left_missi = left_missi
		self.turtle = turtle
		self.right_canni = right_canni
		self.right_missi = right_missi
		self.parent = None
		self.child=[]

	def final(self):
		if self.left_canni == 0 and self.left_missi == 0:
			return True
		else:
			return False

	def valid(self):
		if self.left_missi >= 0 and self.right_missi >= 0 \
                   and self.left_canni >= 0 and self.right_canni >= 0 \
                   and (self.left_missi == 0 or self.left_missi >= self.left_canni) \
                   and (self.right_missi == 0 or self.right_missi >= self.right_canni):
			return True
		else:
			return False

#function for generating child state

def childstate(current_state):
	child = [];

	if current_state.turtle == 'left':
		## Two missionaries crossing from left to right.
		new_state = State(current_state.left_canni, current_state.left_missi - 2, 'right',
                                  current_state.right_canni, current_state.right_missi + 2)

		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## Two cannibals crossing from left to right.
		new_state = State(current_state.left_canni - 2, current_state.left_missi, 'right',
                                  current_state.right_canni + 2, current_state.right_missi)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## One missionary and one cannibal crossing from left to right.
		new_state = State(current_state.left_canni - 1, current_state.left_missi - 1, 'right',
                                  current_state.right_canni + 1, current_state.right_missi + 1)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## One missionary crossing from left to right.
		new_state = State(current_state.left_canni, current_state.left_missi - 1, 'right',
                                  current_state.right_canni, current_state.right_missi + 1)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## One cannibal crossing from left to right.
		new_state = State(current_state.left_canni - 1, current_state.left_missi, 'right',
                                  current_state.right_canni + 1, current_state.right_missi)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)
	else:
		## Two missionaries crossing from right to left.
		new_state = State(current_state.left_canni, current_state.left_missi + 2, 'left',
                                  current_state.right_canni, current_state.right_missi - 2)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## Two cannibals crossing from right to left.
		new_state = State(current_state.left_canni + 2, current_state.left_missi, 'left',
                                  current_state.right_canni - 2, current_state.right_missi)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## One missionary and one cannibal crossing from right to left.
		new_state = State(current_state.left_canni + 1, current_state.left_missi + 1, 'left',
                                  current_state.right_canni - 1, current_state.right_missi - 1)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## One missionary crossing from right to left.
		new_state = State(current_state.left_canni, current_state.left_missi + 1, 'left',
                                  current_state.right_canni, current_state.right_missi - 1)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

		## One cannibal crossing from right to left.
		new_state = State(current_state.left_canni + 1, current_state.left_missi, 'left',
                                  current_state.right_canni - 1, current_state.right_missi)
		if new_state.valid():
			new_state.parent = current_state
			current_state.child.append(new_state)
			child.append(new_state)

	return child