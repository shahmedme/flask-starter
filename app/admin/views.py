import os
from flask import Blueprint, render_template


admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


@admin_bp.route('/')
def index():
    return render_template('admin/dashboard.html')

@admin_bp.route('/users/')
def users():
    return render_template('admin/users.html')
