import pygame
import sys
import numpy as np

# initialize pygame
pygame.init()


# CONSTANTS
WIDTH = 800
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 5
BOARD_COLS = BOARD_ROWS
SQUARE_SIZE = WIDTH/BOARD_ROWS

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_COLOR = (199, 168, 97)
LINE_COLOR = (82, 68, 38)
WHITE = (239, 231, 200)



# # WHITE_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/white_horse.png")
# WHITE_HORSE = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\white_horse.png")
# WHITE_HORSE = pygame.transform.scale(WHITE_HORSE, (150,150))

# # BLACK_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/black_horse.png")
# BLACK_HORSE = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\black_horse.png")
# BLACK_HORSE = pygame.transform.scale(BLACK_HORSE, (150,150))

# # GRAY_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/gray_horse.png")
# GRAY_HORSE = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\gray_horse.png")
# GRAY_HORSE = pygame.transform.scale(GRAY_HORSE, (155,155))

# # GAME_OVER = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/green_horse.png")
# GAME_OVER = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\green_horse.png")
# GAME_OVER = pygame.transform.scale(GAME_OVER, (160,160))

# # RED_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/red_horse.png")
# RED_HORSE = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\red_horse.png")
# RED_HORSE = pygame.transform.scale(RED_HORSE, (160,160))

# # LOSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/lose.png")
# LOSE = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\lose.png")
# LOSE = pygame.transform.scale(LOSE, (160,120))

# # WIN = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/win.png")
# WIN = pygame.image.load(r"C:\Users\User\Documents\Ai-Isolation-Game-main\Isolation Game\win.png")
# WIN = pygame.transform.scale(WIN, (160,120))


WHITE_HORSE = pygame.image.load(r"white_horse.png")


# WHITE_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/white_horse.png")
# WHITE_HORSE = pygame.image.load(r"Isolation Game\white_horse.png")
WHITE_HORSE = pygame.transform.scale(WHITE_HORSE, (150,150))

# BLACK_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/black_horse.png")
BLACK_HORSE = pygame.image.load(r"C:\Users\mizan\Downloads\Telegram Desktop\Ai-Isolation-Game-main\Ai-Isolation-Game-main\Isolation Game\black_horse.png")
BLACK_HORSE = pygame.transform.scale(BLACK_HORSE, (150,150))

# GRAY_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/gray_horse.png")
GRAY_HORSE = pygame.image.load(r"gray_horse.png")
GRAY_HORSE = pygame.transform.scale(GRAY_HORSE, (155,155))

# GAME_OVER = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/green_horse.png")
GAME_OVER = pygame.image.load(r"green_horse.png")
GAME_OVER = pygame.transform.scale(GAME_OVER, (160,160))

# RED_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/red_horse.png")
RED_HORSE = pygame.image.load(r"red_horse.png")
RED_HORSE = pygame.transform.scale(RED_HORSE, (160,160))

# LOSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/lose.png")
LOSE = pygame.image.load(r"lose.png")
LOSE = pygame.transform.scale(LOSE, (160,120))

# WIN = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/win.png")
WIN = pygame.image.load(r"win.png")
WIN = pygame.transform.scale(WIN, (160,120))




# # WHITE_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/white_horse.png")
# WHITE_HORSE = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\\Isolation Game\\white_horse.png")
# WHITE_HORSE = pygame.transform.scale(WHITE_HORSE, (150,150))

# # BLACK_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/black_horse.png")
# BLACK_HORSE = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\Isolation Game\\black_horse.png")
# BLACK_HORSE = pygame.transform.scale(BLACK_HORSE, (150,150))

# # GRAY_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/gray_horse.png")
# GRAY_HORSE = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\\Isolation Game\\gray_horse.png")
# GRAY_HORSE = pygame.transform.scale(GRAY_HORSE, (155,155))

# # GAME_OVER = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/green_horse.png")
# GAME_OVER = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\\Isolation Game\\green_horse.png")
# GAME_OVER = pygame.transform.scale(GAME_OVER, (160,160))

# # RED_HORSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/red_horse.png")
# RED_HORSE = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\\Isolation Game\\red_horse.png")
# RED_HORSE = pygame.transform.scale(RED_HORSE, (160,160))

# # LOSE = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/lose.png")
# LOSE = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\\Isolation Game\\lose.png")
# LOSE = pygame.transform.scale(LOSE, (160,120))

# # WIN = pygame.image.load("/home/samin/Desktop/study/4.1/Isolation/win.png")
# WIN = pygame.image.load("C:\\Users\\User\\Documents\\Ai-Isolation-Game-main\\Isolation Game\\win.png")
# WIN = pygame.transform.scale(WIN, (160,120))








# VARIABLES
player = 1
game_over = False
losePlayer = 0


# SCREEN
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Horse Jump' )
screen.fill( BG_COLOR )


# CONSOLE BOARD
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )



# Player Current Possition
playerOneCurrentRow = -1
playerOneCurrentCol = -1
playerTwoCurrentRow = -1
playerTwoCurrentCol = -1


# FUNCTIONS
def draw_lines():

    for i in range(1,BOARD_ROWS):
        # horizontal
        pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE*i), (WIDTH, SQUARE_SIZE*i), LINE_WIDTH )

    for i in range(1,BOARD_COLS):
        # vertical
        pygame.draw.line( screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH )


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
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol
    #check my current movie is empty and is valid directional move
    return (board[row][col] == 0 and ( 
        (currentRow == -1 and currentCol==-1) or
        (currentRow-1 == row and currentCol-1 == col) or
        (currentRow-1 == row and currentCol+1 == col) or
        (currentRow+1 == row and currentCol-1 == col) or
        (currentRow+1 == row and currentCol+1 == col)
    ))				

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True

def check_lose(player):
    if(player == 1):
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol


    if(currentRow == -1 or currentCol == -1):
        return False

    return not (
        (-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ) or
        (-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ) or
        (-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ) or
        (-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ) 
    )

def restart():
    screen.fill( BG_COLOR )
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0



def bestMove(player = 2):
    bestScore = -100000
    move = None

    global playerTwoCurrentCol
    global playerTwoCurrentRow



    #never used for player
    if(player == 1):
        currentRow = playerOneCurrentRow
        currentCol = playerOneCurrentCol
    else:
        currentRow = playerTwoCurrentRow
        currentCol = playerTwoCurrentCol


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

    if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ):
        board[currentRow-1][currentCol-1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1 , currentCol-1,0,False)
        board[currentRow-1][currentCol-1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow-1 , currentCol-1)

    if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ):
        board[currentRow-1][currentCol+1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+1,0,False)
        board[currentRow-1][currentCol+1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow-1,currentCol+1)

    if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ):
        board[currentRow+1][currentCol-1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-1,0,False)
        board[currentRow+1][currentCol-1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow+1,currentCol-1)

    if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ):
        board[currentRow+1][currentCol+1] = 2
        score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+1,0,False)
        board[currentRow+1][currentCol+1] = 0

        if(score>bestScore):
            bestScore = score
            move = (currentRow+1,currentCol+1)
    

    playerTwoCurrentRow = move[0]
    playerTwoCurrentCol = move[1]
    mark_square( move[0], move[1], 2)
     


    
scores = {
  1: 10,
  2: -10,
  0: 0
}
# depth not use becouse the depth is not const value and it chnage when any player make his move and the  depth in the code handle by
# check_lose(player)
def minimax(board, player, playerOneCurrentRow, playerOneCurrentCol, playerTwoCurrentRow, playerTwoCurrentCol , depth, isMaximizing):
    #check is there any move available for player (1 or 2)
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
        #any arbitary small value 
        bestScore = -100000


        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ):
            board[currentRow-1][currentCol-1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1 , currentCol-1, 0,False)
            board[currentRow-1][currentCol-1] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ):
            board[currentRow-1][currentCol+1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+1,0,False)
            board[currentRow-1][currentCol+1] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ):
            board[currentRow+1][currentCol-1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-1,0,False)
            board[currentRow+1][currentCol-1] = 0

            bestScore = max(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ):
            board[currentRow+1][currentCol+1] = 2
            score = minimax(board,1,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+1,0,False)
            board[currentRow+1][currentCol+1] = 0


            bestScore = max(score,bestScore)
        
        print("BEST SCORE MAX = ",bestScore)
        return bestScore

    else:
        bestScore = 100000
        
        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow-1][currentCol-1] == 0 ):
            board[currentRow-1][currentCol-1] = 2
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-1 , currentCol-1,0,True)
            board[currentRow-1][currentCol-1] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow-1 and currentRow-1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow-1][currentCol+1] == 0 ):
            board[currentRow-1][currentCol+1] = 2
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow-1,currentCol+1,0,True)
            board[currentRow-1][currentCol+1] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol-1 and currentCol-1 < BOARD_COLS and board[currentRow+1][currentCol-1] == 0 ):
            board[currentRow+1][currentCol-1] = 2
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol-1,0,True)
            board[currentRow+1][currentCol-1] = 0

            bestScore = min(score,bestScore)

        if(-1 < currentRow+1 and currentRow+1 < BOARD_ROWS and -1 < currentCol+1 and currentCol+1 < BOARD_COLS and board[currentRow+1][currentCol+1] == 0 ):
            board[currentRow+1][currentCol+1] = 2
            score = minimax(board,2,playerOneCurrentRow,playerOneCurrentCol,currentRow+1,currentCol+1,0,True)
            board[currentRow+1][currentCol+1] = 0

            bestScore = min(score,bestScore)
        
        

        print("BEST SCORE MIN= ",bestScore)
        return bestScore




draw_lines()

font = pygame.font.Font(None, 36)

# MAINLOOP---------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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
                mark_square( clicked_row, clicked_col, player )

                playerOneCurrentRow = clicked_row
                playerOneCurrentCol = clicked_col
                print('Player One Current Row and Col: (',str(playerOneCurrentRow)+','+str(playerOneCurrentCol)+')')


                if check_lose( 2 ):
                    losePlayer = 2
                    game_over = True
                    draw_figures()
                    print("AI lost")

                else:
                    player = 2
                    bestMove(player)

                    if check_lose( 1 ):
                        losePlayer = 1
                        game_over = True
                        print("human  lost")
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


    pygame.display.update()