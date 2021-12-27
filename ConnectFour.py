import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7



def create_game_game_board():
    game_board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return game_board


def drop_peice(game_board, row, col, player_piece):
    game_board[row][col] = player_piece


def is_valid_location(game_board, col):
    return game_board[ROW_COUNT-1][col]==0


def get_next_open_row(game_board, col):
    for r in range(ROW_COUNT):
        if game_board[r][col] == 0:
            return r


def print_game_board(game_board):
    print(np.flip(game_board, 0))

## Basic method for checking each win condition. 
def winning_move(game_board, player_piece):

    ##cheking horizontal win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if game_board[r][c] == player_piece and game_board[r][c+1] == player_piece and game_board[r][c+2] == player_piece and game_board[r][c+3] == player_piece:
                return True
            
    ##cheking vertical win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if game_board[r][c] == player_piece and game_board[r+1][c] == player_piece and game_board[r+2][c] == player_piece and game_board[r+3][c] == player_piece:
                return True
            
    ##cheking up diagonal win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if game_board[r][c] == player_piece and game_board[r+1][c+1] == player_piece and game_board[r+2][c+2] == player_piece and game_board[r+3][c+3] == player_piece:
                return True
            
    ##cheking down diagonal win 
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if game_board[r][c] == player_piece and game_board[r-1][c+1] == player_piece and game_board[r-2][c+2] == player_piece and game_board[r-3][c+3] == player_piece:
                return True

## sets up the game with a new game board 
def draw_game_board(game_board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if game_board[r][c]==1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif game_board[r][c]==2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()



game_board = create_game_game_board()
game_over = False
## used to keep track of whose turn it is. 0 == player 1; 1 == player 2
turn = 0

##pygame variables for board
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2-8)


screen = pygame.display.set_mode(size)
draw_game_board(game_board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)


## game play
while not game_over:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                
                if is_valid_location(game_board, col):
                    row = get_next_open_row(game_board, col)
                    drop_peice(game_board, row, col, 1)
                    
                    ## checking for connect four - player 1
                    if winning_move(game_board, 1):
                        label = myfont.render("Player 1 Wins!!", True, BLACK, RED)
                        screen.blit(label, (10,10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(game_board, col):
                    row = get_next_open_row(game_board, col)
                    drop_peice(game_board, row, col, 2)
                    
                    ## checking for connect four - player 2
                    if winning_move(game_board, 2):
                        label = myfont.render("Player 2 Wins!!", True, BLACK, YELLOW)
                        screen.blit(label, (10,10))
                        game_over = True

            draw_game_board(game_board)

            turn +=1
            turn = turn % 2
    
        
            if game_over:
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()
