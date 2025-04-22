#Problem 1
# Definition for a binary search tree(BST) node. A BST unlike other
#Data Tree Formats only has two Children nodes per Node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #Definition for a binary tree node.
    #class TreeNode(object):
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    #Review of Python Syntax
    #Classes are a collection of code grouped together under the umberlla of a shared name
    #Python has both Methods & Functions as a part of its codebase
    #Methods use the dot notation which might be like adding something to a list, ie, listname.append(5)
    #Functions however are called individually with parameters and no specific object references len(listname)
    #One of the benefits of python classes is that they can accept parameters, and they have a special function
    #The __init__() method allows us to define an unspecified value for the parameter of self
    #This allows us to designate something a method rather than a function, using self as a reference to
    #you guessed it! its self!!!
    #This Function will be acting recursively to verify the Tree Values
    #Whats a tree(BST)? a tree is a type of list recognizable by its unique
    #structure, as it relies on a linked list structure(Which means that you can
    #Navigate relative to a node position). The distinction however from
    #other collection formats is that it places on emphasis on dual branches to
    #the other nodes. there are other formats of BST's, like a splay tree, that
    #make use of the most recently referenced values to shift around its order.
    def isSameTree(self, p, q):
        #First we determine if p == q
        #First question, whats the variables of p/q referencing here?
        #Why is it different than p.val, and why would we prefer one over the other
        if p == q:
            #Return true because we are only comparing two nodes at a given time
            return True
        #if there is no value for p OR q, and their values misalign
        #Second Question Why do we want to use OR for the final check though?
        if p is None or q is None or p.val != q.val:
            #We want to return false Here
            return False
        #If we call the function, the initial call will generally immediately return this call
        #Third Question: What is a recursive function? 
        #Why do we use it twice here?
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #Final Question: whats the structural difference between a method and function performing these same #actions?

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
