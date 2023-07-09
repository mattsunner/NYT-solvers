"""
main.py - Entrypoint to the applciation and API

Author: Matthew Sunner, 2023
"""
import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv

from solver.bee import bee_solver

load_dotenv()

app = Flask(__name__)

# Globals
WORD_LIST = os.getenv('WORD_LIST')


# App API Routes

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Health Check Passed'})


@app.route('/solvers/bee', methods=['GET', 'POST'])
def solver_route():

    if request.method == 'GET':
        return jsonify({'message': 'GET hit; documentation and form'})
    
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

        return jsonify({'results': final_list})

if __name__ == '__main__':
    PORT = 5005
    app.run(debug=True, port=PORT)