def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,(a%b))

def lcm(a, b):
    gcd_ab = gcd(a,b)
    lcm_ab = a*b//gcd_ab
    return lcm_ab
# / -> float number

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

