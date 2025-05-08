from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_number():
    random_number = random.randint(1, 100)  # Generates a random integer between 1 and 100
    return render_template('index.html', number=random_number)

if __name__ == '__main__':
    app.run(debug=True)