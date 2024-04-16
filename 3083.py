# Given a string s, find any
# substring
# of length 2 which is also present in the reverse of s.

# Return true if such a substring exists, and false otherwise.

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        substringExists = False
        s = list(s)
        reverse_s = list(s)
        i = len(s) - 1
        j = 0
        while i >= 0:
            reverse_s[j] = s[i]
            i -= 1
            j += 1

        print("reverse(s) = " + str(reverse_s))

        s_substrings = []
        reverse_s_substrings = []
        i = 0
        while i < len(s) - 1:
            s_substrings.append(s[i:i+2]) 
            reverse_s_substrings.append(reverse_s[i:i+2])
            i += 1
        
        print("s " + str(s_substrings))
        print("reverse_ s = " + str(reverse_s_substrings))
        temp = [x for x in s_substrings if x not in reverse_s_substrings]
        print(" temp = " + (str(temp)))
        if temp != s_substrings:
            substringExists = True
        
        print(substringExists)
        return substringExists

if __name__ == "__main__":
    mySolution = Solution()
    s = "abcd"
    mySolution.isSubstringPresent(s)