from typing import Union, List
# from collections import deque
# should i make a deque??

T = TypeVar("T", List[List[Union[str, int]]])


def tilepuzzle(start: T, goal: T) -> List[T]:
    return reverse(statesearch([start], goal, []))

def statesearch(unexplored: List, goal: T, path: List) -> List[T]:
    if unexplored == []:   # if there are no more states left to explore
        return []   # no path found to goal
    elif goal == head(unexplored):   # if the initial state == goal
        return cons(goal, path)   ########### cons
    else:
        result = statesearch(generateNewStates(head(unexplored)), goal, cons(head(unexplored), path))
        if result != []:   # if a path to the goal can be found
            return result
        else:
            return statesearch(tail(unexplored), goal, path)   # new start: oldest entry in unexplored list

def moveU(curState: T):
    pass


def moveD(curState: T):
    pass


def moveL(curState: T):
    return reverseEach(generateNew(reverse(curState), 0, "", ""))   ###### reverseEach


def moveR(curState: T):
    return generateNew(curState, 0, "", "")


def generateNew(curState, pos: int, oldSegment: str, newSegment: str) -> List[T]:
    pass


def replaceSegment(oldList, pos: int, segment: str) -> List[T]:
    pass


def segmentEqual(currState: T, pos: int, oldSegment: str) -> Bool:
    return oldSegment == take(len(oldSegment), drop(pos, currState))   ######## take, drop


def reverseEach(listOfLists: List[T]) -> List[T]:
    result = []
    for list in listOfLists:
        result.append(reverse(list))
    return result

def generateNewStates(curState: T) -> List:   # one big list of next possible moves
    return moveU(curState) + moveD(curState) + moveL(curState) + moveR(curState)

###


def cons():
    pass
