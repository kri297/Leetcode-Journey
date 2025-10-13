class Solution:
    def reverse(self, num: int) -> int:
        def kri(n: int) -> int:
            return n if n >= 0 else -n

        sign = -1 if num < 0 else 1
        num = kri(num) 
        rev = 0

        while num:
            rev = rev * 10 + num % 10
            num //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
