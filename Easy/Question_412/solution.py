class Solution:
     def fizzBuzz(self, n: int) -> list[str]:
         ans = []
         for i in range(1, n+1):
            K = ""
            if i % 3 == 0:
                K += "Fizz"
            if i % 5 == 0:
                K += "Buzz"
            if not K:
                K = str(i)
            ans.append(K)
         return ans
