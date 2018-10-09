#coding:utf-8
import os
from flask import Flask, render_template, json, request, flash, session, abort
import mysql.connector

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host="162.241.2.133",
  user="solimpec_vini",
  passwd="08@04vithata"
)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/index')
def voltar():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)