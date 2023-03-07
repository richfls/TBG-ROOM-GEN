import random

mapGrid= [[0 for i in range(10)] for j in range(10)]


xpos = random.randrange(0,10)
ypos = random.randrange(0,10)

mapGrid[xpos][ypos] = 1

for i in range(10):
    num1 = random.randrange(1,5)
    if mapGrid[xpos][ypos] == 1:
        if xpos <= 10 and xpos>=1 and ypos <=10 and ypos>=1:
            if num1 == 1 :
                 xpos -= 1
            if num1 == 3:
                ypos -=1
        if xpos <=8 and xpos >=0 and ypos <=8 and ypos>=0:
            if num1 == 2:
                 xpos += 1
            else:
                ypos += 1
        mapGrid[xpos][ypos] = random.randrange(2,6)
    
    elif mapGrid[xpos][ypos] !=1:
        if xpos <= 10 and xpos>=1 and ypos <=10 and ypos>=1:
            if num1 == 1 :
                 xpos -= 1
            if num1 == 3:
                ypos -=1
        if xpos <=8 and xpos >=0 and ypos <=8 and ypos>=0:
            if num1 == 2:
                 xpos += 1
            else:
                ypos += 1
        mapGrid[xpos][ypos] = random.randrange(2,6)
            
    
    
for i in range (10):
    for j in range(10):
        if mapGrid[i][j] == 0:
            print("[  ]", end = "")
        else:
            print("[", end = "")
            print(mapGrid[i][j], end = "")
            print("]", end = "")
    print()
