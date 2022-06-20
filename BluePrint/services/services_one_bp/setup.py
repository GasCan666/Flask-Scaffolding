from flask import Blueprint
from App import App

service_one_bp = Blueprint("service_one_bp", __name__,
                      url_prefix="/service_one_bp/",
                      template_folder="templates",
                      static_folder='static')


from . import sample_index


app = App.get_flask_instance()
app.register_blueprint(service_one_bp)
