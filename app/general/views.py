import os
from flask import Blueprint, render_template


general_bp = Blueprint('general_bp', __name__, template_folder='templates', static_folder='static')


@general_bp.route('/')
def index():
    return render_template('general/home.html')


@general_bp.route('/about/')
def about():
    return render_template('general/about.html')


@general_bp.route('/contact/')
def contact():
    return render_template('general/contact.html')
