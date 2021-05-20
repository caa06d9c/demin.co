from flask import Blueprint, request, jsonify

bp = Blueprint('echo', __name__)


def _processing():
    reply = dict()
    for v in ['browser',
              'platform']:
        result = getattr(request.user_agent, v)

        if result:
            reply[v] = result

    reply.update(method=request.method,
                 ip=request.remote_addr,
                 host=request.host,
                 path=request.path)

    return jsonify(reply)


@bp.route('/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def root():
    return _processing()


@bp.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def catch(path):
    return _processing()
