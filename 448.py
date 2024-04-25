    # Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# COME BACK AND FIGURE OUT HOW TO DO IT WITH A HASHSET ITS NOT FUCKING POSSIBLE
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                ans.append(i)
        return ans
    
if __name__ == "__main__":
    my_solution = Solution()
    test = [4,3,2,7,8,2,3,1]
    my_solution.findDisappearedNumbers(test)