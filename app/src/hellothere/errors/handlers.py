from flask import Blueprint, current_app
from flask.templating import render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return (
        render_template(
            "errors/404.html",
            background_color=current_app.config["BACKGROUND_COLOR"],
            color=current_app.config["COLOR"],
            name=current_app.config["NAME"],
        ),
        404,
    )


@errors.app_errorhandler(500)
def error_505(error):
    return (
        render_template(
            "errors/500.html",
            background_color=current_app.config["BACKGROUND_COLOR"],
            color=current_app.config["COLOR"],
            name=current_app.config["NAME"],
        ),
        500,
    )
