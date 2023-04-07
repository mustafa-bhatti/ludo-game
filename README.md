# ludo-game
Ludo inspired game written in python for my programming assignment
Rules:
Each player has 3 tokens
[1,2,3]= player 1
[4,5,6]= player 2
First player to reach the last tile with all three tokens wins.
if a player's token lands on another  player's token , that token is considered killed and removed from the board
if a player roll a six, they are prompted with option to place their token on a board
if a player rolls double six, they are prompted with option to roll again or move their current tokens
if a player rolls double three times, their turn is wasted is considered invalid and next player rolls the dice

**OUTPUT:**
Player 1 Tokens :  [1, 2, 3] 

Player 2 Tokens :  [4, 5, 6] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

Player 1 will roll the dice first

PLAYER 1's Turn


Enter Any key to continue
Rolling the dice..........

.......4,1........

[0, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

PLAYER 2's Turn

Enter Any key to continue

Rolling the dice..........

.......6,1........


Options:
0 : Roll again(only if you rolled 6,6)
1 : Place a token on the board - AVAILABLE  : [4, 5, 6])
2 : Move a token on the board - AVAILABLE  : [])
OPTION : 1
Enter the token you wish to place on the board : [4, 5, 6]  : 
TOKEN : 4
[4, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

Dice =  [1]
Enter the token you wish to move on the board : [4] :  
TOKEN :  4
[0, 4, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

[0, 0, 0, 0] 

