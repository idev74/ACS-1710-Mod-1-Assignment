from curses.ascii import isdigit
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):
    """Display a message to the user that changes based on their word inputs"""
    return f'The {adjective} {noun} likes to go to the market.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Displays multiplied numbers based on user input"""
    if number1.isdigit() is True and number2.isdigit() is True:
        return f'{number1} times {number2} is {int(number1) * int(number2)}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    if n.isdigit() is True:
        repeated_times = (word + ' ') * int(n)
        return(repeated_times)
    else:
       return('Invalid input. Please try again by entering a word and a number!')

@app.route('/dicegame')
def dicegame():
    roll = random.randint(1,6)
    if roll == 6:
        return f'You rolled a {roll}. You win!'
    else:
        return f'You rolled a {roll}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)

