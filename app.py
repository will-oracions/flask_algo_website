from flask import Flask, render_template, request
from collections import deque
from algorithms import *

app = Flask(__name__)

exercises = [
    {"num": "9", "title": "Calcul de 𝑛!"},
    {"num": "10", "title": "Nombre premier"},
    {"num": "11", "title": "Les copains"},
    {"num": "17", "title": "Le schtroumpf"},
    {"num": "22", "title": "Lecture et trace d'une matrice carrée"},
    {"num": "23", "title": "Matrice transposée"},
    {"num": "27", "title": "Fonctions occurrences, concatener, recherche"},
    {"num": "31", "title": "Gestion d'une course"},
    {"num": "33", "title": "File"},
    {"num": "34", "title": "Notation polonaise inversée"},
    {"num": "40", "title": "Conjugaison des verbes du premier groupe"},
    {"num": "41", "title": "Trie par sélection (tableaux et listes chainées)"},
    {"num": "42", "title": "Trie par insertion (tableaux et listes chainées)"},
    {"num": "43", "title": "Trie bulle (tableaux et listes chainées)"},
    {"num": "44", "title": "Elément à la ième position dans une liste chainée"},
    # {"num": "45", "title": "Ajout d'un élément à une position donnée dans une liste chainée"},
    {"num": "46", "title": "Matrices creuses"},
]

@app.route('/')
def index():
    return render_template('index.html', exercises=exercises)

@app.route('/exercice/<num>')
def show_exercice(num):
    return render_template('exercice.html', num=num, exercises=exercises)

@app.route('/exercice/<int:num>', methods=['POST'])
def exercice(num):
    result = None
    errorMessage = ''
    if request.method == 'POST':
        try:
            result = calculate_exercice(num, request.form)
        except ValueError as error:
            errorMessage = str(error)
    return render_template(f'exercice.html', errorMessage=errorMessage, input=request.form, num=str(num), result=result, exercises=exercises)

def calculate_exercice(num, form):
    if num == 9:
        n = int(form['numberInput'])
        return calculate_factorial(n)
    
    if num == 10:
        n = int(form['numberInput'])
        return is_prime(n)
    
    if num == 11:
        p = int(form['numberP'])
        q = int(form['numberQ'])
        return are_amicable_numbers(p, q)
    
    if num == 17:
        arr1 = form['arrayA']
        arr2 = form['arrayB']
        return calculate_schtroumpf(arr1, arr2)
    
    if num == 22:
        degree = int(form['degree'])
        matrix = form['matrix']
        return calculate_matrix_trace(degree, matrix)
    
    if num == 23:
        degree = int(form['degree'])
        matrix = form['matrix']
        return calculate_transposed_matrix(degree, matrix)
    
    if num == 27:
        list1 = form['list1']
        list2 = form['list2']
        element = form['element']
        # return calculate_transposed_matrix(degree, matrix)
        return '--'
    
    if num == 31:
        runners = []

        runner_number = form['runner_number']
        runner_name = form['runner_name']
        runner_time = form['runner_time']

        new_runner = Runner(runner_number, runner_name, runner_time)
        runners.append(new_runner)

        # return update_ranking(runners)
        return '--'

    if num == 33:
        client_queue = deque()

        client_number = int(form['client_number'])
        client_name = form['client_name']
        arrival_time = form['arrival_time']

        new_client = Client(client_number, client_name, arrival_time)
        add_client(client_queue, new_client)

        next_client = serve_next_client(client_queue)
        return next_client

    if num == 34:
        expression = request.form['expression']
        return evaluate_expression(expression)

    if num == 40:
        verb = request.form['verb']
        return conjugate_verb(verb)

    if num == 41:
        input_list = request.form['input_list']
        return selection_sort(input_list)

    if num == 42:
        input_list = request.form['input_list']
        return insertion_sort(input_list)
    if num == 43:
        input_list = request.form['input_list']
        return bubble_sort(input_list)
    if num == 44:
        input_list = request.form['input_list']
        position = int(request.form['position'])
        return element_at_position(input_list, position)
    
    if num == 45:
        input_list = request.form['input_list']
        element = int(request.form['element'])
        position = int(request.form['position'])
        linked_list = create_linked_list(input_list)
        return add_element_at_position(linked_list, element, position)

    if num == 46:
        matrix_a = request.form['matrix_a']
        matrix_b = request.form['matrix_b']
        return calculate_sparse_matrix_sum(matrix_a, matrix_b)

    return None


if __name__ == '__main__':
    app.run(debug=True)
