# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for letter in letters:
           if ord(letter) > ord(target):
               return letter
           
        return letters[0]
    

        

if __name__ == "__main__":
    my_solution = Solution()
    test = list(["c","f","j"])
    target = "a"
    print(str(my_solution.nextGreatestLetter(test, target)))
