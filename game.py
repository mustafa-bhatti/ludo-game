# Assignment 1  - COMP 111
#Name : Ghulam Mustafa Bhatti - 261947095
import random
p1 = [[1, 2, 3], [4, 5, 6]] #token list
temp1 = [1, 2, 3] # player1 tokens on the board
temp2 = [4, 5, 6] # player2 tokens on the board
arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]   # Initialises Variables


def reset(): # Resets the board

    global temp1, arr, p1,  temp2
    arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    p1 = [[1, 2, 3],[4, 5, 6]]

    temp1 = [1, 2, 3]
    temp2 = [4, 5, 6]


def board(): # Displays the current state of the board

    for i in arr:
        print(i, "\n")


def diceRoll(): # Rolls the dice twice returns them as a list

    num = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(f"Rolling the dice..........\n\n.......{num},{num2}........\n")
    num = [num, num2]
    return num


def findIndex(token):  # Finds index of the token

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == token:
                index = [i, j]
                return index


def kill(tBoard, token): # kills the opponent token, takes the index positions from the board

    if tBoard in temp1 and token > 3:
        p1[1].append(token)
        print("Player 2's token killed!!\n")
    elif tBoard in temp2 and 0 < token < 4:
        p1[0].append(token)
        print("Player 1's token killed\n")
    elif token == 0: # if the target index has zero 
        return 1
    else:
        print("Your token is already on this position, Move your token first\n")
        return 0

def move(dice, index, token, tBoard,counter=0): # moves the tokens and handles special cases

    if counter==2: # max number of retries
        return 0
    if index == None:
        print("Token is not on the board, Try Again\n")
    else:
        t0 = index[0]
        t1 = index[1]
        num = index[1]+dice
        y = t0
        x = t1
        if num > 3:  # when next row is needed
            y += 1
            x = 3-x
            dice -= x  # removes number of tiles skiipped in the first row
            if dice > 4:  # when another row is needed
                dice -= 4
                y += 1
                x = dice-1
            else:  # another row is not needed
                x = dice-1
        else:
            x += dice  # new row is not needed
        if x > 3 or y > 3: # special case if index exceeds the (3)(3)
            print("Can't place your token, Next Turn\n")
        else:
            k=kill(arr[t0][t1],arr[y][x])
            if k==0:
                token = int(input(f"Enter the token you wish to move on the board : {tBoard}  :  \nTOKEN : "))
                index = findIndex(token)
                return move(dice, index, token, tBoard,counter+1)
            else:
                if y==3 and x == 3: # Final position 
                    arr[3][3]=0
                    arr[t0][t1] = 0
                    if token>3:
                        temp2.remove(token) # removes the token from player list
                    else:
                        temp1.remove(token)
                else:
                    arr[y][x] = token # moves the token
                    arr[t0][t1] = 0

def finalMove(dice, tBoard, special_case=False, counter=0): # main function to handle moving tokens
    if special_case == True: # if only one dice is left
        print("Dice = ", dice)
        token = int(input(f"Enter the token you wish to move on the board : {tBoard} :  \nTOKEN :  "))
        if token not in tBoard:
            print("\nInvalid Token, Try Again\n")
            return finalMove(dice, tBoard, True, counter + 1)
        index = findIndex(token)
        dice = dice[0]
        move(dice, index, token, tBoard)
        board()
    else:
        if counter>3:
            return 0
        print("Dice = ",dice)
        token = int(input(f"Enter the token you wish to move on the board : {tBoard} :  \nTOKEN :  "))
        if token not in tBoard:
            print("\nInvalid Token, Try Again\n")
            return finalMove(dice, tBoard, counter + 1)
        dice1 = dice[0]
        index = findIndex(token)
        move(dice1, index, token, tBoard)
        board()
        return finalMove(dice[1:], tBoard, True) # recursively calls the function again for the other dice




def tokenBoard(tBoard, temp): # returns the tokens present on the board

    tokenBoard = []
    for i in temp:
        if i not in tBoard:
            tokenBoard.append(i)
    return tokenBoard



def turn(player,tBoard, counter=0): # handles the player turn, rolls the dice and handle all the special cases as well

    dice =diceRoll()
    if counter == 3:
        print(f"You rolled 6 three times, Next Turn\n")
        return 1

    if 6 in dice:  # prompts user to choose 
        option = int(input(f"\nOptions:\n0 : Roll again(only if you rolled 6,6)\n1 : Place a token on the board - AVAILABLE  : {player})\n2 : Move a token on the board - AVAILABLE  : {tBoard})\nOPTION : "))
        if option>2:
            option = int(input(f"\nWRONG INPUT\nOptions:\n0 : Roll again\n1 : Place a token on the board - AVAILABLE  : {player})\n2 : Move a token on the board - AVAILABLE  : {tBoard})\nOPTION : "))

        if option == 1:
            token = int(input(f"Enter the token you wish to place on the board : {player}  : \nTOKEN : "))
            if token not in player:
                print("invalid choice")
            else:
                if arr[0][0] == 0:  # starts the game at (0)(0)

                    arr[0][0] = token
                    player.remove(token)
                    tBoard.append(token)
                    board()
                    dice.remove(6)
                    finalMove(dice, tBoard, True) # option for the other dice


                else:
                    tBoard.append(token)
                    k = kill(tBoard[-1], arr[0][0])   ## if another token is already there
                    if k == 0:
                        finalMove(dice, tBoard)
                    else:
                        if token>3:
                            p1[1].remove(token)
                        elif 0 < token < 4:
                            p1[0].remove(token)
                        arr[0][0]=token
                        board()

        elif option == 2: # moves the token present on the board
            if len(tBoard)==0:
                print("invalid choice")
            else:
                finalMove(dice, tBoard)

        elif option==0: # rolls again
            if [6,6] == dice:
                print("Dice = ",dice)
                next=turn(player,tBoard,counter+1)
                if next!=1:
                    return turn(player,tBoard)
                return next
            else:
                print("invalid choice")


    else:
        if len(tBoard)>0:
            finalMove(dice,tBoard)
        else:
            board()

    return player #returns updated player token list

def check_win():
    if len(temp1) == 0 and len(p1[0]) == 0:
        print("PLAYER 1 Won\n")
        return True
    elif len(temp2) == 0 and len(p1[1]) == 0:
        print("PLAYER 2 Won\n")
        return True
    else:
        return False


# main game 
game = True
while game == True:
    print("Player 1 Tokens : ", p1[0], "\n\nPlayer 2 Tokens : ", p1[1], "\n")
    board()
    print("Player 1 will roll the dice first\n")
    win = False
    while win == False:
        # Player 1 turn main
        print("PLAYER 1's Turn\n")
        resume = input("Enter Any key to continue\n")
        t_Board = tokenBoard(p1[0], temp1) # returns tokens on the board
        p = turn(p1[0], t_Board)
        p1[0] =p  # updates player1 list
        win=check_win()
        print("PLAYER 2's Turn\n")
        resume = input("Enter Any key to continue\n")
        t_Board = tokenBoard(p1[1], temp2) 
        p = turn(p1[1], t_Board)
        p1[1] = p # updates player 2 list
        win=check_win()
    ans = input("Do you want to play again? (y/n)\n")
    if ans == "y":
        reset()
    elif ans == "n":
        game = False
    else:
        print("Wrong Input")
