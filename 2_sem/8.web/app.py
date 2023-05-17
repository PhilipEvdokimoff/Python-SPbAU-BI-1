#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_folder="static", template_folder='templates')


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/jupiter')
def jupiter():
    return render_template('jupiter.html')


# Горжусь тем, что сделал именно так, а не написал отдельный вывод для каждого блокнота!
@app.route('/jupiter/<string:notebook>')
def notebooks_pages(notebook):
    return render_template(f'notebooks_pages/{notebook}.page.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    num1 = 0
    num2 = 0
    operation = '+'
    result = None

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                result = '??? (ошибка при делении на ноль)'

    return render_template('calculator.html', num1=num1, num2=num2, operation=operation, result=result)


if __name__ == '__main__':
    app.run(debug=True)
