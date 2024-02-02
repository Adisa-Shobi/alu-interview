#!/usr/bin/python3

def rain(walls):
    '''
    Given a list of non-negative integers representing walls of
    width 1, calculate how much water will be retained after it rains.
    '''
    n = len(walls)
    if n <= 2:
        return 0
    return calculate_units(walls)


def calculate_units(walls, idx=1, units=0, pending=[]):
    '''
    Given a list of non-negative integers
    representing walls of width 1, calculate
    how much water will be retained after it rains.
    '''
    if idx == len(walls) - 1:
        return units
    depth = [walls[idx-1] - walls[idx], walls[idx+1] - walls[idx]]
    vol = min(depth)
    if vol > 0:
        return calculate_units(walls, idx+1, units+vol, pending=pending)
    elif vol == 0:
        pending.append(max(depth))
        return calculate_units(walls, idx+1, units, pending=pending)
    if pending:
        return calculate_units(
            walls,
            idx+1, units+(min(pending) * len(pending)),
            pending=[]
        )
    return calculate_units(walls, idx+1, units, pending=[])
