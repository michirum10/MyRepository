from flask import Blueprint, render_template

main = Blueprint('main', __name__)
LoginSystem13 = Blueprint('LoginSystem13', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@LoginSystem13.route('/LoginSystem13')
def LoginSystem13():
    return render_template('LoginSystem13.html')
