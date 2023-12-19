# algorithms.py
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Veuillez entrer un nombre entier positif.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
