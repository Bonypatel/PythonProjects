class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()
        

        for i in range(0, len(nums)):
            if i > 0:
                if nums[i] - nums[i - 1] != 1:
                    ans = i
            if i + 1 == len(nums):
                if nums[i] != len(nums):
                    ans = len(nums)

        print(ans)
        return ans
    
if __name__ == "__main__":
    my_solution = Solution()
    test = [1, 2]
    my_solution.missingNumber(test)