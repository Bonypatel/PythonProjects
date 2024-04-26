# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range 
# [1, n] that do not appear in nums.

# SOLVED BY BACKTRACKING WITH SETS. TRY NOT TO BACK TRACK WITH BRUTE FORCE
# Time complexity: O(n^2)
# Space complexity: O(n2^n)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        ans_set = set(nums)
        test = set()
        
        for i in range(1, len(nums) + 1):
            test.add(i)

        test = test - ans_set

        for i in range(len(test)):
            ans.append(test.pop())

        return ans
    
if __name__ == "__main__":
    my_solution = Solution()
    test = [1,1]
    my_solution.findDisappearedNumbers(test)