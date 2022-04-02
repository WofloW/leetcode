
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]

        # a = list(a)
        # b = list(b)
        # carry = 0
        #
        # res = ''
        # while a or b or carry:
        #     s = (int(a.pop()) if a else 0) + (int(b.pop()) if b else 0) + carry
        #
        #     res += str(s & 1)
        #     carry = s >> 1
        # return res[::-1]

        a_len, b_len = -len(a), -len(b)
        carry = 0
        i = -1
        res = ''
        while i >= a_len or i >= b_len or carry:
            s = (int(a[i]) if i >= a_len else 0) + (int(b[i]) if i >= b_len else 0) + carry
            res = str(s & 1) + res
            carry = s >> 1
            i -= 1
        return res



