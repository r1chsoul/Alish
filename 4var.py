def gcd(a, b): a if b == 0 else gcd(b, a % b)
a, b, c, d = map(int, input().split())
print(a * d // gcd(a * d, b * c), '/', b * c // gcd(a * d, b * c))