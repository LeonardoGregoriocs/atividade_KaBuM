from flask import Flask

from atividade_KaBuM.application.blueprints.routes import blueprint as routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app