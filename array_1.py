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

#Missing numbers less than the number in the list

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d ={}
        for i,n in enumerate(temp):
            if n not in d:
                d[n] = i
        ret = []
        for i in nums:
            ret.append(d[i])

        return ret

#Minimum number of points to visit all the points
points = [[1,1],[3,4],[-1,0]]
ret = 0
x1, y1 = points.pop()  #removes last element
while points:
    x2, y2 = points.pop()
    print(x2,y2)
    ret += max(abs(y2-y1),abs(x2-x1))
    print(ret)
    x1, y1 = x2, y2
    print(x1,y1)
print(ret)
        
#plus one
""""
Key Observations:
Digits are ordered from most significant to least significant.
Example: [1, 2, 3] represents 123.
You cannot directly modify it as an integer, since the number may be very large.
Edge cases:
If the last digit is not 9, simply increment it.
If the last digit is 9, it turns into 0, and we carry 1 to the left.
If all digits are 9 (e.g., [9,9,9]), the result will have an extra digit ([1,0,0,0])."""

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):  # Traverse from right to left
            if digits[i] < 9:
                digits[i] += 1  # Increment if not 9
                return digits
            digits[i] = 0  # Set to 0 if it's 9 (carry over)
        
        return [1] + digits

digits = [1, 2, 3]
sol = Solution()
print(sol.plusOne(digits))

"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

XOR operation

5 ^ 5 = 0
5 ^ 0 = 5
"""

def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

#Roman to integer
s = "MCIIV"
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0
prev = 0

for char in reversed(s):
    curr = roman_map[char]
    if curr >= prev:
        total += curr
    else:
        total -= curr
    prev = curr

print(total)

#ISOMORPHIC Strings

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):  # Step 1: Check if lengths are different
        print(f"Lengths do not match: len(s)={len(s)}, len(t)={len(t)}")
        return False

    s_to_t = {}  # Step 2: Map s -> t
    t_to_s = {}  # Step 2: Map t -> s

    print("\nProcessing character mappings:")
    for char_s, char_t in zip(s, t):  # Step 3: Iterate through both strings
        print(f"Checking pair: ({char_s}, {char_t})")

        # Step 3.1: Check if s->t mapping is valid
        if char_s in s_to_t:
            print(f"  {char_s} is already mapped to {s_to_t[char_s]}")
            if s_to_t[char_s] != char_t:
                print(f"  Conflict! {char_s} cannot map to both {s_to_t[char_s]} and {char_t}.")
                return False

        # Step 3.2: Check if t->s mapping is valid
        if char_t in t_to_s:
            print(f"  {char_t} is already mapped to {t_to_s[char_t]}")
            if t_to_s[char_t] != char_s:
                print(f"  Conflict! {char_t} cannot map to both {t_to_s[char_t]} and {char_s}.")
                return False

        # Step 3.3: Store valid mappings
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s
        print(f"  Mapping established: {char_s} → {char_t} and {char_t} → {char_s}")

    print("\nNo conflicts found, strings are isomorphic.")
    return True  # Step 4: No conflicts found
isIsomorphic("foo", "bar")

#Word_pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in  char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
        return True

    
