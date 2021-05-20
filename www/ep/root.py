from flask import Blueprint, send_from_directory, redirect
from os import path, getcwd

bp = Blueprint('root', __name__)


@bp.route('/')
def root():
    return redirect('https://www.linkedin.com/in/caa06d9c/')


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(getcwd(), 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@bp.route("/<path:invalid_path>")
def handle_unmatchable(*args, **kwargs):
    return redirect('/')
