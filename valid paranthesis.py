class Solution(object):
    def isValid(self, s):
        opcl = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for i in s:
            if i in opcl.values():   
                stack.append(i)
            elif i in opcl:          
                if len(stack) == 0 or stack.pop() != opcl[i]:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    # Ask user for input
    user_input = input("Enter a string with brackets: ")
    result = sol.isValid(user_input)
    print(result)