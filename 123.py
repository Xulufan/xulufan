def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def prime_sum(num: int):
    prime = []
    for i in range(num + 1):
        if isprime(i):
            prime.append(i)
    print(sum(prime))

prime_sum(100000)
