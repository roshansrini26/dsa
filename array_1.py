#Contains duplicate values
from typing import Counter, List

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

#Intger to roman

def intToRoman(self, num: int) -> str:
        roman_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        res = ""

        for val, symbol in roman_map:
            while num >= val:
                res += symbol
                num -= val
        return res 

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


#rotate array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def rev(start,end):
            while start < end:
                nums[start] , nums[end] = nums[end] , nums[start]
                start += 1
                end -= 1
        
        rev(0,n-1)

        rev(0,k-1)

        rev(k,n-1)

nums = [4,5,6,8,9,7,1,2]
sol = Solution()
sol.rotate(nums,3)
print(nums)

#intersection of array:
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_map = {}
        res = []

        for num in nums1:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        for num in nums2:
            if num in count_map and count_map[num] >0:
                res.append(num)
                count_map[num] -= 1
        return res

#add binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2::] # bin will return 0b100 so slice [2::]

sol = Solution()
res = sol.addBinary("1101","1100")
print(int(res,2))

# Generate parnathesis

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        def backtrack(open, close):
            if len(sol) == 2*n:
                res.append(''.join(sol))

            if open < n:
                sol.append('(')
                backtrack(open + 1, close)
                sol.pop()

            if open > close:
                sol.append(')')
                backtrack(open, close + 1)
                sol.pop()

        backtrack(0,0)
        return res

#valid anagram in a string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)  #counter to p
        s_count = Counter(s[:len(p)-1]) #counter to s with 1 less than element

        res = []

        for i in range(len(p)-1,len(s)):
            s_count[s[i]] += 1  # add the coming element to s_count

            if s_count == p_count:  #check both is same values append to result
                res.append(i-len(p)+1)

            s_count[s[i-len(p)+1]] -= 1  #remove the count for the left most index in s_count
            if s_count[s[i-len(p)+1]] == 0:  #if the value of the element is zero delete the element
                del s_count[s[i-len(p)+1]]
        return res

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
print(sol.findAnagrams("abab", "ab"))

#find sqrt without built in function

class Solution: #binary search
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x
        left = 0
        right = x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans