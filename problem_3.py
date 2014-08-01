def prime_factors(x):

    factors = []

    while x % 2 == 0:
        factors.append(2)
        x /= 2

    i = 3
    while i * i <= x:
        while x % i == 0:
            factors.append(i)
            x /= i
        i += 2

    if x > 1:
        factors.append(x)

    return factors

number = 600851475143

primes = prime_factors(number)

print "The largest prime factor of {num} is {prime}".format(
    num=number, prime=max(primes))
