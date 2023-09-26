def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    dp = ( (6*m)+2 ) * [ 0 ]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    i = 3
    while i <= n and not ( dp[ i-2 ] == 0 and dp[ i-1 ] == 1 ):
        dp[ i ] = ( dp[ i-2 ] + dp[ i-1 ] ) % m
        i += 1
    P = i-2 # (P)isano period
    # case 1) (P)isano period NOT reached, return the N-th fibonacci number
    # case 2) (P)isano period reached, return (N mod P)-th fibonacci number
    ans = dp[ n ] if n <= i-1 else dp[ n % P ]
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
