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
    #First Question: What is a binary tree? what is a binary search tree? How do they differ from other tree formats?
    #A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.
    #Second Question: When do we use a binary tree? What are its advantages?
    #When a tree is well balanced, it can provide O(log n) time complexity for search, insert, and delete operations.
    #Second Question: What is the difference between a method and a function? Why do we use self here?
    def isSameTree(self, p, q):
        #First we determine if p == q
        #Third question, whats the variables of p/q referencing here? What are they?
        #Why is it different than p.val, and why would we prefer one over the other
        #Fourth Question: Why do we use == here? What is the difference between == and = ?
        if p == q:
            #Return true because we are only comparing two nodes at a given time
            return True
        #if there is no value for p OR q, and their values misalign
        #Fifth Question Why do we want to use OR for the final check though?
        if p is None or q is None or p.val != q.val:
            #We want to return false Here
            return False
        #If we call the function, the initial call will generally immediately return this call
        #Sixth Question: What is a recursive function? 
        #Why do we use it twice here?
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #Seventh Question: whats the structural difference between a method and function performing these same #actions?
    #Final Question: What is the time complexity of this algorithm? What is the space complexity?
    #The time complexity is O(n) because we are iterating through the tree once, and the space complexity is O(h) where h is the height of the tree
    #The space complexity is O(n) in the worst case, where the tree is completely unbalanced and resembles a linked list.
    #The space complexity is O(log n) in the best case, where the tree is balanced

    #def isSameTree(self, p, q):
        #return p == q if not p or not q else p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#Problem 2
class HouseRobberSolution(object):
    #First Question: What is the difference between a method and a function? Why do we use self here?
    #Second Question: What does the method rob do? What is its purpose?
    def rob(self, nums):
        #Is our list empty? If so, return 0
        if len(nums) < 0:
            return 0
        #If our list length is less than 3, it means that we can only rob one house without alerting the cops 
        if len(nums) < 3:
            #Third Question: Why do we use max here? 
            return max(nums)
        #Fourth Question: Why do we use nums[2] += nums[0] here? What is the purpose of this line?
        #If our list length is 3 or more, we can rob the first house and the third house
        nums[2] += nums[0]
        #Fifth Question: What is the purpose of the for loop here? What is it doing?
        #Sixth Question: What is the purpose of range(3, len(nums))? Why do we start at 3?
        #We are iterating through the list starting at index 3, and adding the maximum of the previous two houses to the current house
        for i in range(3, len(nums)):
            #Seventh Question: What is the purpose of nums[i] += max(nums[i - 2], nums[i - 3])?
            #We are adding the maximum of the previous two houses to the current house
            nums[i] += max(nums[i - 2], nums[i - 3])
        #Eighth Question: Why do we return max(nums[-1], nums[-2])? What is the purpose of this line?
        #We are returning the maximum of the last two houses, which is the maximum amount of money we can rob without alerting the cops
        #Ninth Question: What is the purpose of nums[-1] and nums[-2]? Why do we use negative indexing here?
        #Unlike other languages, python supports negative indexing allows us to access the last two elements of the list without knowing the length of the list
        return max(nums[-1], nums[-2])
        #Final Question: What is the time complexity of this algorithm? What is the space complexity?
        #The time complexity is O(n) because we are iterating through the list once, and the space complexity is O(1) because we are not using any extra space
#Problem 3
#First Question: What is the difference between a method and a function? Why do we use self here?
#Second Question: What does the method twoSum do? What is its purpose?
#Third Question: What is a hash table? What is its purpose?
#They have a key-value pair structure, where the key is the number and the value is the index of that number in the list.
#Theyre speed is O(1) for lookups, and they are used to store the indices of the numbers in the list.
class TwoSumSolution(object):
    def twoSum(self, nums, target):
        #Fourth Question: What is the purpose of the nums_hash dictionary? What is it doing?
        nums_hash = {}
        #Fifth Question: What is the purpose of the for loop here? What is it doing?
        #We are iterating through the entire length of the list nums
        #Sixth Question: What is the purpose of using the range function here if we already the length of our list? Why do we use it?
        for i in range(len(nums)):
            #Seventh Question: What is the purpose of the if statement here? What is it doing?
            #We are checking if the difference between the target and the current number is in the hash table
            if target - nums[i] in nums_hash:
                #Eighth Question: What is the purpose of the return statement here? What value are we returning?
                #We are returning the indices of the two numbers that add up to the target
                #Nums hash[target - nums[i]] is the index of the first number, and i is the index of the second number
                return [nums_hash[target - nums[i]], i]

#Problem 4

class DecodeStringSolution(object):
    #First Question: What is the difference between a method and a function? Why do we use self here?
    #Second Question: What does the method decodeString do? What is its purpose?
    def decodeString(self, s):
        #One benefit pof python is easily defining several variables at once
        #Third Question: What is the purpose of each variable here? What are they doing?
        stack, num, string = [], 0, ""
        #Fourth Question: What is the purpose of the for loop here? What is it doing?
        #We are iterating through the string s, and checking each character
        for i in s:
            #Fifth Question: What is the difference between if, elif, and else statements?
            #Sixth Question: What is the purpose of the if statement here? What is it doing?
            if i == "[":
                #We are pushing the current number and string onto the stack
                #Seventh Question: What is the purpose of the stack here? What is it doing?
                #The stack is used to store the current number and string when we encounter a "[" character
                #Eighth Question: What is the purpose of the num and string variables here? What are they doing?
                #The num variable is used to store a filler value, and the string variable is used to store a filler value
                stack += string,
                stack += num,
                num, string = 0, ""
            elif i == "]":
                #Ninth Question: What are pre_num and pre_string doing here? What are they referencing?
                #We are popping the last number and string from the stack
                pre_num, pre_string = stack.pop(), stack.pop()
                #Tenth Question: What is the purpose of the string variable here? What is it doing?
                #We are multiplying the current string by the last number in the stack
                #Eleventh Question: What is the purpose of the pre_num variable here? What is it doing?
                #The pre_num variable is used to store the last number in the stack, which is used to multiply the characters within current subsection of our total final string
                string = pre_string + pre_num * string
            elif i.isdigit():
                #Twelfth Question: What is the purpose of the num variable here? What is it doing?
                #We are checking if the current character is a digit, and if so, we are updating the num variable 
                num = num * 10 + int(i)
            else:
                #Thirteenth Question: What is the purpose of the string variable here? What is it doing?
                #We are adding the current character to the string variable
                string += i
        #returning the final string
        return string

