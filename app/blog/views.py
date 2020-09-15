import os
from flask import Blueprint, render_template


blog_bp = Blueprint('blog_bp', __name__, template_folder='templates', static_folder='static')


@blog_bp.route('/')
def index():
    return render_template('blog/blog.html')
