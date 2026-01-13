class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        def power(base, exp):
            if exp == 0:
                return 1
            half = power(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base
        
        return power(x, n)
