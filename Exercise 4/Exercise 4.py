
import random

def main():
    #list which contains the number of victories of each player and the number of ties
    #results[0] = player1 win counter, results[1] = player2 win counter, results[2] = tie counter 
    results = [0,0,0] 
    #to check if we are in the cheating portion of the program
    cheating_time = False
    #check to not move to players 2 turn if player one has already
    flag2 = False
    outcome = ""
    outcome2 = ""
    #we run the game 200 times(100 for the normal program and 100 for the cheating program)
    for i in range(200):
        print(f"    Game {i+1}    \n")
        deck = create_deck()
        
        player1=[] #player1 hand
        player2=[] #player2 hand
        players1_sum = 0
        players2_sum = 0

        print("P1 joins the game")

        players1_sum = player_draw_step(player1,deck,cheating_time)

        check_result(players1_sum,players2_sum,results)
        if(players1_sum > 21):
            print("")
            flag2 = True

        #if player one has not lost yet do this
        if flag2 == False:
            print("P2 joins the game") #we add player 2
        
            players2_sum = player_draw_step(player2,deck,cheating_time)

            check_result(players1_sum,players2_sum,results)

            #breakline for next game
            print("")

        #switch to the cheating games
        if(i == 99):
            #save the outcome
            outcome = f"the results of 100 games without cheating are: \nPlayer1 victories: {results[0]}\nPlayer2 victories: {results[1]}\nTies victories: {results[2]}"
            #clear the results
            for i in range(3): results[i] = 0
            cheating_time = False
        
        flag2 = False
        
    #save outcome2
    outcome2 = f"the results of 100 games with cheating are: \nPlayer1 victories: {results[0]}\nPlayer2 victories: {results[1]}\nTies victories: {results[2]}"
    #print the results
    print(outcome)
    print(outcome2)
    print("terminating program")
    input("press any key to continue...")
     
#creates a deck
def create_deck():
    colored_cards = []
    figures = ["J", "Q", "K"]
    uncolored_cards_cards = [i for i in range(1, 11)] + figures
    colors = ["Hearts", "Swords", "Clumbs", "Diamonds"]
    #for each uncolored card give create a colored one with the 4 possible colors
    for uncolored_card in uncolored_cards_cards:
        for color in colors:
            colored_cards.append([uncolored_card,color])
    random.shuffle(colored_cards)
    #colored_cards shuffled is the deck
    return colored_cards

#draws a random card for the according player from the deck and stops if it reaches 16 or greater
def player_draw_step(player,deck,cheating_time):
    figures = ["J", "Q", "K"]
    players_sum = 0

    #if we are on the cheating games do the following:
    if(cheating_time == True):
        #to determine if it the first or the second player, if it is the first player the deck will be full(52 cards)
        if len(deck) == 52:
            player.append(deck.pop())
            #check if the card is the one we need
            while player[0][0] != 10 and player[0][0] != "J" and player[0][0] != "Q"  \
                and player[0][0] != "K":
                #if it is not put it back in the deck
                deck.append(player.pop())
                #shuffle the deck
                random.shuffle(deck)
                #redraw a card
                player.append(deck.pop())
        #if it is the second's player draw
        else:
            player.append(deck.pop())
            #check if the card is the one we need
            while player[0][0] == 10 or player[0][0] == "J" or player[0][0] == "Q"  \
                or player[0][0] == "K":
                #if it is not put it back in the deck
                deck.append(player.pop())
                #shuffle the deck
                random.shuffle(deck)
                #redraw a card
                player.append(deck.pop())
    
    while players_sum<16:
        players_sum=0
        #remove a card from the deck and give it to player one
        player.append(deck.pop())
        #NOTE print (player1) for checking
        for card in player:
            #calculate points for figures
            if card[0] in figures:
                players_sum = players_sum + 10 # j,Q,K count as 10
            #every other card
            else:
                players_sum = players_sum+card[0] 
        print(f"They drew {card[0]} of {card[1]}")
        print(f"The sum is now {players_sum}")
        print("")

    print("\n")
    return players_sum

def check_result(players1_sum,players2_sum,results):

    #check if it player's one turn
    if players2_sum == 0:
        #if player1 sum of the cards is not between 16,21 then player2 wins
        if players1_sum>21:
            print("P2 wins!")
            results[1] += 1
        #if that is not the case return result = "", which means that the game continues
        return results
    
    #if player2 sum of the cards is not between 16,21 then player1 wins
    if players2_sum>21:
        print("P1 wins!")
        results[0] +=1
    #if player1 sum is greater than player2 sum, then player1 wins    
    elif players1_sum>players2_sum:
        print("P1 wins!")
        results[0] +=1
    #if player2 sum is greater than player1 sum, then player2 wins
    elif players2_sum>players1_sum:
        print("P2 wins!")
        results[1] +=1
    #if  player2 sum and player1 sum are equal(final option), then it is a draw
    else:
        print("draw!")
        results[2] +=1
    
    return results
    
    
#program's entry point
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()