from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    return render_template('froyo_form.html')



@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    context = {
        'flavor': users_froyo_flavor,
        'toppings': users_froyo_toppings
    }
    return render_template('froyo_results.html', **context)




@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/favorites_results')
def favorites_results():
    color = request.args.get('color')
    animal = request.args.get('animal')
    city = request.args.get('city')
    
    return f'Wow, I didn\'t know {color} {animal}s lived in {city}!'


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter your secret message: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """



@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get('message')
    sorted_message = sort_letters(message)
    
    return f"Here's your secret message!<br>{sorted_message}"



@app.route('/calculator')
def calculator():
    return render_template('calculator_form.html')


@app.route('/calculator_results')
def calculator_results():
    operand1 = int(request.args.get('operand1'))
    operand2 = int(request.args.get('operand2'))
    operation = request.args.get('operation')

    if operation == 'add':
        result = operand1 + operand2
    elif operation == 'subtract':
        result = operand1 - operand2
    elif operation == 'multiply':
        result = operand1 * operand2
    elif operation == 'divide':
        result = operand1 / operand2
    
    context = {
        'operand1': operand1,
        'operand2': operand2,
        'operation': operation,
        'result': result
    }
    
    return render_template('calculator_results.html', **context)




HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign, 'Unknown personality')
    lucky_number = random.randint(1, 99)
    
    context = {
        'name': name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality,
        'lucky_number': lucky_number
    }
    
    return render_template('horoscope_results.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=5001)