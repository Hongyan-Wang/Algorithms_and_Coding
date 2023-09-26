# Uses python3
import sys

def sum( dp, N, M ):
        return ( dp[ N-1 ] * dp[ N ] ) % M if N > 0 else 0

def fibonacci_lastD_sum( N):
    M = 10
    N += 1 # the sum of squared fibonacci numbers from 0 to N is equal to fib( N ) * fib( N+1 ), so iterate till fib( N+1 )
    dp = ( (6*M)+2 ) * [ 0 ]
    dp[ 0 ] = 0
    dp[ 1 ] = 1
    dp[ 2 ] = 1
    i = 3
    while i <= N and not ( dp[ i-2 ] == 0 and dp[ i-1 ] == 1 ):
        dp[ i ] = ( dp[ i-2 ] + dp[ i-1 ] ) % M
        i += 1
        
    P = i-2 # (P)isano period
        # case 1) (P)isano period NOT reached, return the N-th fibonacci number
        # case 2) (P)isano period reached, return (N mod P)-th fibonacci number
    ans = sum( dp, N, M ) if N <= i-1 else sum( dp, N % P, M )
    return ans


if __name__ == '__main__':
    input = sys.stdin.read();
    N= map(int, input.split())
    print(fibonacci_lastD_sum(N))
