from flask import Blueprint, Response

bp = Blueprint('alive', __name__)


@bp.route('/', methods=['GET'])
def root():
    return Response(status=200)
