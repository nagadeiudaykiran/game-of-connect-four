Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
impo
rt pygame
SyntaxError: invalid syntax
import pygame
pygame 2.1.2 (SDL 2.0.18, Python 3.10.1)
Hello from the pygame community. https://www.pygame.org/contribute.html
import sys
import math
BLUE = (0,0,225)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ROW_COUNT = 6
COLUMN_COUNT = 7
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]=piece

    
def is_valid_location(board,col):
    return board[ROW_COUNT-1][COL]==0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r

        
def print_board(board):
    print(np.flip(board,0))

    
def winning_move(board,piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board [r][c+2]==piece and board[r][c+3]==piece:
                return True

            
for c in range(COLUMN_COUNT-3)
SyntaxError: expected ':'
def winning_move(board,piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board [r][c+2]==piece and board[r][c+3]==piece:
                return True
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT-3):
                    if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board [r+3][c]==piece:
                        return True
                    for c in range(COLUMN_COUNT-3):
                        for  r in range(3,ROW_COUNT):
                            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                                return True

                            
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_count):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
            dor c in range(COLUMN_COUNT):
                
SyntaxError: invalid syntax
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_count):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    if board[r][c]==1:
                        pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        elif board[r][c] ==2
                        
SyntaxError: invalid syntax
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_count):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    if board[r][c]==1:
                        pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                    elif board[r][c] ==2
                    
SyntaxError: expected ':'
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_count):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    if board[r][c]==1:
                        pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                    elif board[r][c] ==2:
                        pygame.draw.circle(screen,YELLOW,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        pygame.display.update()

                        
board = create_board()
print_board(board)
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]
game_over=False
trun=0
pygame.init()
(5, 0)
SQUARESIZE=100
width = COLUMN_COUNT*SQUARESIZE
height=(ROW_COUNT+1)*SQUARESIZE
size = (width,height)
RADIUS=int(SQUARESIZE/2-5)
screen= pygame.display.set_mode(size)
draw_board(board)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    draw_board(board)
  File "<pyshell#62>", line 3, in draw_board
    for r in range(ROW_count):
NameError: name 'ROW_count' is not defined. Did you mean: 'ROW_COUNT'?
draw_board(board)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    draw_board(board)
  File "<pyshell#62>", line 3, in draw_board
    for r in range(ROW_count):
NameError: name 'ROW_count' is not defined. Did you mean: 'ROW_COUNT'?
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    if board[r][c]==1:
                        pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                    elif board[r][c] ==2:
                        pygame.draw.circle(screen,YELLOW,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                        pygame.display.update()

                        
board = create_board()
print_board(board)
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]
game_over=False
trun=0
pygame.init()
(5, 0)
SQUARESIZE=100
width = COLUMN_COUNT*SQUARESIZE
height=(ROW_COUNT+1)*SQUARESIZE
size = (width,height)
RADIUS=int(SQUARESIZE/2-5)
screen= pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont=pygame.font.sysFONT("MONOSPACE",75)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    myfont=pygame.font.sysFONT("MONOSPACE",75)
AttributeError: module 'pygame.font' has no attribute 'sysFONT'. Did you mean: 'SysFont'?
myfont=pygame.font.SysFont("MONOSPACE",75)
while nor=t game_over:
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                posx=event.ost[0]
                if turn ==0:
                    pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(squaresize/2)),RADIUS)
                    pugame.display.update()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                        if turn==0:
                            posx = event.post[0]
                            col=int(math.floor(posx/SQUARESIZE))
                            if is _valid_location(board,col):
                                
SyntaxError: invalid syntax
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                posx=event.ost[0]
                if turn ==0:
                    pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(squaresize/2)),RADIUS)
                    pugame.display.update()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                        if turn==0:
                            posx = event.post[0]
                            col=int(math.floor(posx/SQUARESIZE))
                            if is_valid_location(board,col):
                                row=get_next_open_row(board,col)
                                drop_piece(board,row,col,1)
                                if winning_move(board,1)
                                
SyntaxError: expected ':'
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                posx=event.ost[0]
                if turn ==0:
                    pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(squaresize/2)),RADIUS)
                    pugame.display.update()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                        if turn==0:
                            posx = event.post[0]
                            col=int(math.floor(posx/SQUARESIZE))
                            if is_valid_location(board,col):
                                row=get_next_open_row(board,col)
                                drop_piece(board,row,col,1)
                                if winning_move(board,1):
                                    label=myfont.render("player 1 wins!",1,RED)
                                    screen.blit(label,(40,10))
                                    game_over=True
                 else:
                     
SyntaxError: unindent does not match any outer indentation level
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                posx=event.ost[0]
                if turn ==0:
                    pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(squaresize/2)),RADIUS)
                    pugame.display.update()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                        if turn==0:
                            posx = event.post[0]
                            col=int(math.floor(posx/SQUARESIZE))
                            if is_valid_location(board,col):
                                row=get_next_open_row(board,col)
                                drop_piece(board,row,col,1)
                                if winning_move(board,1):
                                    label=myfont.render("player 1 wins!",1,RED)
                                    screen.blit(label,(40,10))
                                    game_over=True
                                    else:
                                        
SyntaxError: invalid syntax
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                posx=event.ost[0]
                if turn ==0:
                    pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(squaresize/2)),RADIUS)
                    pugame.display.update()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                        if turn==0:
                            posx = event.post[0]
                            col=int(math.floor(posx/SQUARESIZE))
                            if is_valid_location(board,col):
                                row=get_next_open_row(board,col)
                                drop_piece(board,row,col,1)
                                if winning_move(board,1):
                                    label=myfont.render("player 1 wins!",1,RED)
                                    screen.blit(label,(40,10))
                                    game_over=True
                                else:
                                    posx=event.pos[0]
                                    col=int(math.floor(posx/SQUARESIZE))
                                    if is_valid_location(board,col):
                                        row=get_next_open_row(board,col)
                                        drop_piece(board,row,col,2)
                                        if winning_move(board,2):
                                            label=myfont.render("player 2 wins!",1,YELLOW)
                                            screen.blit(label,(40,10))
                                            game_over=True
                                            print_board(board)
                                            draw_board(board)
                                            trun+=1
                                            trun=trun%2
                                            if game_over:
                                                pygame.time.wait(3000)
                                                