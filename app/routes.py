#routes.py
from app import app

@app.route('/')
@app.route('/home')
def home():
	return "homepage"

@app.route('/add')
def add():
	return "add"

@app.route('/subtract')
def subtract():
	return "subtract"

@app.route('/multiply')
def multiply():
	return "multiply"

@app.route('/divide')
def divide():
	return "divide"