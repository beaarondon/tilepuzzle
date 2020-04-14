from typing import List, TypeVar
from copy import deepcopy
# from collections import deque
# should i make a deque??

T = TypeVar("T")   # List[List[int]]


def tilepuzzle(start: T, goal: T) -> List[T]:
    return reverse(statesearch([start], goal, []))   # reverse to: start -> goal


def statesearch(unexplored: List, goal: T, path: List) -> List[T]:
    if unexplored == []:   # no more states left to explore
        return []   # no path found to goal
    elif goal == head(unexplored):   # if the oldest entry == goal
        return conc(goal, path)
    else:
        # expand current state, add new states to unexplored list
        result = statesearch(generateNewStates(head(unexplored)), goal, conc(head(unexplored), path))
        if result != []:   # if a path to the goal was found
            return result
        else:
            return statesearch(tail(unexplored), goal, path)   # RECURSE; tail = everything EXCEPT head = [1:]

###

def moveU(curState: T):
    for row in range(len(curState)):
        for col in range(len(curState[0])):
            if curState[row][col] == 0 and row-1 >= 0:
                replacement = curState[row-1][col]
                return generateNew(curState, row, col, 0, replacement, "u")

def moveD(curState: T):
    for row in range(len(curState)):
        for col in range(row):
            if curState[row][col] == 0 and row+1 < len(curState):
                replacement = curState[row+1][col]
                return generateNew(curState, row, col, 0, replacement, "d")

def moveL(curState: T):
    for row in range(len(curState)):
        for col in range(row):
            if curState[row][col] == 0 and col-1 >= 0:
                replacement = curState[row][col-1]
                return generateNew(curState, row, col, 0, replacement, "l")

def moveR(curState: T):
    for row in range(len(curState)):
        for col in range(row):
            if curState[row][col] == 0 and col+1 < row:
                replacement = curState[row][col+1]
                return generateNew(curState, row, col, 0, replacement, "r")

###

def generateNew(curState: T, row: int, col: int, empty: int, replacement: int, movement: str) -> List[T]:
    result = []
    result.append(swap(curState, row, col, empty, replacement, movement))
    return result

def swap(oldState: T, row: int, col: int, empty: int, replacement: int, movement: str) -> List[T]:
    newState = deepcopy(oldState)
    newState[row][col] = deepcopy(replacement)
    if movement.lower() == "u":
        newState[row-1][col] = empty
    elif movement.lower() == "d":
        newState[row+1][col] = empty
    elif movement.lower() == "l":
        newState[row][col-1] = empty
    elif movement.lower() == "r":
        newState[row][col+1] = empty
    return newState


def reverseEach(listOfLists: List[T]) -> List[T]:
    result = []
    for list in listOfLists:
        result.append(reverse(list))
    return result


def generateNewStates(curState: T) -> List:   # add all new possible moves to list of unexplored states
    newStates = []
    if moveU(curState) is not None:
        newStates += moveU(curState)
    if moveD(curState) is not None:
        newStates += moveD(curState)
    if moveL(curState) is not None:
        newStates += moveL(curState)
    if moveR(curState) is not None:
        newStates += moveR(curState)
    return newStates
    # add all generated new states to unexplored list

###

def conc(item: T, list: List[T]):
    return [item] + list
def head(list):
    return list[0]
def tail(list):
    return list[1:]
def reverse(list):
    return list[::-1]
