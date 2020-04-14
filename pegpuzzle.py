def pegpuzzle(start,goal):
    return reverse(statesearch([start],goal,[]))

def statesearch(unexplored,goal,path):
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    else:
        result = statesearch(generateNewStates(head(unexplored)), goal, cons(head(unexplored), path))
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored), goal, path)

# replaceSegment("RR__BB",1,"_R") => "R_R_BB"
def replaceSegment(oldList,pos,segment):
    return oldList[0:pos] + segment + oldList[(pos + len(segment)):]
def generateNew(currState,pos,oldSegment,newSegment):
    result = []
    for i in range(pos, len(currState) - 1):
        if segmentEqual(currState,i,oldSegment):
            result.append(replaceSegment(currState,i,newSegment))
    return result
def segmentEqual(currState,pos,oldSegment):
    return (oldSegment == take(len(oldSegment), drop(pos,currState)))

# generateNewRedSlides("R_R_BB") => ["_RR_BB","R__RBB"]
def generateNewRedSlides(currState):
    return generateNew(currState,0,"R_","_R")
def generateNewRedJumps(currState):
    return generateNew(currState,0,"RB_","_BR")

def generateNewBlueSlides(currState):
    return reverseEach(generateNew(reverse(currState),0,"B_","_B"))
def generateNewBlueJumps(currState):
    return reverseEach(generateNew(reverse(currState),0,"BR_","_RB"))
def reverseEach(listOfLists):
    result = []
    for st in listOfLists:
        result.append(reverse(st))
    return result


def reverse(st):
    return st[::-1]
def head(lst):
    return lst[0]
def tail(lst):
    return lst[1:]
def take(n,lst):
    return lst[0:n]
def drop(n,lst):
    return lst[n:]
def cons(item,lst):
    return [item] + lst


def generateNewStates(currState):
    return (generateNewRedSlides(currState) + generateNewRedJumps(currState) +  generateNewBlueSlides(currState) + generateNewBlueJumps(currState))

# pegpuzzle("RR_BB","BB_RR") =>
# ['RR_BB', 'R_RBB', 'RBR_B', 'RBRB_', 'RB_BR', '_BRBR', 'B_RBR', 'BBR_R', 'BB_RR']