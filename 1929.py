
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        counter = 0
        ans = []

        while counter < 2:
            for i in range(0, len(nums), 1):
                ans.append(nums[i])
                if i == len(nums) - 1:
                    counter += 1
        
        return ans

if __name__ == "__main__":
    mySoloution = Solution()
    temp_list = [1,2,1]
    mySoloution.getConcatenation(temp_list)