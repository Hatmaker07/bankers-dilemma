import random
SHARE = 6
p1points = 0
p2points = 0
SHARE = 3
STEAL = 5
playerorder = [0,1,2,3,4,5,6]
player1moves = [0]
player2moves = [0]
currentmove = 0
gamelength = 200
var11 = 0
var12 = 0
var13 = 0
var21 = 0
var22 = 0
var23 = 0
currentround = 1
def rules():
    global player1moves, player2moves, currentmove, p1points, p2points
    if(player1moves[currentmove] == SHARE and player2moves[currentmove] == SHARE):
        p1points += SHARE
        p2points += SHARE
    if(player1moves[currentmove] == STEAL and player2moves[currentmove] == SHARE):
        p1points += STEAL
    if(player1moves[currentmove] == SHARE and player2moves[currentmove] == STEAL):
        p2points += STEAL
    if(player1moves[currentmove] == STEAL and player2moves[currentmove] == STEAL):
        p1points += 1
        p2points += 1
def p1verysmart():
    global player1moves, player2moves, var11, var12, var13
    if(currentmove != 1):
    #stops the forgiving part if they STEAL first
        for i in range (-5,0):
            if(var11 == 0 and player1moves[i] == STEAL and player2moves[i] == SHARE):
                    var11 = -1
            if(var11 == 0 and player1moves[i] == SHARE and player2moves[i] == STEAL):
                    var11 = 1
        #stops the forgiving part if they STEAL for 3 moves straight
        for i in range (0,3):
            if(var12 != 3 and player2moves[currentmove - i] == STEAL):
                var12 = var12 + 1
            elif(var12 == 3):
                var11 = 1
        #after 5 moves, STEAL unless they STEAL
        for i in range (0,5):
            if(player2moves[currentmove-i] == SHARE):
                var13 = var13 + 1
            if(var13 == 5):
                player1moves.append(STEAL)
            var13 = 0
        #Stops retaliation to retaliation
        if(player1moves[currentmove - 1] == STEAL and player2moves[currentmove] == STEAL and var11 != 1):
            player1moves.append(SHARE)
        else:
            player1moves.append(SHARE)
def p2verysmart():
    global player1moves, player2moves, var21, var22, var23
    if(currentmove != 1):
        #stops the forgiving part if they STEAL first
        for i in range (-5,0):
            if(var21 == 0 and player2moves[i] == STEAL and player1moves[i] == SHARE):
                var21 = -1
            if(var21 == 0 and player2moves[i] == SHARE and player1moves[i] == STEAL):
                var21 = 1
        #stops the forgiving part if they STEAL for 3 moves straight
        for i in range (0,3):
            if(var22 != 3 and player1moves[currentmove - i] == STEAL):
                var22 = var22 + 1
            elif(var22 == 3):
                var21 = 1
        #after 5 moves, STEAL unless they STEAL
        for i in range (0,5):
            if(player1moves[currentmove-i] == SHARE):
                var23 = var23 + 1
            if(var23 == 5):
                player2moves.append(STEAL)
            var23 = 0
            #Stops retaliation to retaliation
        if(player1moves[currentmove - 1] == STEAL and player2moves[currentmove] == STEAL and var11 != 1):
            player2moves.append(SHARE)
        else:
            player2moves.append(SHARE)
def p1friendly():
    player1moves.append(SHARE)
def p2friendly():
    player2moves.append(SHARE)
def p1sample():
    global player2moves, currentmove, var11
    if(currentmove != 1):
        if(player2moves[currentmove] == SHARE):
            #returns false if the other player SHAREs
            player1moves.append(SHARE)
        else:
            #has a 8 in 9 chance of returning true if the other player STEALs
            var11 = random.randint(1,10)
            if(var11 != 1):
                player1moves.append(STEAL)
            else:
                player1moves.append(SHARE)
    else:
        #SHAREs on the 1st move
        player1moves.append(SHARE)
def p2sample():
        global player1moves, currentmove, var21
        if(currentmove != 1):
            if(player1moves[currentmove] == SHARE):
                player2moves.append(SHARE)
            else:
                var21 = random.randint(1,10)
                if(var21 != 1):
                    player2moves.append(STEAL)
                else:
                    player2moves.append(SHARE)
        else:
            player2moves.append(SHARE)
def p1othersample():
    global var11, player2moves, currentmove, STEAL
    if(currentmove != 1):
        if(var11 != 1 and player2moves[currentmove] == STEAL):
            var11 = 1
        if(var11 == 1):
            player1moves.append(STEAL)
        else:
            player1moves.append(SHARE)
    else:
        player1moves.append(SHARE)
def p2othersample():
    global var21, player1moves, currentmove, STEAL
    if(currentmove != 1):
        if(var21 != 1 and player1moves[currentmove] == STEAL):
            var21 = 1
        if(var21 == 1):
            player2moves.append(STEAL)
        else:
            player2moves.append(SHARE)
    else:
        player2moves.append(SHARE)
def p1forgiveness():
    global player2moves, var11, currentmove
    if(currentmove != 1):
        if(player2moves[currentmove] == STEAL):
            var11 = 1
        if(player2moves[currentmove] == SHARE):
            var11 = 0
        if(var11 == 1):
            player1moves.append(STEAL)
        else:
            player1moves.append(SHARE)
    else:
        player1moves.append(SHARE)
def p2forgiveness():
    global player1moves, var21, currentmove
    if(currentmove != 1):
        if(player1moves[currentmove] == STEAL):
            var21 = 1
        if(player1moves[currentmove] == SHARE):
            var21 = 0
        if(var21 == 1):
            player2moves.append(STEAL)
        else:
            player2moves.append(SHARE)
    else:
        player2moves.append(SHARE)
pselect1 = []
pselect2 = []
score = []
for i in range (0, len(pselect1)):
    for j in range (0, len(pselect2)):
        pselect1[i]()
        pselect2[j]()
        append.score(p1points)
        append.score(p2points)
        p1points = 0
        p2points = 0
        currentmove = 0
        player1moves = []
        player2moves = []
while(currentround <= 6):
    while(gamelength >= 0):
        rules()
        if(playerorder[currentround] == 1):
            forgiveness()
        if(playerorder[currentround] == 2):
            friendly()
        if(playerorder[currentround] == 3):
            othersample()
        if(playerorder[currentround] == 4):
            verysmart()
        if(playerorder[currentround] == 5):
            sample()
        gamelength = gamelength - 1
        currentmove = currentmove + 1
    currentround = currentround + 1
print("=======================")
print("       --------  ")
print("      /  |  |  \ ")
print("     /          \ ")
print("     |  \    /   | ")
print("     \   ====    /")
print("      \         /")
print("        ------- ")
print("=======================")
#points are printed here

