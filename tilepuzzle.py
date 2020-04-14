from typing import List, TypeVar
from copy import deepcopy

T = TypeVar("T")   # List[List[int]]

def tilepuzzle(start: T, goal: T) -> List[T]:
    return (statesearch([start], goal, [], [start], []))   # reverse to: start -> goal


def statesearch(unexplored: List, goal: T, path: List, generated: List, newStates: List) -> List[T]:
    for state in unexplored:
        if state not in newStates:
            newStates = conc(state, newStates)
        if state in path and state in newStates:
            newStates.remove(state)
    """
    START: BRUTE FORCE REMOVE DUPLICATE STATES (delete section to see)
    """
    if len(path) >= 2:
        if path[len(path)-1] == path[len(path)-2]:
            path.remove(path[len(path)-1])
    """
    END: BRUTE FORCE REMOVE DUPLICATE STATES
    """
    if unexplored == []:   # no more states left to explore
        return []   # no path found to goal
    elif goal == head(unexplored):   # if the oldest entry == goal
        return conc(goal, path)
    else:
        # expand current state, add new states to unexplored list
        result = statesearch(generateNewStates(head(unexplored), generated, newStates), goal, conc(head(unexplored), path), generated, newStates)   ##### WHY DOES THIS DO TWICE?
        if result != []:   # if a path to the goal was found
            return result
        else:
            return statesearch(tail(unexplored), goal, generated, newStates)   # RECURSE; tail = everything EXCEPT head = [1:]

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

def generateNewStates(curState: T, generated: List, newStates: List) -> List:   # add all new possible moves to list of unexplored states
    u = moveU(curState)
    d = moveD(curState)
    l = moveL(curState)
    r = moveR(curState)
    if u is not None and u not in generated:
        newStates = conc(u, newStates)
        generated.append(u)
    if d is not None and d not in generated:
        newStates = conc(d, newStates)
        generated.append(d)
    if l is not None and l not in generated:
        newStates = conc(l, newStates)
        generated.append(l)
    if r is not None and r not in generated:
        newStates = conc(r, newStates)
        generated.append(r)
    return newStates
    # add all generated new states to unexplored list

def conc(item: T, list: List[T]):
    return list + [item]
def head(list: List[T]):
    return list[0]
def tail(list: List[T]):
    return list[1:]
def reverse(list: List[T]):
    return list[::-1]
