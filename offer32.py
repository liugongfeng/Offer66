from functools import cmp_to_key


class Solution:
    def PrintMinNumber(self, nums):
        num = list(map(str, nums))
        num.sort(key = cmp_to_key(lambda b, a: ((a+b)<(b+a))-((a+b)>(b+a)) ))
        return ''.join(num).lstrip('0') or '0'
    





s = Solution()
res = s.PrintMinNumber([3,32,321])
print(res)