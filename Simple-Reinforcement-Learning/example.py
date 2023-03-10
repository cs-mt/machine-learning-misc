import random 

# For this example there are 2 possible actions, go left, or go right. 
# We have 2 states, START and a blank space. 

qTable = {
        "START": [0.0, 0.0],
        "SPACE": [0.0, 0.0]  # index 0: left, index 1: right
}

agentPos = 0
finishPos = 20

def draw():
    out = ""
    for x in range(finishPos):
        if(x==agentPos):
            out += "X"
        else:
            out += "_"

    print(out)

for x in range(100):
    print(qTable)
    draw()

    state = "START" if agentPos == 0 else "SPACE"

    actionPoints = max(qTable[state])
    action = qTable[state].index(actionPoints)


    for z in range(len(qTable.keys())):
        explore = random.uniform(0, 0.01)
        key = list(qTable.keys())[z]
        for x in range(len(qTable[key])):
            qTable[key][x] += explore


    if(action == 0 and agentPos > 0):
        agentPos-=1 
    elif(action == 1):
        agentPos+=1

    lr = 1
    dr = 0

    reward = 1 if action == 1 else -1
    maxReward = 1

    # New point calculation formula:
    # New Point = Current Point + Learning Rate * (Reward for the Action + Discount Rate * Maximum Possible Reward in the New State - Current Point)

    newPoints = actionPoints + lr * (reward + dr * maxReward - actionPoints)
    qTable[state][action] = newPoints

    if(agentPos == finishPos):
        print("Finished.")
        exit()
