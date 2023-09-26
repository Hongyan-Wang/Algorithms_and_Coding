def fibonacci_number(n):
    if n <= 1:
        return n
    Fn = [0, 1]
    for i in range(2, n+1):
        Fn.append(Fn[-1]+Fn[-2])
    return Fn[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
