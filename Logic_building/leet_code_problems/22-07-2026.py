"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


def longest_common_prefix_string(strs: list[str]) -> str:
    if not strs:
        return ""
    else:
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix
    

x = list(input().split(','))

print(longest_common_prefix_string(x))