import random
#create board
board = ["_","_","_",
        "_","_","_",
        "_","_","_"]
currentPlayer = "X"
winner = None
runningMatch = True
#set up the board layout
def playBoard(board) :
    print (board[0] + " | " + board[1] + " | " + board[2])
    print ("---------------")
    print (board[3] + " | " + board[4] + " | " + board[5])
    print ("---------------")
    print (board[6] + " | " + board[7] + " | " + board[8])
    print ("---------------")


# user input
def userInput(board) :
    inp = int(input("Choose a number from 1 to 9 : "))
    if inp >= 1 and inp <= 9 and board[inp-1] == '_' :
        board[inp-1] = currentPlayer
    else :
        print ("Check your number or the place is already taken")

#check for win or tie
#check horizontal
def checkHorizontal(board) :
    global winner
    if board[0] == board[1] == board[2] and board[0] != '_' :
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '_' :
         winner = board[3]
         return True
    elif board[6] == board[7] == board[8] and board[6] != '_' :
        winner = board[6]
        return True
    
#check vertical
def checkVertical(board) :
    global winner
    if board[0] == board[3] == board[6] and board[0] != '_' :
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '_' :
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '_' :
        winner = board[2]
        return True

#check diagonal
def checkDiagonal(board) :
    global winner
    if board[0] == board[4] == board[8] and board[0] != '_' :
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_' :
        winner = board[2]
        return True

#check tie
def checkTie(board) :
    global runningMatch
    if not(checkHorizontal(board)) and not(checkVertical(board)) and not(checkDiagonal(board)) and '_' not in board : 
         playBoard(board)
         print ("The match is a tie")
         runningMatch = False

       
           
    
        

#check for winner
def checkWin() :
    global runningMatch
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board) :
        playBoard(board)
        print ("The winner is " + winner)
        runningMatch = False

#switch player
def switchPlayer() :
    global currentPlayer
    if currentPlayer == "X" :
        currentPlayer = "O"
    else :
        currentPlayer = "X"

#computer as a player 
def computer(board) :
     while currentPlayer == "O" :
        position = random.randint(0 , 8)
        if board[position] == '_' :
            board[position] = "O"
            switchPlayer()



#get the game running
while runningMatch :
    playBoard(board)
    userInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    if runningMatch :
        computer(board)
        checkWin()
        checkTie(board)
    


    

    
    
