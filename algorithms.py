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

# Trace d'une matrice
def calculate_matrix_trace(degree, matrix):
    rows = matrix.split(';')
    elements = [list(map(int, row.split(','))) for row in rows]

    if len(elements) != degree or any(len(row) != degree for row in elements):
        raise ValueError("La matrice doit être de degré carré.")

    return sum(elements[i][i] for i in range(degree))

# Transposé
def calculate_transposed_matrix(degree, matrix):
    rows = matrix.split(';')
    elements = [list(map(int, row.split(','))) for row in rows]

    if len(elements) != degree or any(len(row) != degree for row in elements):
        raise ValueError("La matrice doit être de degré carré.")

    transposed_matrix = [[elements[j][i] for j in range(degree)] for i in range(degree)]
    return transposed_matrix

# Exercice 27
def occurrences(x, l):
    return l.count(x)

def concatener(l1, l2):
    return l1 + l2

def recherche(x, l):
    try:
        return l.index(x)
    except ValueError:
        return -1

# Exercice 31
class Runner:
    def __init__(self, number, name, time):
        self.number = number
        self.name = name
        self.time = time

def update_ranking(runners):
    sorted_runners = sorted(runners, key=lambda x: x.time)
    return [(runner.number, runner.name, runner.time) for runner in sorted_runners]

# Exercice 33: Eneo
class Client:
    def __init__(self, number, name, arrival_time):
        self.number = number
        self.name = name
        self.arrival_time = arrival_time

def add_client(queue, client):
    queue.append(client)

def serve_next_client(queue):
    if queue:
        next_client = queue.popleft()
        return f"Client {next_client.number} ({next_client.name})"
    else:
        return "Aucun client en attente"

# Exercice: 34
def evaluate_expression(expression):
    stack = []

    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, token)
            stack.append(result)

    return stack[0] if stack else None

def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ValueError("Division by zero")
    else:
        raise ValueError(f"Unsupported operator: {operator}")

# Exercice 40
def conjugate_verb(verb):
    present_conjugation = conjugate_present(verb)
    future_conjugation = conjugate_future(verb)
    return f"Au présent : {present_conjugation}, Au futur : {future_conjugation}"

def conjugate_present(verb):
    subject_pronouns = ['Je', 'Tu', 'Il/Elle/On', 'Nous', 'Vous', 'Ils/Elles']
    endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']
    conjugation = [f"{pronoun} {verb[:-2]}{end}" for pronoun, end in zip(subject_pronouns, endings)]
    return ', '.join(conjugation)

def conjugate_future(verb):
    subject_pronouns = ['Je', 'Tu', 'Il/Elle/On', 'Nous', 'Vous', 'Ils/Elles']
    endings = ['ai', 'as', 'a', 'ons', 'ez', 'ont']
    conjugation = [f"{pronoun} {verb}r{end}" for pronoun, end in zip(subject_pronouns, endings)]
    return ', '.join(conjugation)

# Exercice 41
def selection_sort(input_list):
    elements = [int(x) for x in input_list.split(',')]
    
    for i in range(len(elements)):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]
    return elements

# Exercice 42
def insertion_sort(input_list):
    elements = [int(x) for x in input_list.split(',')]

    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1

        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = key

    return elements

# Exercice 43
def bubble_sort(input_list):
    elements = [int(x) for x in input_list.split(',')]
    n = len(elements)

    for i in range(n):
        for j in range(0, n-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements

# Exercice 44
def element_at_position(input_list, position):
    elements = [int(x) for x in input_list.split()]

    if 0 <= position < len(elements):
        return elements[position]
    else:
        return None

# Exercice 45
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def add_element_at_position(head, element, position):
    new_node = Node(element)

    if position == 0:
        new_node.next = head
        return new_node

    current = head
    count = 0

    while current and count < position - 1:
        current = current.next
        count += 1

    if current:
        new_node.next = current.next
        current.next = new_node

    return head

def create_linked_list(input_list):
    elements = [int(x) for x in input_list.split()]
    head = Node(elements[0])
    current = head

    for value in elements[1:]:
        current.next = Node(value)
        current = current.next

    return head

# Exercice 46
def calculate_sparse_matrix_sum(matrix_a, matrix_b):
    # Convertir les chaînes en matrices creuses
    sparse_matrix_a = parse_sparse_matrix(matrix_a)
    sparse_matrix_b = parse_sparse_matrix(matrix_b)

    # Calculer la somme des matrices creuses
    result_matrix = add_sparse_matrices(sparse_matrix_a, sparse_matrix_b)

    # Convertir la matrice résultante en une chaîne pour l'affichage
    result_str = matrix_to_string(result_matrix)
    return result_str

def parse_sparse_matrix(matrix_str):
    rows = matrix_str.strip().split('\n')
    sparse_matrix = []
    for i, row in enumerate(rows):
        elements = row.split()
        for j, elem in enumerate(elements):
            if elem != '0':
                sparse_matrix.append((i, j, int(elem)))
    return sparse_matrix

def add_sparse_matrices(matrix_a, matrix_b):
    result_matrix = []
    combined_elements = {}
    
    for i, j, value in matrix_a + matrix_b:
        if (i, j) in combined_elements:
            combined_elements[(i, j)] += value
        else:
            combined_elements[(i, j)] = value

    for (i, j), value in combined_elements.items():
        result_matrix.append((i, j, value))

    return result_matrix

def matrix_to_string(matrix):
    max_row, max_col = max(matrix, key=lambda x: x[0])[0], max(matrix, key=lambda x: x[1])[1]
    result_str = ''
    
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            value = next((v for (r, c, v) in matrix if r == i and c == j), 0)
            result_str += f'{value} '
        result_str = result_str.rstrip() + '\n'
    
    return result_str.strip()

