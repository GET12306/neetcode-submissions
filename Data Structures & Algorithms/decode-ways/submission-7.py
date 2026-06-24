class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        print(n)
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                print('000')
            if i>=2 and (s[i-2]=='1' or (s[i-2]=='2' and s[i-1] in '0123456')):
                dp[i] += dp[i-2]
                print('111')
        
        print(dp)
        return dp[n]