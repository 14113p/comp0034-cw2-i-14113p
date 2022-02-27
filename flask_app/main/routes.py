from flask import Blueprint, render_template, flash
from flask_login import current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/', defaults={'name': 'Anonymous'})
@main_bp.route('/<name>')
def index(name):
    if not current_user.is_anonymous:
        name = current_user.firstname
    return render_template('index.html', title='Home page', name=name)

@main_bp.route('/<first>', defaults={'name': 'Anonymous'})
@main_bp.route('/<first>/<path:rest>', defaults={'name': 'Anonymous'})
def unknown_route(name):
    if not current_user.is_anonymous:
        name = current_user.firstname
    flash(f"The page you look for doesn't exist. Returned to the main page", 'error')
    return render_template('index.html', title='Home page', name=name)