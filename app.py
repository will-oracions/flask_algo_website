from flask import Flask, render_template, request
from algorithms import calculate_factorial, is_prime, are_amicable_numbers

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
    {"num": "45", "title": "Ajout d'un élément à une position donnée dans une liste chainée"},
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
        except ValueError:
            errorMessage = 'Veuillez entrer un nombre entier positif.'

        print(errorMessage)
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
    # Ajoutez d'autres calculs d'exercices en important les fonctions nécessaires depuis algorithms.py
    return None


if __name__ == '__main__':
    app.run(debug=True)
