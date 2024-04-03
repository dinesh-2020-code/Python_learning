from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

# create a set of odd numbers that aren't prime
# odd_not_primes = odds - primes
odd_not_primes = odds.difference(primes)  # Set difference is not commutative (A - B and B - A are two different sets)
print(odd_not_primes)
print(primes - odds)
