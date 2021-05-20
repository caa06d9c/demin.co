import logging

from flask import Flask
from importlib import import_module
from logging import DEBUG, INFO
from os import path, listdir
from paste.translogger import TransLogger


app = Flask(__name__)
logger = logging.getLogger('waitress')

if app.debug:
    app.logger.setLevel(DEBUG)
else:
    logger.setLevel(INFO)

with app.app_context():
    for endpoint in listdir(path.join(app.root_path, 'ep')):
        if endpoint in ['__pycache__']:
            continue

        module_name = f"www.ep.{endpoint}"[:-3]
        module = import_module(module_name)

        bp = getattr(module, 'bp')
        url_prefix = f"/{endpoint[:-3]}"

        if url_prefix == '/root':
            app.register_blueprint(blueprint=bp, url_prefix='/')
        else:
            app.register_blueprint(blueprint=bp, url_prefix=url_prefix)

if app.env == 'dev':
    app.run(use_reloader=False, host='127.0.0.1')
else:
    from waitress import serve
    serve(TransLogger(app, setup_console_handler=False), host="0.0.0.0", port=80)
