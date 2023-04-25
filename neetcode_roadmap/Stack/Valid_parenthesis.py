#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

##very common and important question

class Solution:
    def isValid(self, s: str) -> bool:
        # verycommon
        #using stack algorithm and we'll be using hashmap
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                #checking if this char is a closing paranthesis
                if stack and stack[-1] == closeToOpen[c]:
                    #condition 1 is to check that stack is not empty
                    #condition 2 is to make sure value of opening to the closing ones
                    stack.pop()
                    #since nothing is mentioned in pop, it will remove the last element
                else:
                    #if they don't match each other or stack is empty 
                    return False

            else:
                #condition id we don't get closing paranthesis we'll get it and append it to keep moving for next value
                stack.append(c)

        return True if not stack else False
        #can only return true if stack is empty
