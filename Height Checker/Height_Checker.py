# 1051. Height Checker

# Students are asked to stand in non-decreasing 
# order of heights for an annual photo.

# Return the minimum number of students not 
# standing in the right positions. (This is the 
# number of students that must move in order for 
# all students to be standing in non-decreasing 
# order of height).

# EXAMPLE 1
# Input: [1,1,4,2,1,3]
# 1, 1, 1, 2, 3, 4
# Output: 3
# Explanation: 
# Students with heights 4, 3 and the last 1 are 
# not standing in the right positions.

class Solution(object):
    def heightChecker(self, heights):
        n = len(heights)
        lis = sorted(heights)

        x = 0
        for i in range(n):
            if heights[i] != lis[i]:
                x+=1
        return x

    heights = [1,1,4,2,1,3,4,2,1]
    print(heightChecker(object, heights))