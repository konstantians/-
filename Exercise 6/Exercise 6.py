import random
def main():
    
    playerA_points = 0
    playerB_points = 0
    turn = 0
    #the game is played for 100 turns
    for turn in range (100):
        #create a 2 dimensional array/list which will act as our chessboard
        # (Rows,Columns) = create_chessboard()
        chessboard = create_chessboard()
        players_turn = determine_players_turn(turn)

        chessboard = place_pawns(chessboard)

        (playerA_points, playerB_points) = determine_points(players_turn,chessboard,playerA_points,playerB_points)

        #increase the game rounds 
        turn += 1
    
    print(f"player 1 gathered : {playerA_points} \n")
    print(f"player 2 gathered : {playerB_points} \n")
    print("program terminating")
    input("press any key to continue...")
    
    return

def create_chessboard():

    rows, cols = (8, 8)
    chessboard = [[0 for i in range(cols)] for j in range(rows)]
    #print(chessboard) #NOTE for checking
    return chessboard

def determine_players_turn(turn):
    #player 1 plays in even turns
    if (turn%2 == 0):
        print(f"Turn {turn}, it is player's 1 turn")
        return 1

    #player 2 plays in odd turns
    else:
        print(f"Turn {turn}, it is player's 2 turn")
        return 2

#def place_pawns(Rows,Columns):
def place_pawns(chessboard):       
    #set random location for the queen

    position_x_axis_queen = random.randrange(8)
    position_y_axis_queen = random.randrange(8)
    
    chessboard[position_x_axis_queen][position_y_axis_queen] = "Q"

    #set random location for the bishop

    position_x_axis_bishop = random.randrange(8)
    position_y_axis_bishop = random.randrange(8)


    #check if the bishop falls on the queen
    while(chessboard[position_x_axis_bishop][position_y_axis_bishop] == "Q"):
    
        position_x_axis_bishop = random.randrange(8)
        position_y_axis_bishop = random.randrange(8)

    chessboard[position_x_axis_bishop][position_y_axis_bishop] = "B"
    
    #set random location for the rook
    position_x_axis_rook = random.randrange(8)
    position_y_axis_rook = random.randrange(8)

    #check if the rook falls on the queen or on the bishop
    while(chessboard[position_x_axis_rook][position_y_axis_rook] == "Q" or chessboard[position_x_axis_rook][position_y_axis_rook] == "B"):
    
        position_x_axis_rook = random.randrange(8)
        position_y_axis_rook = random.randrange(8)
    
    chessboard[position_x_axis_rook][position_y_axis_rook] = "R"

    #print(chessboard) #NOTE for checking

    return chessboard


def determine_points(players_turn,chessboard,playerA_points,playerB_points):

   
    
    if(players_turn == 1):
        
        #check queen,bishop and rook positions
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "Q":
                    queen = (i,j)
                if chessboard[i][j] == "B":
                    bishop = (i,j)
                if chessboard[i][j] == "R":
                    rook = (i,j)
        
        
        #check horizontally if there is a bishop and a rook
        if queen[0] == bishop[0] and queen[0] == rook[0]:
            playerA_points += 2
        #check horizontally if there is only bishop
        elif queen[0] == bishop[0]:
            playerA_points += 1
        #check horizontally if there is only rook
        elif queen[0] == rook[0]:
            playerA_points += 1

        #check vertically if there is a bishop and a rook
        if queen[1] == bishop[1] and queen[1] == rook[1]:
            playerA_points += 2
        #check vertically if there is only a bishop
        elif queen[1] == bishop[1]:
            playerA_points += 1
        #check vertically if there is only a rook
        elif queen[1] == rook[1]:
            playerA_points += 1

        
        for i in range(8):
            #check diagonally(κύρια διαγώνιος) if there is bishop and a rook 
            #all pawns that are diagonal are seperated from 11 other positions, the following code checks it(for example 11 22 33 44 or 12 23 34 45)
            if (int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))+ (i * 11) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 11)) \
            and (int(str(queen[0]) + str(queen[1])) == int(str(rook[0]) + str(rook[1]))+ (i * 11) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 11)):

                playerA_points += 2
             #check diagonally if there is only bishop  
            elif int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))+ (i * 11) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 11):
                playerA_points += 1

             #check diagonally if there is bishop and a rook 
            elif int(str(queen[0]) + str(queen[1])) == int(str(rook[0]) + str(rook[1]))+ (i * 11) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 11):
                playerA_points += 1
            #check diagonally(δευτερεύουσα διαγώνιος) if there is bishop and a rook 
            #all pawns that are diagonal are seperated from 9 other positions, the following code checks it(for example 18 27 36 or 17 26 35)
            if (int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))+ (i * 9) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 9)) \
            and (int(str(queen[0]) + str(queen[1])) == int(str(rook[0]) + str(rook[1]))+ (i * 9) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 9)):

                playerA_points += 2
             #check diagonally if there is only bishop  
            elif int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))+ (i * 9) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 9):
                playerA_points += 1

             #check diagonally if there is bishop and a rook 
            elif int(str(queen[0]) + str(queen[1])) == int(str(rook[0]) + str(rook[1]))+ (i * 9) \
            or int(str(queen[0]) + str(queen[1])) == int(str(bishop[0]) + str(bishop[1]))- (i * 9):
                playerA_points += 1
            
    else:

        #check queen,bishop and rook positions
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "Q":
                    queen = (i,j)
                if chessboard[i][j] == "B":
                    bishop = (i,j)
                if chessboard[i][j] == "R":
                    rook = (i,j)


        #check horizontally if rook captures the queen
        if rook[0] == queen[0]:
            playerB_points += 1
        #check vertically if rook captures the queen
        elif queen[1] == rook[1]:
            playerB_points += 1

        for i in range(8):
            #check diagonally(κύρια διαγώνιος) if there is only bishop  
            if int(str(bishop[0]) + str(bishop[1])) == int(str(queen[0]) + str(queen[1]))+ (i * 11) \
            or int(str(bishop[0]) + str(bishop[1])) == int(str(queen[0]) + str(queen[1]))- (i * 11):
                playerB_points += 1 
            #check diagonally(κύρια διαγώνιος) if there is only bishop  
            elif int(str(bishop[0]) + str(bishop[1])) == int(str(queen[0]) + str(queen[1]))+ (i * 9) \
            or int(str(bishop[0]) + str(bishop[1])) == int(str(queen[0]) + str(queen[1]))- (i * 9):
                playerB_points += 1

    return playerA_points,playerB_points

#program's entry poiny
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
