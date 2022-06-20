from flask import Blueprint
from App import App


service_two_bp = Blueprint("service_two_bp", __name__,
                      url_prefix="/service_two/",
                      template_folder="templates",
                      static_folder='static')


from . import sample_index


app = App.get_flask_instance()
app.register_blueprint(service_two_bp)
