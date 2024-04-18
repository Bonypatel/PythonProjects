# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = False
        nums.sort()
        test = nums[0]
        ans = False
        for i in range(1, len(nums), 1):
            if nums[i] == test:
                ans = True
            else:
                test = nums[i]
                    
        return ans
    
if __name__ == "__main__":
    my_solution = Solution()
    test = [1, 2, 3, 1]
    my_solution.containsDuplicate(test)

# Slow as shit but didnt use a lot of memory :)