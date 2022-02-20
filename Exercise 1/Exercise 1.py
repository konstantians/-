import random

def main():
    #the 100 turns, that the game must be played
    counter = 0
    for i in range(100):
        print(f"\n           TURN {i+1}          \n")
        tic_tac_toe_board = create_tic_tac_toe_board()
        
        #check if the condition to end the game has been met 
        turn_over = False
        while (turn_over == False):
            #get a random size ring
            ring_size = get_ring()
            #get random coordinates
            (x_ring_coordinate, y_ring_coordinate) = get_coordinates(ring_size,tic_tac_toe_board)
            #set the ring coordinates values
            tic_tac_toe_board = set_coordinates(ring_size,tic_tac_toe_board,x_ring_coordinate,y_ring_coordinate)
            #check if the condition is met
            turn_over = check_if_game_over(tic_tac_toe_board)
            counter += 1
        
        draw_final_board(tic_tac_toe_board)

    print(f"\n the average amount of moves needed to finish a game were {counter/100} moves or {int(counter/100)} moves")

    print("\n terminating program")
    input("press any key to continue...")
             
#create the tic_tac_toe_board with a 2 dimensional array/list
def create_tic_tac_toe_board():
    rows, cols = (3, 3)
    tic_tac_toe_board = [["0" for i in range(cols)] for j in range(rows)]
    #print(tic_tac_toe_board) #NOTE for checking
    return tic_tac_toe_board

#picks from the rings, a large ring(2/L) or a medium ring(1/M) or a small ring(0/S) 
def get_ring():
    ring_size = random.randrange(3)
    if ring_size == 0: ring_size = "S"
    elif ring_size == 1: ring_size = "M"
    elif ring_size == 2: ring_size = "L" 

    return ring_size

#gets the random coordinates for the ring(small ring = 0/S, medium ring = 1/M, large ring = 2/L)
def get_coordinates(ring_size,tic_tac_toe_board):
    x_ring_coordinate = random.randrange(3)
    y_ring_coordinate = random.randrange(3)

    #check if there is a ring the of same size already there 
    while(ring_size in tic_tac_toe_board[x_ring_coordinate][y_ring_coordinate]):
        x_ring_coordinate = random.randrange(3)
        y_ring_coordinate = random.randrange(3)

    #return the cooardinates
    return x_ring_coordinate,y_ring_coordinate

def set_coordinates(ring_size,tic_tac_toe_board,x_ring_coordinate,y_ring_coordinate):
    #if the spot does not have any rings
    if tic_tac_toe_board[x_ring_coordinate][y_ring_coordinate] == "0":
        tic_tac_toe_board[x_ring_coordinate][y_ring_coordinate] = ring_size
    #if the spot contains a ring of different size
    else:
        tic_tac_toe_board[x_ring_coordinate][y_ring_coordinate] = \
            tic_tac_toe_board[x_ring_coordinate][y_ring_coordinate] + f" {ring_size} "

    return tic_tac_toe_board
    

#checks if the game is over
def check_if_game_over(tic_tac_toe_board):
    turn_over = False
    for i in range(3):
        #I could make this into one big if, but I do not know if this is a good idea(performance wise and
        # from a readibility angle), so I split it into multiple ifs
        #check horizontally for 3 rings of the same size
        if ("S" in tic_tac_toe_board[i][0] and "S" in tic_tac_toe_board[i][1] and "S" in tic_tac_toe_board[i][2]) \
        or ("M" in tic_tac_toe_board[i][0] and "M" in tic_tac_toe_board[i][1] and "M" in tic_tac_toe_board[i][2]) \
        or ("L" in tic_tac_toe_board[i][0] and "L" in tic_tac_toe_board[i][1] and "L" in tic_tac_toe_board[i][2]): 
            turn_over = True
            break
        #check horizontally for combination(S M L or L M S )
        elif("S" in tic_tac_toe_board[i][0] and "M" in tic_tac_toe_board[i][1] and "L" in tic_tac_toe_board[i][2]) \
        or ("L" in tic_tac_toe_board[i][0] and "M" in tic_tac_toe_board[i][1] and "S" in tic_tac_toe_board[i][2]):
            turn_over = True
            break
        #check vertically for 3 rings of different size
        if ("S" in tic_tac_toe_board[0][i] and "S" in tic_tac_toe_board[1][i] and "S" in tic_tac_toe_board[2][i]) \
        or ("M" in tic_tac_toe_board[0][i] and "M" in tic_tac_toe_board[1][i] and "M" in tic_tac_toe_board[2][i]) \
        or ("L" in tic_tac_toe_board[0][i] and "L" in tic_tac_toe_board[1][i] and "L" in tic_tac_toe_board[2][i]): 
            turn_over = True
            break
        #check vertically for combination(S M L or L M S)
        elif("S" in tic_tac_toe_board[0][i] and "M" in tic_tac_toe_board[1][i] and "L" in tic_tac_toe_board[2][i]) \
        or ("L" in tic_tac_toe_board[0][i] and "M" in tic_tac_toe_board[1][i] and "S" in tic_tac_toe_board[2][i]):
            turn_over = True
            break

    #check diagonally(κύρια διαγώνιος) for the same rings, so 00,11,22 must be the same
    if ("S" in tic_tac_toe_board[0][0] and "S" in tic_tac_toe_board[1][1] and "S" in tic_tac_toe_board[2][2]) \
    or ("M" in tic_tac_toe_board[0][0] and "M" in tic_tac_toe_board[1][1] and "M" in tic_tac_toe_board[2][2]) \
    or ("L" in tic_tac_toe_board[0][0] and "L" in tic_tac_toe_board[1][1] and "L" in tic_tac_toe_board[2][2]):
        turn_over = True
    #check diagonally(κύρια διαγώνιος) for combination(S M L or L M S)
    elif("S" in tic_tac_toe_board[0][0] and "M" in tic_tac_toe_board[1][1] and "L" in tic_tac_toe_board[2][2]) \
    or ("L" in tic_tac_toe_board[0][0] and "M" in tic_tac_toe_board[1][1] and "S" in tic_tac_toe_board[2][2]):
        turn_over = True
    #check diagonally(δευτερεύουσα διαγώνιος) for the same rings, so 20,11,02 must be the same
    if("S" in tic_tac_toe_board[2][0] and "S" in tic_tac_toe_board[1][1] and "S" in tic_tac_toe_board[0][2]) \
    or ("M" in tic_tac_toe_board[2][0] and "M" in tic_tac_toe_board[1][1] and "M" in tic_tac_toe_board[0][2]) \
    or ("L" in tic_tac_toe_board[2][0] and "L" in tic_tac_toe_board[1][1] and "L" in tic_tac_toe_board[0][2]):
        turn_over = True
    #check diagonally(δευτερεύουσα διαγώνιος) for combination(S M L or L M S)
    elif("S" in tic_tac_toe_board[2][0] and "M" in tic_tac_toe_board[1][1] and "L" in tic_tac_toe_board[0][2]) \
    or ("L" in tic_tac_toe_board[2][0] and "M" in tic_tac_toe_board[1][1] and "S" in tic_tac_toe_board[0][2]):
        turn_over = True

    return turn_over

#draws the final board
def draw_final_board(tic_tac_toe_board):
    for i in range(3):
        for j in range(3):
            #to not add the final lines in the end of tic tac toe board
            if(j == 2):
                print(f"    {tic_tac_toe_board[i][j]}")
            else:
                print(f"    {tic_tac_toe_board[i][j]}    |",end = '')
        if i!=2: print(" ---------------------------------- ")

#program's entry point
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
