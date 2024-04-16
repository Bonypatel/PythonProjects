# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        i = 0
        print("Input s = " + s)
        while i < len(s):
            if i+1 < len(s):
                score += abs(ord(s[i]) - ord(s[i+1]))
                i += 1
            else:
                i = len(s)

        return score
             


if __name__ == "__main__":
    mySolution = Solution()
    s = ""
    print(str(mySolution.scoreOfString(s)))