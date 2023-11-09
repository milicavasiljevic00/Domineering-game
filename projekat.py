compMove=(0,'A')

def drawTable(row, column, matrix):  # blackboard drawing
    mat = [[0 for i in range(column*2+3)] for j in range(row*2+3)]     
    if mat[0][0] == 0:
        br=row
        for x in range(0,row*2+3):
            for y in range(0,column*2+3):
                if x==0 or x==1 or x==row*2+1 or x==row*2+2:
                    if y==0 or y==1 or y==column*2+1 or y==column*2+2:
                        if y == 1:
                            mat[x][y]= ("  ")
                        else:
                            mat[x][y] = " "
                    elif x==1 or x==row*2+1:
                        if y%2==0:
                            mat[x][y]= ("═")
                        else:
                            mat[x][y]= (" ")
                    elif y%2!=0:
                        mat[x][y] = (" ")
                    elif x==0 or x==row*2+2:
                        if y%2==0:
                            mat[x][y] =  chr(65 + y//2-1)
                elif y==0 or y==1 or y==column*2+1 or y==column*2+2:
                    if x==0 or x==1 or x==row*2+1 or x==row*2+2:
                        mat[x][y]= (" ")
                    elif y==1 or y==column*2+1:
                        if x%2==0:
                            mat[x][y]= "║"
                        else:
                            mat[x][y]= (" ")
                    elif x%2!=0:
                        mat[x][y] = ("  ")
                    elif y==0 or y==column*2+2:
                        if x%2==0:
                            if br >= 10:
                                mat[x][y] =  str(br) 
                            elif y == column * 2+ 2: 
                                mat[x][y] =  str(br)
                            else: 
                                mat[x][y] = " " + str(br)
                            if y == column*2+2:
                                br = br - 1
                else:
                    if x%2!=0:
                        if y%2==0:
                            mat[x][y]="─"
                        else:
                            mat[x][y]=" "
                    elif y%2!=0:
                        if x%2==0:
                            mat[x][y]="|"
                        else:
                            mat[x][y]=" "
                    else:
                        mat[x][y]=" "

    for i in range(0, row):
      for j in range(0, column):
           mat[i*2+2][j*2+2] = matrix[i][j][1]

    for i in range(0,row*2+3):
        for j in range(0,column*2+3):
            print(mat[i][j], end=" ")
        print("")

def createMatrix(row, column): # matrix definition
    matrix = [[(2, " ") for i in range(0,column)] for y in range(0,row)]    # list of columns for each row
    return matrix

def isValidMove(move, matrix, player, column, row): # checking the validity of moves
    y = ord(move[1]) - 65
    moveValid = False
    if move[0] >= 0 and move[0]<= row and y >= 0 and y < column: 
        if player[1] == "X":
            if row - move[0] - 1 >= 0:
                if matrix[row - move[0]][y] == (2," ") and matrix[row - move[0] - 1 ][y ] == (2, " "):
                    moveValid = True
        else: 
            if y + 1 < column:
                if matrix[row - move[0]][y] == (2, " ") and matrix[row - move[0]][y+1] ==(2," "):
                    moveValid = True    
   

    return moveValid

def playMove(matrix, player, move, column, row): # playing moves
    if not isValidMove(move, matrix, player,column, row):
        return False
    else:
        y= ord(move[1]) - 65 
        if player[1] == "X":
            matrix[row - move[0] ][ y] = player  
            matrix[row  - move[0]-1][ y ] = player
        else:
            matrix[row - move[0] ][ y ] = player
            matrix[row - move[0] ][y+1] = player
    return True

def inputMoveValidation(input): # checking the validity of the entry
    input=input.lstrip(' ')
    input=input.rstrip(' ')
    if len(input)>4:
        print("Incorrect entry!")
        return False
    else:
        l = input.split(' ')
        if len(l)==1:
            print("Wrong entry! Please enter the coordinates in the form -> <type><space><column>")
            return False
        else:
            if not l[0].isnumeric():
                print("Incorrect entry!")
                return False
            if l[1] < 'A' and l[1] > 'Z':
                print("Wrong entry! The column position must be an uppercase letter!")
                return False
            
    return True

def convertInputMove(input): # converting from strings to tuples
    input=input.lstrip(' ')
    input=input.rstrip(' ')
    l = input.split(' ')
    return (int(l[0]), l[1])

def endGame(matrix,player,column,row):  # end game check
     end=True
     if player[1]=="X":
        for i in range(1,row):
            for j in range(0, column):
                if matrix[i][j]==(2," ") and matrix[i-1][j]==(2," "):
                    end=False
                    break
     else:
        for i in range(0,row):
            for j in range(0, column-1):
                if matrix[i][j]==(2," ") and matrix[i][j+1]==(2," "):
                    end=False
                    break
     return end

def availableMoves(matrix, player, column, row): # Determining all possible moves of a specific player
    availableMovesList = []
    for i in range(1,row+1):
        for j in range(65, column+65):
            if playMove(matrix,player, (i,chr(j)),column,row):
                #drawTable(row, column, matrix)
                availableMovesList.append((i,chr(j)))
                deleteMove(matrix, (i, chr(j)), player, row)
    return availableMovesList

def deleteMove(matrix,move,player,row): # Deleting a specific move of a specific player
    y= ord(move[1]) - 65 
    if player[1] == "X":
        matrix[row - move[0] ][ y] = (2, " ")  
        matrix[row  - move[0]-1][ y ] = (2, " ")
    else:
        matrix[row - move[0] ][ y ] = (2, " ")
        matrix[row - move[0] ][y+1] = (2, " ")


def minimax(matrix,player,column,row):
    alpha=-column*row
    beta=column*row+1
    global compMove
    max_value(4, alpha, beta, matrix, player, column, row) #u computerMove se stave globalni row i column neki koje dodam i zove se ovaj playMove dalje
    playMove(matrix,player,compMove,column,row)
    drawTable(row,column,matrix)



def proceni_stanje(matrix,player,column,row):
    possibilities1=availableMoves(matrix,player,column,row)
    if player[1] == "X":
        player1 = ((player[0]+1)%2, "O")
    else: 
        player1 = ((player[0]+1)%2, "X")
    possibilities2=availableMoves(matrix,player1,column,row)
    return len(possibilities1)-len(possibilities2)



def max_value(depth, alpha, beta, matrix, player, column, row):
    lista_novih_stanja = availableMoves(matrix,player,column,row)
    if depth == 0 or lista_novih_stanja is None:
     
        return proceni_stanje(matrix,player,column,row)
    else:
        for s in lista_novih_stanja:
            if playMove(matrix, player, s ,column,row):
                alpha = max(alpha, min_value(depth-1, alpha, beta, matrix, player, column, row))
                deleteMove(matrix, s, player, row)
                if alpha >= beta:
                    global compMove
                    compMove=s
                    return beta
    return alpha


def min_value(depth, alpha, beta, matrix, player, column, row):
    lista_novih_stanja = availableMoves(matrix,player,column,row)
    if depth == 0 or lista_novih_stanja is None:
     
        return proceni_stanje(matrix,player,column,row)
    else:
        for s in lista_novih_stanja:
            if playMove(matrix, player, s ,column,row):
                beta = min(beta, max_value(depth-1, alpha, beta, matrix, player, column, row))
                deleteMove(matrix, s, player, row)
                if beta <= alpha:
                    global compMove
                    compMove=s
                    return alpha
    return beta


def startGame(): # main function
    inputTable=False
    while not inputTable:
        row = input("Enter number of rows: ")
        column = input("Enter number of columns: ")
        if not row.isnumeric() or not column.isnumeric():
            print("Wrong entry!")
            continue
        row = int(row)
        column = int(column)
        inputTable=True
        if row < 2 or column < 2:
            print("The board is not big enough!")  
            inputTable=False
    fpCorrect=False
    while not fpCorrect:
        firstPlayer = input("Enter the choice for the first player - \n human(0) computer(1):")
        if not firstPlayer.isnumeric():
            print("Wrong entry!")
            continue
        else:
            firstPlayer = int(firstPlayer)
            if firstPlayer != 0  and firstPlayer !=1:
                print("Wrong entry!")
                continue
        fpCorrect = True
    player1 = (firstPlayer, "X")
    player2 = ((firstPlayer+1)%2, "O")
    player = player1
    matrix = createMatrix(row,column)
    drawTable(row, column, matrix)
    if player[0]==0:
        move = input("Enter the coordinates of the move:")
    end=False
    while not end:
        if player[0]==1:
            print("Computer on the move:")
            minimax(matrix,player,column,row)
        else:
            if not inputMoveValidation(move):
                move = input("Enter the coordinates of the move:")
                continue
            move = convertInputMove(move)
            if not playMove(matrix,player,move, column, row):
                print("Move "+ str(move)  + " is not valid!")
                move = input("Enter the coordinates of the move:")
                continue
            drawTable(row, column, matrix)
        if player[1] == "X":
            player = player2
        else: 
            player = player1
        end = endGame(matrix,player,column,row)
        if not end:
            if player[0]==0:
                move = input(" Enter the coordinates of the move:")      
        else:
            print("GAME OVER")
            if player[1]=="X":
                print("The winner is player O")
            else:
                print("The winner is player X")
    
if __name__ == "__main__":
    startGame()
