def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def binary_palindrome(num):
    binary = bin(num)[2:]
    return binary == binary[::-1]

def prime_binary_palindromes(n):
    result = []
    for i in range(2, n + 1):
        if is_prime(i) and binary_palindrome(i):
            result.append(i)
    return result 

n = int(input("vvedite chislo: "))
print(prime_binary_palindromes(n))