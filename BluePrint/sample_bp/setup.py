from flask import Blueprint
from App import App


sample_bp = Blueprint("sample_bp", __name__,
                      url_prefix="/sample/",
                      template_folder="templates",
                      static_folder='static')


from . import sample_index


app = App.get_flask_instance()
app.register_blueprint(sample_bp)
