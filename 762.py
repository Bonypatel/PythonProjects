# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a 
# prime number of set bits in their binary representation.

# Recall that the number of set bits an integer has is the number of 1's present when written in binary.

#     For example, 21 written in binary is 10101, which has 3 set bits.
from math import sqrt
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        set_bits = []

        for i in range(left, right + 1):
            binary_num = bin(i)[2:]
            set_bits.append(binary_num.count("1"))
        print(set_bits)
        for num in set_bits:
            if (Solution.is_prime(num)):
                ans += 1
        
        return ans
    
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    
if __name__ == "__main__":
    mySolution = Solution()
    left,right = 10,15
    print(mySolution.countPrimeSetBits(left,right))



