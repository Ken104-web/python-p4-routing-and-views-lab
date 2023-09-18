#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:integer>')
def count(integer):
    num = []
    for i in range(integer + 1):
        # append each num and in their own line using the newline character
        num.append(str(i))
        result = '\n'.join(num)
        return result

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
     answer = None

     if operation == '+':
        answer = num1 + num2
     elif operation == '-':
        answe = num1 - num2
     elif operation == '*':
        answer = num1 * num2
     elif operation == 'div':
        if num2 != 0:
            answer = num1 / num2
        else:
            return 'Not possible'
     elif operation == '%':
        answer = num1 % num2

     if answer is not None:
        return str(answer)
     else:
        return 'Invalid operation.'
    

    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
