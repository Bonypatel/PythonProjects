class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ans = Solution.binary_search(nums, 0, len(nums), target)

        return ans

    def binary_search(nums, min, max, x):
        if max >= min:
            mid = max + min // 2
            if mid == max == min:
                if x > nums[len(nums) - 1]:
                    return -1

            if nums[mid] == x:
                return mid
            elif nums[mid] > x:
                return Solution.binary_search(nums, min, mid - 1, x)
            elif nums[mid] < x:
                return Solution.binary_search(nums, mid + 1, max, x)
        else:
            return -1
    


if __name__ == "__main__":
    mySolution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    mySolution.search(nums, target)