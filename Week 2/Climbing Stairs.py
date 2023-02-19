class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = 0
		# base cases
        one = 1
        two = 2
        for i in range(3, n + 1):
            # compute number of ways for i
            ways = one+two
            # step up to i + 1   
            # 1 step below becomes 2 steps below
            # current number of ways becomes 1 step below
            two, one = ways, two
        return ways