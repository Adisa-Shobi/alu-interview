#!/usr/bin/python3
'''
Solution to the rain problem
Approach: Recursion
Time complexity: O(n)
Space complexity: O(n)
'''


def rain(walls):
    '''
    Given a list of non-negative integers representing walls of
    width 1, calculate how much water will be retained after it rains.
    '''
    n = len(walls)
    l, r = [0] * (n + 1), [0] * (n + 1)
    ans = 0
    for i in range(1, len(walls) + 1):
        l[i] = max(l[i - 1], walls[i - 1])
    for i in range(len(walls) - 1, 0, -1):
        r[i] = max(r[i + 1], walls[i])
    for i in range(len(walls)):
        ans += max(0, min(l[i + 1], r[i]) - walls[i])
    return ans


# def calculate_units(walls, idx=1, units=0, pending=[]):
#     '''
#     Given a list of non-negative integers
#     representing walls of width 1, calculate
#     how much water will be retained after it rains.
#     '''
#     if idx == len(walls) - 1:
#         return units
#     left_depth = walls[idx-1] - walls[idx]
#     right_depth = walls[idx+1] - walls[idx]
#     depth = [left_depth, right_depth]
#     positive_depth = [num for num in depth if num >= 0]
#     vol = -1
#     if positive_depth:
#         vol = min(positive_depth)
#     if vol > 0:
#         return calculate_units(walls, idx+1, units+vol, pending=pending)
#     elif vol == 0 :
#         if idx == 1 and left_depth <= 0:
#             return calculate_units(walls, idx+1, units)
#         else:
#             pending.append(max(depth))
#             print(pending, idx, left_depth)
#             return calculate_units(walls, idx+1, units, pending=pending)
#     if pending:
#         return calculate_units(
#             walls,
#             idx+1,
# units+(min([num for num in pending if num != 0]) * len(pending)),
#             pending=[]
#         )
#     return calculate_units(walls, idx+1, units)
