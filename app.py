# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 17:30:21 2025

@author: jburg
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/agradecimiento')
def agradecimiento():
    return render_template('agradecimiento.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)




