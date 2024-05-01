# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# no extra space means must swap in place
# no binary search because arrys are not sorted

# THE FUCKING SOLUTION IS TO USE XOR ARE YOU FUCKING KIDDING ME

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res

        print(res)
        return res
    


if __name__ == "__main__":
    my_solution = Solution()
    test = [4,1,2,1,2]
    my_solution.singleNumber(test)