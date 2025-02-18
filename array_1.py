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

#enumerate - iterable values loop through
a = [1,2,3]

for i, n in enumerate(a):
    print(f"{i} : {n}")

nums = [3,0,1]
sum(range(len(nums)+1))
print(range(0,4))
sum(nums)

#Missing number
nums = [0,1]
nums = [0,1,5,2,3,8,4,6]
nums.sort()
sum(range(len(nums)+1)) - sum(nums)

#dictionary
dictionary = {
    "name" : "Rosh",
    "occupation" : "Student",
    "age" : 21
}

for k,v in dictionary.items():
    print(f"{k} : {v}")

print(dictionary["age"])

map_key = map(dictionary.get, dictionary)

#sort() and sorted()

nums = (1,4,5,8,2)
nums.sort() #only list can be sorted
sorted(nums)

#lambda function

check = lambda x: "Even" if x%2 == 0 else "Odd"

print(check(854135262))

#filter func

n = range(0,9)
even = filter(lambda x: x % 2 == 0,n)
print(list(even))

#find the missing numbers and return array

nums = [4,3,2,7,8,2,3,1]
set_nums = set(nums)
ret = []
for i in range(1,len(nums)+1):
    if i not in set_nums:
        ret.append(i)

#Two sum
#Hashmap
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            if target - v in hash_map:
                return [i, hash_map[target - v]]
            hash_map[v] = i

# Example usage
nums = [2, 7, 11, 14]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))