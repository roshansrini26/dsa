#Contains duplicate values
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))
