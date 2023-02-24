
import pygame as p
from chess import chessengine

WIDTH = HIGHT =512 
dimension = 8 # 8x8 board 
SQ_SIZE = HIGHT // dimension
MAX_FPS =15 # for animations
IMAGES={}

"""
load immages = global dictionary runes once in main
"""
def LoadImages():
  pieces= ["wp","wR","wN","wB","wQ","wK","bp","bR","bN","bB","bQ","bK",]
  for piece in pieces:
    IMAGES[piece]= p.transform.scale(p.image.load("images/"+ piece + ".png"), (SQ_SIZE,SQ_SIZE))
    # can acess images by saying images["wp"]
# main driver .and handle input and graphics 
def main():
  p.init()
  screen = p.display.set_mode((WIDTH,HIGHT))
  clock = p.time.Clock()
  screen.fill(p.Color("white"))
  gs = chessengine.GameState()
  LoadImages() # do before while lo op 
  running = True 
  while running:
    for i in p.event.get():
      if e.type == p.QUIT:
        running = False
    drawGameState(screen,gs)    
    clock.tick(MAX_FPS)
    p.display.flip()
#graphics
def drawGameState(screen,gs):
  drawBoard(screen)# draws squares 
  drawPeices(screen,gs.board)# draws peices on top of square 
#draws sqares on bard 
def drawBoard(screen):
  colors = [p.color("white"), p.color("grey")]
  for r in range(dimension):
    for c in range(dimension):
      color = colors [((r+c)%2)]
      p.draw.rect(screen,color,p.React(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE)) 
# draw peices using current game state 
def drawPeices(screen,board):
  pass  
#if _name_ == "_main_":
main()
drawBoard(screen)