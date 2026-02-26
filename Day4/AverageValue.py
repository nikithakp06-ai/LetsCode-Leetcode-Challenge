class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total_sum = 0
        count = 0
        for n in nums:
            if n % 6 == 0:
                total_sum += n
                count += 1
        if count == 0:
            return 0

        return total_sum // count
        
