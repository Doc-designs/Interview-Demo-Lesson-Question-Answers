#Problem 1
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSameTree(self, p, q):
        #This Function will be acting recursively to verify the Tree Values
        if (self != p or self != q) and p != q:
            print("Recursive Call")
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p == q:
            return True
        else:
            return False

    #def isSameTree(self, p, q):
        #return p == q if not p or not q else p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#Problem 2
class HouseRobberSolution(object):
    def rob(self, nums):
         if len(nums) < 0:
             return max([0])
         if len(nums) < 3:
             return max(nums):
         nums[2] += nums[0]
         for i in range(3, len(nums)): nums[i] += max(nums[i - 2], nums[i - 3])
            return max(nums[-1], nums[-2])
        
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

def main():
    # Example usage of the solutions
    # Problem 1: Same Tree
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    treeNode = TreeNode()
    print(treeNode.isSameTree(p, q))  # Output: True

    # Problem 2: House Robber
    nums = [2, 7, 9, 3, 1]
    house_robber_solution = HouseRobberSolution()
    print(house_robber_solution.rob(nums))  # Output: 12

    # Problem 3: Two Sum
    nums = [2, 7, 11, 15]
    target = 9
    two_sum_solution = TwoSumSolution()
    print(two_sum_solution.twoSum(nums, target))  # Output: [0, 1]

    # Problem 4: Decode String
    s = "3[a2[c]]"
    decode_string_solution = DecodeStringSolution()
    print(decode_string_solution.decodeString(s))  # Output: "accaccacc"

if __name__ == "__main__":
    main()
