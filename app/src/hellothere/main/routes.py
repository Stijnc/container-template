from flask import Blueprint, current_app, render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    background_color = current_app.config["BACKGROUND_COLOR"]
    color = current_app.config["COLOR"]
    name = current_app.config["NAME"]
    text = current_app.config["TEXT"]
    img_uri = current_app.config["IMG_URI"]
    return render_template(
        "index.html",
        name=name,
        text=text,
        background_color=background_color,
        color=color,
        img_uri=img_uri,
    )
