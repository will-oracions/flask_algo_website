# algorithms.py
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Veuillez entrer un nombre entier positif.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Ajoutez ici d'autres fonctions d'algorithme au besoin
