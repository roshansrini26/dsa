#longest common prefix

from typing import Counter, List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        first = strs[0]
        last = strs[-1]

        prefix = ""

        for i in range(min(len(first),len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))

#valid parenthesis  

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
    
sol = Solution()
print(sol.isValid("(()[]{})"))

#longest valid parenthesis

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length

sol = Solution()
print(sol.longestValidParentheses(")()())"))

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

#ISOMORPHIC Strings - Tough to read

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

#Multiply strings sithout using any built-in functions

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m , n = len(num1) , len(num2)
        res = [0] * (m + n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i+j, i+j+1
                total = mul + res[pos2]

                res[pos2] = total %10
                res[pos1] += total // 10

        res_str = "".join(map(str,res)).lstrip("0")
        return res_str if res_str else "0"

sol = Solution()
print(sol.multiply("123","456"))

