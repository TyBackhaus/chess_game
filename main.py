import os 
import sys 
import pygame
#user interface 
import pygame as p
from chess import chessengine

WIDTH = HIGHT =512 
dimension = 8 # 8x8 board 
sq_size = HIGHT // dimension
MAX_FPS =15 # for animations
IMAGES={}

"""
load immages = global dictionary runes once in main
"""
def Load_Images():
  pieces= ["wp","wR","wN","wB","wQ","wK","bp","bR","bN","bB","bQ","bK",]
  for piece in pieces:
    IMAGES[piece]= p.transform.scale(p.image.load("images/"+ piece+ ".png"), (sq_size,sq_size))
    # can acess images by saying images["wp"]
# main driver .and handle input and graphics 
def main():
  p.int()
  screen = p.display.set_mode((WIDTH,HIGHT))
  clock = p.time.Clock()
  screen.fill(p.color("white"))
  gs = chessengine.GameState()
  Load_Images() # do before while lo op 
  running = True 
  while running:
    for i in p.event.get():
      if e.type == p.QUIT:
        running = False
    drawGameState(screen,gs)    
    clock.tick(MAX_FPS)
    p.display.flip()
def drawGameState(screen,gs):
  drawbard(screen)# draws squares 
  drawpeices(screen.gs)# draws peices on top of square 
def drawborad(screen):
  colors = [p.color("white"), p.color("grey")]
  for r in range(dimension):
    for c in range(dimension):
      ((r+c)%2)
# draw peices using current game state 
def drawpeices(screen):
  
  main()
  