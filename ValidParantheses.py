# ou are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Return true if s is a valid string, and false otherwise.


class Solution:
    def isValid(self, s: str) -> bool:
        tempStack = []
        ans = False
        if len(s) == 1:
            return False
        openBracketCount = 0
        closeBracketCount = 0
        for bracket in s:
            print("bracket = " + str(bracket))
            if bracket == "(" or bracket == "{" or bracket == "[":
                print("openbracket continue")
                tempStack.append(bracket)
                openBracketCount += 1
            elif bracket == ")" or bracket == "}" or bracket == "]":
                closeBracketCount += 1
                if len(tempStack) != 0:
                    combination = tempStack.pop() + bracket
                else:
                    combination = bracket
                    ans = False

                if (combination == "()" or combination == "{}" or combination == "[]"):
                    ans = True
                    print("ans is true")
                    print("combination in answer is true : " + str(combination))

                else:
                    ans = False
                    print("ans is False")
                    print("combination in answer is False : " + str(combination))
            print("combination = " + combination)
            print("openBracketCount = " + str(openBracketCount))
            print("closeBracketCount = " + str(closeBracketCount))
            testCount = openBracketCount + closeBracketCount
            testCount = testCount % 2
            print("testCount = " + str(testCount))

            if testCount == 0:
                    
        return ans
    

if __name__ == "__main__":
    mySolution = Solution()
    input =  "({{{{}}}))"
    print(str(mySolution.isValid(input)))
