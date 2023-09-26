def sum(dp, N, M):
    ans = 0
    for i in range(0, N+1):
        ans += dp[i]
        ans%= M
    return ans

def fibonacci_sum(N):
    M = 10
    dp = ((6*M)+2)*[0]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    i = 3
    while i <= N and not (dp[i-2] == 0 and dp[i-1] == 1):
        dp[i] = (dp[i-2] +dp[i-1])%M
        i = i+1
    P = i-2
    ans = sum(dp, N, M) if N<= i-1 else sum(dp, N%P, M)
    return ans 


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
