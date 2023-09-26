def fibonacci_last_digit(n):
    if n <= 1:
        return n
    dp = []
    dp.append(0)
    dp.append(1)
    for i in range(2, n+1):
        dp.append((dp[-1]+dp[-2])% 10) 

    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
