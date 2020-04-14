from typing import List, TypeVar
from copy import deepcopy
# from collections import deque
# should i make a deque??

T = TypeVar("T")   # List[List[int]]


def tilepuzzle(start: T, goal: T) -> List[T]:
    return reverse(statesearch([start], goal, [], [start]))   # reverse to: start -> goal


def statesearch(unexplored: List, goal: T, path: List, explored: List) -> List[T]:
    if unexplored == []:   # no more states left to explore
        return []   # no path found to goal
    elif goal == head(unexplored):   # if the oldest entry == goal
        return conc(goal, path)
    else:
        # expand current state, add new states to unexplored list
        result = statesearch(generateNewStates(head(unexplored), explored), goal, conc(head(unexplored), path), explored)
        if result != []:   # if a path to the goal was found
            return result
        else:
            return statesearch(tail(unexplored), goal, path, explored)   # RECURSE; tail = everything EXCEPT head = [1:]

###

def moveU(curState: T):
    for row in range(len(curState)):
        for col in range(len(curState[0])):
            if curState[row][col] == 0 and row-1 >= 0:
                replacement = curState[row-1][col]
                return generateNew(curState, row, col, 0, replacement, "u")
    return None

def moveD(curState: T):
    for row in range(len(curState)):
        for col in range(len(curState[0])):
            if curState[row][col] == 0 and row+1 < len(curState):
                replacement = curState[row+1][col]
                return generateNew(curState, row, col, 0, replacement, "d")
    return None

def moveL(curState: T):
    for row in range(len(curState)):
        for col in range(len(curState[0])):
            if curState[row][col] == 0 and col-1 >= 0:
                replacement = curState[row][col-1]
                return generateNew(curState, row, col, 0, replacement, "l")
    return None

def moveR(curState: T):
    for row in range(len(curState)):
        for col in range(len(curState[0])):
            if curState[row][col] == 0 and col+1 < len(curState):
                replacement = curState[row][col+1]
                return generateNew(curState, row, col, 0, replacement, "r")
    return None
###

def generateNew(curState: T, row: int, col: int, empty: int, replacement: int, movement: str) -> List[T]:
    return swap(curState, row, col, empty, replacement, movement)

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


def generateNewStates(curState: T, explored: List) -> List:   # add all new possible moves to list of unexplored states
    newStates = []
    u = moveU(curState)
    d = moveD(curState)
    l = moveL(curState)
    r = moveR(curState)
    if u is not None and u not in explored:
        newStates = conc(u, newStates)
        explored.append(u)
    if d is not None and d not in explored:
        newStates = conc(d, newStates)
        explored.append(d)
    if l is not None and l not in explored:
        newStates = conc(l, newStates)
        explored.append(l)
    if r is not None and r not in explored:
        newStates = conc(r, newStates)
        explored.append(r)
    return newStates
    # add all generated new states to unexplored list

###

def conc(item: T, list: List[T]):
    return list + [item]
def head(list):
    return list[0]
def tail(list):
    return list[1:]
def reverse(list):
    return list[::-1]
