# Python Tik Tak Toe Game
import random

# Array of responses
arr = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


# PlayBoard display
def printPlayBoard():
    print("\n")
    print(' '+arr[0][0]+' | '+arr[0][1]+' | '+arr[0][2])
    print("-----------")
    print(' '+arr[1][0]+' | '+arr[1][1]+' | '+arr[1][2])
    print("-----------")
    print(' '+arr[2][0]+' | '+arr[2][1]+' | '+arr[2][2])
    print("\n")

def getInput(sym):
    inp = input("Enter the matric position : ")
    if(pingPlayBoard(inp[0],inp[1])):
        assignInput(inp[0],inp[1],sym)
        printPlayBoard()
        if(checkWinner(sym)):
            print(sym+' has won the game !!!!!  : )')
            exit()
    else:
        print("Already occupied.. Retry !")
        getInput(sym)

def assignInput(row,col,sym):
    arr[row][col]=sym

def pingPlayBoard(row,col):
    if(arr[row][col]!=' '):
        return False
    return True            

def manualDriver():
    for e in range(0,9):
        if(e%2==0):
            getInput('x')
        else:
            getInput('0')
    print("Its a Draw !!!!!!!    : (")

def checkWinner(sym):
    if((arr[0][0]==sym and arr[0][1]==sym and arr[0][2]==sym) or (arr[1][0]==sym and arr[1][1]==sym and arr[1][2]==sym) or (arr[2][0]==sym and arr[2][1]==sym and arr[2][2]==sym)):
        return True
    elif((arr[0][0]==sym and arr[1][1]==sym and arr[2][2]==sym) or (arr[0][2]==sym and arr[1][1]==sym and arr[2][0]==sym)):
        return True
    elif((arr[0][0]==sym and arr[1][0]==sym and arr[2][0]==sym) or (arr[0][1]==sym and arr[1][1]==sym and arr[2][1]==sym) or (arr[0][2]==sym and arr[1][2]==sym and arr[2][2]==sym)):
        return True
    else:
        return False

def autoDriver():
    mySym = raw_input("choose your symbol from 'x' or '0' : ")
    comp = ' '
    print(mySym)
    if(mySym=='x'):
        comp = '0'
    else:
        comp = 'x'

    for e in range(0,9):
        if(e%2==0):
            getInput(mySym)
        else:
            getCompInput(comp)

    print("Its a Draw !!!!!!!    : (") 

def getCompInput(sym):
    row = random.randint(0,2)
    col = random.randint(0,2)
    if(pingPlayBoard(row,col)):
        assignInput(row,col,sym)
        printPlayBoard()
        if(checkWinner(sym)):
            print(sym+' has won the game !!!!!  : )')
            exit()
    else:
        getCompInput(sym)

def init():
    if(input("Do you want to play multiplayer or with computer ? 1 = Computer / 2 = Multiplayer ")==1):
        autoDriver()
    else:
        manualDriver()

init()
