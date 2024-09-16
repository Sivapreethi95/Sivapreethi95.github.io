def printHundred():
    i = 1
    while i <= 100:
        print(i, end=" ")
        i += 1
    print()

def printNumbers(n):
    i = 1
    while i <= n:
        print(i, end=" ")
        i +=1
    print()

def printOddnumbers(n):
    i = 1
    while i <= n:
        if i % 2 == 1:
            print(i, end=" ")
        i +=1
    print()

def printOddnumbersmethodtwo(n):
    i = 1
    while i <= n:
        print(i, end=" ")
        i +=2
    print()

printOddnumbersmethodtwo(10)
#printNumbers(10)
#printNumbers(25)
#printNumbers(1)    
#printHundred()
#printHundred()