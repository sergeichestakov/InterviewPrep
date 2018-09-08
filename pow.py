# Implement pow() function that returns x ^ n
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if not n: # Base case: x ^ 0 is always 1
            return 1
        if n < 0: # Inverse
            return 1 / self.myPow(x, -n)

        if n % 2: # Odd
            return x * self.myPow(x, n - 1)
        else: # Even
            return self.myPow(x * x, n / 2)
