from .setup import service_two_bp
from flask import render_template
from .PageMap import PageMap
from flask import request
from .FuncSample import FuncSample


@service_two_bp.route("/")
def get_news():
    print("requests received")
    return render_template(PageMap.index_html)


@service_two_bp.route("/getTime", methods=["POST"])
def get_time():
    requestor = request.form.get("name")
    return requestor + ":" + FuncSample.get_time()
