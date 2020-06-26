'''
A nice problem taken from https://leetcode.com/problems/trapping-rain-water/
We're given an array which represents surface trapping rain water.
[3, 2, 1, 3] gives something like this:

#  #
## #
####

The task is to calculate amount of water that can be trapped between the peaks.
'''

inp = [0,1,0,2,1,0,1,3,2,1,2,1]
answer = 6

def calculate_filled(heights):
    if len(heights) <= 2:
        return 0
    total = 0
    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]
    left_max[0] = heights[0]
    for i in range(1, len(heights) - 1): ## check from left to right
        left_max[i] = max(heights[i], left_max[i-1])
    right_max[-1] = heights[-1]
    for i in range(1, len(heights) - 1): ## check from right to left
        right_max[-i-1] = max(heights[-i-1], right_max[-i])
    for i in range(1, len(heights) - 1): ## calculate trapped amount
        total += min(left_max[i], right_max[i]) - heights[i]
    return total

print(calculate_filled(inp))
