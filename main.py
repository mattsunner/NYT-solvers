"""
main.py - Entrypoint to the applciation and API

Author: Matthew Sunner, 2023
"""
import os

from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv

from solver.bee import bee_solver

load_dotenv()

app = Flask(__name__)

# Globals
WORD_LIST = os.getenv('WORD_LIST')
HOST = os.getenv('HOST')


# App API Routes

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/bee', methods=['GET', 'POST'])
def bee_form():
    return render_template('bee_form.html')


@app.route('/bee/results', methods=['POST'])
def bee_solver_api():
    
    if request.method == 'POST':
        letters = request.form['letters']
        golden_letter = request.form['golden_letter']

        # Clean up data passed in
        letter_list = []
        for l in letters:
            letter_list.append(l)
    
        # Solver logic
        word_list = bee_solver.word_list_generator(WORD_LIST)

        int_list = bee_solver.word_list_parser(word_list, letter_list)
        golden_list = bee_solver.golden_letter_checker(int_list, golden_letter)

        final_list = bee_solver.return_size(golden_list, 4)

        return render_template('bee_form.html', final_list=final_list)

if __name__ == '__main__':
    PORT = 5005
    app.run(debug=True, port=PORT, host=HOST)