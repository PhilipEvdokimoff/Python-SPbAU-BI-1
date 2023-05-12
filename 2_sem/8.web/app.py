#!/usr/bin/env python3

from flask import Flask, render_template, url_for

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


if __name__ == '__main__':
    app.run(debug=True)
