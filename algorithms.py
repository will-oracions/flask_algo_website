# factoriel
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Veuillez entrer un nombre entier positif.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
# est premier
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Copains
def are_amicable_numbers(p, q):
    return sum_of_divisors(p) == q and sum_of_divisors(q) == p

def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

# schtroumpf
def calculate_schtroumpf(array_a, array_b):
    elements_a = [int(x.strip()) for x in array_a.split(',')]
    elements_b = [int(x.strip()) for x in array_b.split(',')]

    if len(elements_a) != len(elements_b):
        raise ValueError("Les tableaux doivent avoir la même longueur.")

    return sum(a * b for a, b in zip(elements_a, elements_b))
