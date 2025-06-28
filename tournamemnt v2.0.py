import array
import random
playernum = 6
verysmartplayer = 0
friendlyplayer = 0
sampleplayer = 0
othersampleplayer = 0
forgivenessplayer = 0
playerorder = [0,1,2,3,4,5,6]
player1moves = [0]
player2moves = [0]
currentmove = 0
gamelength = 200
player1red = False
player2red = False
share = 3
steal = 5
var11 = 0
var12 = 0
var13 = 0
var14 = 0
var15 = 0
var21 = 0
var22 = 0
var23 = 0
var24 = 0
var25 = 0
p1p = 0
p2p = 0
aplayer1 = 0
aplayer2 = 0
aplayer3 = 0
aplayer4 = 0 
aplayer5 = 0
playerdefined = 0
currentround = 1
def rules():
    global player1moves, player2moves, currentmove, p1p, p2p
    if(player1moves[currentmove] == share and player2moves[currentmove] == share):
        p1p = p1p + share
        p2p = p2p + share
    if(player1moves[currentmove] == steal and player2moves[currentmove] == share):
        p1p = p1p + steal
    if(player1moves[currentmove] == share and player2moves[currentmove] == steal):
        p2p = p2p + steal
    if(player1moves[currentmove] == steal and player2moves[currentmove] == steal):
        p1p = p1p + 1
        p2p = p2p + 1
    if(player1red == True):
        player1moves.append(steal)
    else:
        player1moves.append(share)
    if(player2red == True):
        player2moves.append(steal)
    else:
        player2moves.append(share)
def verysmart():
    global p1verysmart, p2verysmart
    def p1verysmart():
        global player1moves, player2moves, var11, var12, var13, var14, var15, player1red
        if(currentmove != 1):
        #stops the forgiving part if they steal first
            for i in range (-5,0):
                if(var11 == 0 and player1moves[i] == steal and player2moves[i] == share):
                        var11 = -1
                if(var11 == 0 and player1moves[i] == share and player2moves[i] == steal):
                        var11 = 1
            #stops the forgiving part if they steal for 3 moves straight
            for i in range (0,3):
                if(var12 != 3 and player2moves[currentmove - i] == steal):
                    var12 = var12 + 1
                elif(var12 == 3):
                    var11 = 1
            #after 5 moves, steal unless they steal
            for i in range (0,5):
                if(player2moves[currentmove-i] == share):
                    var13 = var13 + 1
                if(var13 == 5):
                    player1red = True
                var13 = 0
            #Stops retaliation to retaliation
            if(player1moves[currentmove - 1] == steal and player2moves[currentmove] == steal and var11 != 1):
                player1red = False
            else:
                player1red = False
    def p2verysmart():
        global player1moves, player2moves, var21, var22, var23, var24, var25, player2red
        if(currentmove != 1):
            #stops the forgiving part if they steal first
            for i in range (-5,0):
                if(var21 == 0 and player2moves[i] == steal and player1moves[i] == share):
                    var21 = -1
                if(var21 == 0 and player2moves[i] == share and player1moves[i] == steal):
                    var21 = 1
            #stops the forgiving part if they steal for 3 moves straight
            for i in range (0,3):
                if(var22 != 3 and player1moves[currentmove - i] == steal):
                    var22 = var22 + 1
                elif(var22 == 3):
                    var21 = 1
            #after 5 moves, steal unless they steal
            for i in range (0,5):
                if(player1moves[currentmove-i] == share):
                    var23 = var23 + 1
                if(var23 == 5):
                    player2red = True
                var23 = 0
                #Stops retaliation to retaliation
                if(player1moves[currentmove - 1] == steal and player2moves[currentmove] == steal and var11 != 1):
                        player2red = False
            else:
                player2red = False
    if(verysmartplayer == 1):
        p1verysmart()
    if(verysmartplayer == 2):
        p2verysmart()
def friendly():
    global p1friendly, p2friendly
    def p1friendly():
        global player1red
        player1red = False
    def p2friendly():
        global player2red
        player2red = False
    if(friendlyplayer == 1):
        p1friendly()
    if(friendlyplayer == 2):
        p2friendly()
def sample():
    global p1sample, p2sample
    def p1sample():
        global player2moves, player1red, currentmove, var11
        if(currentmove != 1):
            if(player2moves[currentmove] == share):
                player1red = False
            else:
                var11 = random.randint(1,10)
                if(var11 != 1):
                    player1red = True
                else:
                    player1red = False
        else:
            player1red = False
    def p2sample():
            global player1moves, player2red, currentmove, var21
            if(currentmove != 1):
                if(player1moves[currentmove] == share):
                    player2red = False
                else:
                    var21 = random.randint(1,10)
                    if(var21 != 1):
                        player2red = True
                    else:
                        player2red = False
            else:
                player2red = False
    if(sampleplayer == 1):
        p1sample()
    if(sampleplayer == 2):
        p2sample()
def othersample():
    global p1othersample, p2othersample
    def p1othersample():
        global var11, player2moves, currentmove, player1red, steal
        if(currentmove != 1):
            if(var11 != 1 and player2moves[currentmove] == steal):
                var11 = 1
            if(var11 == 1):
                player1red = True
            else:
                player1red = False
        else:
            player1red = False
    def p2othersample():
        global var21, player1moves, currentmove, player2red, steal
        if(currentmove != 1):
            if(var21 != 1 and player1moves[currentmove] == steal):
                var21 = 1
            if(var21 == 1):
                player2red = True
            else:
                player2red = False
        else:
            player2red = False
    if(othersampleplayer == 1):
        p1othersample()
    if(othersampleplayer == 2):
        p2othersample()
def forgiveness():
    global p1forgiveness, p2forgiveness
    def p1forgiveness():
        global player2moves, var11, currentmove, player1red
        if(currentmove != 1):
            if(player2moves[currentmove] == steal):
                var11 = 1
            if(player2moves[currentmove] == share):
                var11 = 0
            if(var11 == 1):
                player1red = True
            else:
                player1red = False
        else:
            player1red = False
    def p2forgiveness():
        global player1moves, var21, currentmove, player2red
        if(currentmove != 1):
            if(player1moves[currentmove] == steal):
                var21 = 1
            if(player1moves[currentmove] == share):
                var21 = 0
            if(var21 == 1):
                player2red = True
            else:
                player2red = False
        else:
            player2red = False
    if(forgivenessplayer == 1):
        p1forgiveness()
    if(forgivenessplayer == 2):
        p2forgiveness()
if(verysmartplayer <=0 and playerdefined == 0):
    verysmartplayer = random.randint (1,2)
    playerdefined = verysmartplayer
elif(playerdefined == 1):
    verysmartplayer = 2
else:
    verysmartplayer = 1
if(friendlyplayer <=0 and playerdefined == 0):
    friendlyplayer = random.randint (1,2)
    playerdefined = friendlyplayer
elif(playerdefined == 1):
    friendlyplayer = 2
else:
    friendlyplayer = 1
if(sampleplayer <=0 and playerdefined == 0):
    sampleplayer = random.randint (1,2)
    playerdefined = sampleplayer
elif(playerdefined == 1):
    sampleplayer = 2
else:
    sampleplayer = 1
if(othersampleplayer <=0 and playerdefined == 0):
    othersampleplayer = random.randint (1,2)
    playerdefined = othersampleplayer
elif(playerdefined == 1):
    othersampleplayer = 2
else:
    othersampleplayer = 1
if(forgivenessplayer <=0 and playerdefined == 0):
    forgivenessplayer = random.randint (1,2)
    playerdefined = forgivenessplayer
elif(playerdefined == 1):
    forgivenessplayer = 2
else:
    forgivenessplayer = 1

while(currentround <= 6):
    while(gamelength >= 0):
        rules()
        if(playerorder[currentround] == 4):
            verysmart()
        if(playerorder[currentround] == 2):
            friendly()
        if(playerorder[currentround] == 5):
            sample()
        if(playerorder[currentround] == 1):
            forgiveness()
        if(playerorder[currentround] == 3):
            othersample()
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
if(verysmartplayer == 1):
    print("verysmart: " + str(p1p) + " points")
elif(verysmartplayer == 2):
        print("verysmart: " + str(p2p) + " points")
if(friendlyplayer == 1):
    print("friendly: " + str(p1p) + " points")
elif(friendlyplayer == 2):
        print("friendly: " + str(p2p) + " points")
if(sampleplayer >=0):
    print("sample: " + str(p1p) + " points")
elif(sampleplayer == 2):
        print("sample: " + str(p2p) + " points")
if(othersampleplayer == 1):
    print("othersample: " + str(p1p) + " points")
elif(othersampleplayer == 2):
        print("othersample: " + str(p1p) + " points")
print("=======================")