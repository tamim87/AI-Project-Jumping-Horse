import pygame
import sys
import numpy as np

# initialize pygame
pygame.init()


# CONSTANTS
WIDTH = 800
HEIGHT = WIDTH
LINE_WIDTH = 10
BOARD_ROWS = 5
BOARD_COLS = BOARD_ROWS
SQUARE_SIZE = WIDTH/BOARD_ROWS
SCORE_AREA_HEIGHT = 100

# # Colors
BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (128, 128, 128)
WHITE = (238,238,210)
GRAY = (118,150,86)
# # WHITE = "#e2e2e2"
# # GRAY = "#00695C"

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_COLOR = (199, 168, 97)
# BG_COLOR = "#a39489"

LINE_COLOR = (82, 68, 38)
# WHITE = (239, 231, 200)

AI=1
HU=1



WHITE_HORSE = pygame.image.load(r"white_horse.png")
WHITE_HORSE = pygame.transform.scale(WHITE_HORSE, (150,150))

BLACK_HORSE = pygame.image.load(r"black_horse.png")
BLACK_HORSE = pygame.transform.scale(BLACK_HORSE, (150,150))

GRAY_HORSE = pygame.image.load(r"cross.png")
GRAY_HORSE = pygame.transform.scale(GRAY_HORSE, (160,160))

GAME_OVER = pygame.image.load(r"green_horse.png")
GAME_OVER = pygame.transform.scale(GAME_OVER, (160,160))

RED_HORSE = pygame.image.load(r"red_horse.png")
RED_HORSE = pygame.transform.scale(RED_HORSE, (160,160))

LOSE = pygame.image.load(r"lose.png")
LOSE = pygame.transform.scale(LOSE, (160,120))

WIN = pygame.image.load(r"win.png")
WIN = pygame.transform.scale(WIN, (160,120))


# VARIABLES
player = 1
game_over = False
losePlayer = 0


# SCREEN
screen = pygame.display.set_mode( (WIDTH, HEIGHT + SCORE_AREA_HEIGHT) )
pygame.display.set_caption( 'Horse Jump' )
# screen.fill( BG_COLOR )


# CONSOLE BOARD
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )


# Player Current Possition
playerOneCurrentRow = -1
playerOneCurrentCol = -1
playerTwoCurrentRow = -1
playerTwoCurrentCol = -1


# Draw the chessboard
def draw_chessboard():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_ROWS):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_score_area():
    pygame.draw.rect(screen, WHITE, (0, HEIGHT, WIDTH, SCORE_AREA_HEIGHT))

# FUNCTIONS
# def draw_lines():

#     for i in range(1,BOARD_ROWS):
#         # horizontal
#         pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE*i), (WIDTH, SQUARE_SIZE*i), LINE_WIDTH )

#     for i in range(1,BOARD_COLS):
#         # vertical
#         pygame.draw.line( screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH )


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                if (row == playerOneCurrentRow and col == playerOneCurrentCol and losePlayer == 1 ):    #player1 lost UI
                    screen.blit(RED_HORSE, (int( col * SQUARE_SIZE ), int( row * SQUARE_SIZE )))
                    screen.blit(GAME_OVER, (320,320))
                    screen.blit(LOSE, (320,480))
                elif (row == playerOneCurrentRow and col == playerOneCurrentCol):
                    screen.blit(BLACK_HORSE, (int( col * SQUARE_SIZE ), int( row * SQUARE_SIZE )))
                else:
                    screen.blit(GRAY_HORSE, (int( col * SQUARE_SIZE ), int( row * SQUARE_SIZE )))
            elif board[row][col] == 2:
                if (row == playerTwoCurrentRow and col == playerTwoCurrentCol and losePlayer == 2 ):    #player2 lost UI
                    screen.blit(RED_HORSE, (int( col * SQUARE_SIZE ), int( row * SQUARE_SIZE )))
                    screen.blit(GAME_OVER, (320,320))
                    screen.blit(WIN, (320,480))
                elif (row == playerTwoCurrentRow and col == playerTwoCurrentCol):
                    screen.blit(WHITE_HORSE, (int( col * SQUARE_SIZE ), int( row * SQUARE_SIZE )))
                else:
                    screen.blit(GRAY_HORSE, (int( col * SQUARE_SIZE ), int( row * SQUARE_SIZE )))
    pygame.display.update()


def mark_square(row, col, player):
    board[row][col] = player
    print ("----------------------------------------------------")
    print("Player " + str(player) + " marked square : (" + str(row) + "," + str(col) + ")")
    print(board)
    print ("----------------------------------------------------")


def available_square(row, col, player):
    if(player == 1): 
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
        sp_move=HU
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol
        sp_move=AI

    return (board[row][col] == 0 and ( 
        (currentRow == -1 and currentCol==-1) or
        (currentRow-2 == row and currentCol-1 == col) or
        (currentRow-2 == row and currentCol+1 == col) or
        (currentRow-1 == row and currentCol-2 == col) or
        (currentRow-1 == row and currentCol+2 == col) or
        (currentRow+1 == row and currentCol-2 == col) or
        (currentRow+1 == row and currentCol+2 == col) or
        (currentRow+2 == row and currentCol-1 == col) or
        (currentRow+2 == row and currentCol+1 == col) or

        (currentRow-1 == row and currentCol-1 == col and sp_move>0) or
        (currentRow-1 == row and currentCol+1 == col and sp_move>0) or
        (currentRow+1 == row and currentCol-1 == col and sp_move>0) or
        (currentRow+1 == row and currentCol+1 == col and sp_move>0)
    ))				

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True

def check_lose(player):
    global HU
    global AI
    if(player == 1):
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
        sp_move=HU
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol
        sp_move=AI


    if(currentRow == -1 or currentCol == -1):
        return False

    return not (
        (-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-2][currentCol-1] == 0 ) or
        (-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-2][currentCol+1] == 0 ) or
        (-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow-1][currentCol-2] == 0 ) or
        (-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow-1][currentCol+2] == 0 ) or
        (-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow+1][currentCol-2] == 0 ) or
        (-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow+1][currentCol+2] == 0 ) or
        (-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+2][currentCol-1] == 0 ) or
        (-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+2][currentCol+1] == 0 ) or

        (-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 and sp_move>0) or
        (-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 and sp_move>0) or
        (-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 and sp_move>0) or
        (-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 and sp_move>0) 
    )

def check_special(row ,col,player):
    global HU
    global AI
    if(player == 1):
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol

    if((currentRow-1 == row and currentCol-1 == col) or
        (currentRow-1 == row and currentCol+1 == col) or
        (currentRow+1 == row and currentCol-1 == col) or
        (currentRow+1 == row and currentCol+1 == col)):
        if player==1:
            HU=HU-1
        else:
            AI=AI-1







def restart():
    # screen.fill( BG_COLOR )
    draw_chessboard()
    global AI
    global HU
    AI=1
    HU=1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0



def bestMove(player = 2):
    bestScore = -100000
    move = None

    global playerTwoCurrentCol
    global playerTwoCurrentRow

    global AI
    global HU
    move=(-1,-1)

    #never used for player
    if(player == 1):
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
        sp_move=HU
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol
        sp_move=AI

    if(currentRow == -1 or currentCol == -1):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if(board[row][col] == 0):
                    board[row][col] = 2
                    score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,row,col,0,False)
                    board[row][col] = 0

                    if(score>bestScore):
                        bestScore = score
                        move = (row,col)

    if(-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-2][currentCol-1] == 0 ):
        board[currentRow-2][currentCol-1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-2 , currentCol-1,0,False)
        board[currentRow-2][currentCol-1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow-2 , currentCol-1)

    if(-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-2][currentCol+1] == 0 ):
        board[currentRow-2][currentCol+1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-2,currentCol+1,0,False)
        board[currentRow-2][currentCol+1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow-2,currentCol+1)

    if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow-1][currentCol-2] == 0 ):
        board[currentRow-1][currentCol-2] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol-2,0,False)
        board[currentRow-1][currentCol-2] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow-1,currentCol-2)

    if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow-1][currentCol+2] == 0 ):
        board[currentRow-1][currentCol+2] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+2,0,False)
        board[currentRow-1][currentCol+2] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow-1,currentCol+2)

    if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow+1][currentCol-2] == 0 ):
        board[currentRow+1][currentCol-2] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-2,0,False)
        board[currentRow+1][currentCol-2] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow+1,currentCol-2)

    if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow+1][currentCol+2] == 0 ):
        board[currentRow+1][currentCol+2] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+2,0,False)
        board[currentRow+1][currentCol+2] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow+1,currentCol+2)

    if(-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+2][currentCol-1] == 0 ):
        board[currentRow+2][currentCol-1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+2,currentCol-1,0,False)
        board[currentRow+2][currentCol-1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow+2,currentCol-1)

    if(-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+2][currentCol+1] == 0 ):
        board[currentRow+2][currentCol+1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+2,currentCol+1,0,False)
        board[currentRow+2][currentCol+1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow+2,currentCol+1)

    if(move!=(-1,-1)):
        playerTwoCurrentRow = move[0]
        playerTwoCurrentCol = move[1]
        mark_square( move[0], move[1], 2)
    else:
        if(sp_move>0):
            if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ):
                board[currentRow-1][currentCol-1] = 2 
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1 , currentCol-1,0,False)
                board[currentRow-1][currentCol-1] = 0
                AI=AI+1
                if(score>bestScore):
                    bestScore = score
                    move = (currentRow-1 , currentCol-1)

            if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ):
                board[currentRow-1][currentCol+1] = 2
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+1,0,False)
                board[currentRow-1][currentCol+1] = 0
                AI=AI+1
                if(score>bestScore):
                    bestScore = score
                    move = (currentRow-1,currentCol+1)

            if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ):
                board[currentRow+1][currentCol-1] = 2
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-1,0,False)
                board[currentRow+1][currentCol-1] = 0
                AI=AI+1
                if(score>bestScore):
                    bestScore = score
                    move = (currentRow+1,currentCol-1)

            if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ):
                    board[currentRow+1][currentCol+1] = 2
                    AI=AI-1
                    score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+1,0,False)
                    board[currentRow+1][currentCol+1] = 0
                    AI=AI+1
                    if(score>bestScore):
                        bestScore = score
                        move = (currentRow+1,currentCol+1)
            if(move!=(-1,-1)):
                playerTwoCurrentRow = move[0]
                playerTwoCurrentCol = move[1]
                mark_square( move[0], move[1], 2)
                AI=AI-1
            
  
        


     


    
scores = {
  1: 10,
  2: -10,
  0: 0
}

# depth not use because the depth is not const value and it change when any player make his move and the  depth in the code handled by
# check_lose(player)
def minimax(board, player, playerOneCurrentRow, playerOneCurrentCol, playerTwoCurrentRow, playerTwoCurrentCol , depth, isMaximizing):
    # check if there is any move available for player (1 or 2)
    # if check_lose(player)==true(no available move) result = player return 10/-10;
    # if check_lose(player)==false result = 0  return 0;
    result = player if check_lose(player) else 0
    if result is not None:
        return scores[result]


    if(player == 1):
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol
    #if ture maximize the player 2 score
    if isMaximizing:
        #any arbitrary small value 
        bestScore = -100000


        if(-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-2][currentCol-1] == 0 ):
            board[currentRow-2][currentCol-1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-2 , currentCol-1,0,False)
            board[currentRow-2][currentCol-1] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-2][currentCol+1] == 0 ):
            board[currentRow-2][currentCol+1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-2,currentCol+1,0,False)
            board[currentRow-2][currentCol+1] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow-1][currentCol-2] == 0 ):
            board[currentRow-1][currentCol-2] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol-2,0,False)
            board[currentRow-1][currentCol-2] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow-1][currentCol+2] == 0 ):
            board[currentRow-1][currentCol+2] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+2,0,False)
            board[currentRow-1][currentCol+2] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow+1][currentCol-2] == 0 ):
            board[currentRow+1][currentCol-2] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-2,0,False)
            board[currentRow+1][currentCol-2] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow+1][currentCol+2] == 0 ):
            board[currentRow+1][currentCol+2] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+2,0,False)
            board[currentRow+1][currentCol+2] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+2][currentCol-1] == 0 ):
            board[currentRow+2][currentCol-1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+2,currentCol-1,0,False)
            board[currentRow+2][currentCol-1] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+2][currentCol+1] == 0 ):
            board[currentRow+2][currentCol+1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+2,currentCol+1,0,False)
            board[currentRow+2][currentCol+1] = 0

            bestScore = max(score,bestScore)
        
        if bestScore ==-100000 and AI>0:
            if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ):
                board[currentRow-1][currentCol-1] = 2
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1 , currentCol-1, 0,False)
                board[currentRow-1][currentCol-1] = 0
                AI=AI+1

                bestScore = max(score,bestScore)

            if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ):
                board[currentRow-1][currentCol+1] = 2
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+1,0,False)
                board[currentRow-1][currentCol+1] = 0
                AI=AI+1
                bestScore = max(score,bestScore)

            if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ):
                board[currentRow+1][currentCol-1] = 2
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-1,0,False)
                board[currentRow+1][currentCol-1] = 0
                AI=AI+1
                bestScore = max(score,bestScore)

            if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ):
                board[currentRow+1][currentCol+1] = 2
                AI=AI-1
                score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+1,0,False)
                board[currentRow+1][currentCol+1] = 0
                AI=AI+1

                bestScore = max(score,bestScore)
            
        
        print("BEST SCORE MAX = ",bestScore)
        return bestScore

    else:
        bestScore = 100000

        if(-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-2][currentCol-1] == 0 ):
            board[currentRow-2][currentCol-1] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-2 , currentCol-1,0,True)
            board[currentRow-2][currentCol-1] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow-2 and currentRow-2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-2][currentCol+1] == 0 ):
            board[currentRow-2][currentCol+1] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-2,currentCol+1,0,True)
            board[currentRow-2][currentCol+1] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow-1][currentCol-2] == 0 ):
            board[currentRow-1][currentCol-2] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol-2,0,True)
            board[currentRow-1][currentCol-2] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow-1][currentCol+2] == 0 ):
            board[currentRow-1][currentCol+2] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+2,0,True)
            board[currentRow-1][currentCol+2] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-2 and currentCol-2 < BOARD_COLS and board[currentRow+1][currentCol-2] == 0 ):
            board[currentRow+1][currentCol-2] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-2,0,True)
            board[currentRow+1][currentCol-2] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+2 and currentCol+2 < BOARD_COLS and board[currentRow+1][currentCol+2] == 0 ):
            board[currentRow+1][currentCol+2] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+2,0,True)
            board[currentRow+1][currentCol+2] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+2][currentCol-1] == 0 ):
            board[currentRow+2][currentCol-1] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+2,currentCol-1,0,True)
            board[currentRow+2][currentCol-1] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow+2 and currentRow+2 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+2][currentCol+1] == 0 ):
            board[currentRow+2][currentCol+1] = 1
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+2,currentCol+1,0,True)
            board[currentRow+2][currentCol+1] = 0

            bestScore = min(score,bestScore)
        
        if bestScore == 100000 and HU>0:
            if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ):
                board[currentRow-1][currentCol-1] = 2
                HU=HU-1
                score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-1 , currentCol-1,0,True)
                board[currentRow-1][currentCol-1] = 0
                HU=HU+1
                bestScore = min(score,bestScore)

            if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ):
                board[currentRow-1][currentCol+1] = 2
                HU=HU-1
                score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+1,0,True)
                board[currentRow-1][currentCol+1] = 0
                HU=HU+1

                bestScore = min(score,bestScore)

            if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ):
                board[currentRow+1][currentCol-1] = 2
                HU=HU-1
                score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-1,0,True)
                board[currentRow+1][currentCol-1] = 0
                HU=HU+1

                bestScore = min(score,bestScore)

            if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ):
                board[currentRow+1][currentCol+1] = 2
                HU=HU-1
                score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+1,0,True)
                board[currentRow+1][currentCol+1] = 0
                HU=HU+1
                bestScore = min(score,bestScore)

            


        print("BEST SCORE MIN= ",bestScore)
        return bestScore



# Get the cell indices based on mouse position
def get_cell_indices(mouse_pos):
    x, y = mouse_pos
    row = y // SQUARE_SIZE  
    col = x // SQUARE_SIZE
    return row, col

clock = pygame.time.Clock()

# draw_lines()

font = pygame.font.Font(None, 36)
# screen.fill( BG_COLOR )
# draw_lines()
draw_chessboard()
draw_score_area()

# MAINLOOP---------
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # if event.type == pygame.MOUSEMOTION:
        #     # mouse_pos = pygame.mouse.get_pos()
        #     mouse_pos = event.pos
        #     if HEIGHT > mouse_pos[1] >= 0:
        #         row, col = get_cell_indices(mouse_pos)
        #         x = col * SQUARE_SIZE
        #         y = row * SQUARE_SIZE
        #         # if (row + col) % 2 == 0:
        #             # pygame.draw.rect(screen, YELLOW, (x, y, SQUARE_SIZE, SQUARE_SIZE))
        #         # else:
        #         pygame.draw.rect(screen, GREEN, (x, y, SQUARE_SIZE, SQUARE_SIZE))



        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            #print('Mouse X position: ' + str(mouseX))
            #print('Mouse Y position: ' + str(mouseY))
            print('Clicked row: ' + str(clicked_row))
            print('Clicked col: ' + str(clicked_col))

            if available_square( clicked_row, clicked_col, 1 ):
                player = 1
                check_special(clicked_row,clicked_col,player)
                mark_square( clicked_row, clicked_col, player )

                playerOneCurrentRow = clicked_row
                playerOneCurrentCol = clicked_col
                print('Player One Current Row and Col: (',str(playerOneCurrentRow)+','+str(playerOneCurrentCol)+')')


                if check_lose( 2 ):
                    losePlayer = 2
                    game_over = True
                    draw_figures()

                else:
                    player = 2
                    bestMove(player)

                    if check_lose( 1 ):
                        losePlayer = 1
                        game_over = True
                        print("********************************************************")
                        print("Player 1 lost.\nRestarting game : Press -> R")
                        print("Quit game : Press -> Q")
                        print("********************************************************")
                    
                    draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
                losePlayer = 0
                playerOneCurrentRow = -1
                playerOneCurrentCol = -1
                playerTwoCurrentRow = -1
                playerTwoCurrentCol = -1
            
            elif event.key == pygame.K_q:
                pygame.display.quit()
                sys.exit()  
        

    


    # # Handle cell hover
    # mouse_pos = pygame.mouse.get_pos()
    # if HEIGHT > mouse_pos[1] >= 0:
    #     row, col = get_cell_indices(mouse_pos)
    #     x = col * SQUARE_SIZE
    #     y = row * SQUARE_SIZE
    #     # if (row + col) % 2 == 0:
    #         # pygame.draw.rect(screen, YELLOW, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    #     # else:
    #     pygame.draw.rect(screen, GREEN, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    
    pygame.display.update()
    # clock.tick(50)    
