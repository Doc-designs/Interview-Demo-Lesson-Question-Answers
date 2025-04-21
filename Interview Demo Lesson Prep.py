#Problem 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SameTreeSolution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

class Solution:
    def isSameTree(self, p, q):
        return p == q if not p or not q else p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#Problem 2
class HouseRobberSolution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
class Solution:
    def rob(self, nums):
        if len(nums) <= 2: return max(nums or [0])
        nums[2] += nums[0]
        for i in range(3, len(nums)): nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])

#Problem 3
class TwoSumSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash: 
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i

#Problem 4

class DecodeStringSolution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
class Solution:
    def decodeString(self, s):
        stack, num, string = [], 0, ""
        for c in s:
            if c == "[":
                stack += string,
                stack += num,
                num, string = 0, ""
            elif c == "]":
                pre_num, pre_string = stack.pop(), stack.pop()
                string = pre_string + pre_num * string
            elif c.isdigit(): num = num * 10 + int(c)
            else: string += c
        return string