from flask import Flask, render_template, request
import random
app = Flask(__name__)

facts = [
    'can guess both even and odd numbers',
    'helps in learning numbers',
    'make learning fun',
    'entertain your boring life',
    'help children learn and memorise numbers'
]
number_to_guess = random.randint(1,10)

def play(guess):
    if guess < number_to_guess:
       message = "Too low! Try again."
    elif guess > number_to_guess:
        message = "Too high! Try again."
    else:
        message = "Congratulations! You guessed it!"
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def display_game():
    return render_template('game.html')

@app.route(rule='/game', methods=['POST'])
def process_game():
    global number_to_guess
    guess = int(request.form['guess'])
    message = play(guess)
    return render_template('game.html', message=message)


@app.route('/about')
def about():
    return render_template('about.html', facts=facts)


