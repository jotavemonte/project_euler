"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"""
analysis:
According to Euclid's lemma: any integer greater than 1 may be decomposed
into a factorization of prime numbers

So: For a number to be prime, decomposition by no prime before it returns
an integer
"""
import unittest
import time
import math


def get_primes_lower_than(number):
    def is_prime(number, primes_before):
        max_limit = math.floor(math.sqrt(number))
        for prime in primes_before:
            if number % prime == 0:
                return False
            if prime > max_limit:
                return True
        return True

    if number <= 2:
        return []

    accum = 3
    primes_before = [2]

    while accum < number:
        time_before = time.time()
        prime_bool = True
        if is_prime(accum, primes_before):
            primes_before.append(accum)
        accum += 2
    return primes_before


def first_n_primes_sum(n):
    return sum(get_primes_lower_than(n))


if __name__ == '__main__':
    start_time = time.time()
    print(first_n_primes_sum(2E6))
    elapsed_time = time.time() - start_time


class TestIsPrime(unittest.TestCase):
    def test_one(self):
        self.assertNotIn(1, get_primes_lower_than(10))

    def test_two(self):
        self.assertIn(2, get_primes_lower_than(10))

    def test_three(self):
        self.assertIn(3, get_primes_lower_than(10))

    def test_four(self):
        self.assertNotIn(4, get_primes_lower_than(10))

    def test_five(self):
        self.assertIn(5, get_primes_lower_than(10))

    def test_nine(self):
        self.assertNotIn(9, get_primes_lower_than(10))

class TestPrimeNumber(unittest.TestCase):
    def test_first_ten(self):
        self.assertEqual(first_n_primes_sum(10), 17)
