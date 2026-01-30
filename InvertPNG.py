import tkinter as tk
from tkinter import filedialog
import imageio.v3 as iio
import matplotlib.pyplot as plt
import pygame
import pygame.draw

#path = filedialog.askopenfilename(initialdir=r"C:\Users\Nihil\Source\Repos\InvertPNG\Input")
path = r"C:\Users\Nihil\Source\Repos\InvertPNG\Input\Obsidian_furniture_set_house.png"
img = iio.imread(path)
pygame.init()
sx, sy, skl = len(img[0]), len(img), 4
screen = pygame.display.set_mode((sx*skl, sy*skl))

for x in range(sx):
	for y in range(sy):
		clr = img[y][x]
		if skl == 1:
			screen.set_at((x, y), clr)
		else:
			pygame.draw.rect(screen, clr, (x*skl, y*skl, 4, 4))
pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			running = False


pygame.quit()
print("Done")
...
