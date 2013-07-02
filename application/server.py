from flask import Blueprint, render_template

app = Blueprint('main', __name__)

@app.route('/main')
def main():
    return render_template('main.html')

