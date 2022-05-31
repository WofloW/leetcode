# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']

        for c in s:
            res = [i + j for i in res for j in {c, c.swapcase()}]
        return res

        # for c in s:
        #     if c.isalpha():
        #         res = [i + j for i in res for j in [c.lower(), c.upper()]]
        #     else:
        #         res = [i + c for i in res]
        # return res

#         res = []
#         def dfs(i, path):
#             if i == len(s):
#                 res.append(''.join(path))
#                 return

#             if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
#                 path.append(s[i].lower())
#                 dfs(i + 1, path)
#                 path.pop()
#                 path.append(s[i].upper())
#                 dfs(i + 1, path)
#                 path.pop()
#             else:
#                 path.append(s[i])
#                 dfs(i + 1, path)
#                 path.pop()

#         dfs(0, [])
#         return res