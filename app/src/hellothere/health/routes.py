from datetime import datetime

from flask import Blueprint, current_app
from flask.helpers import make_response
from healthcheck import EnvironmentDump, HealthCheck

health = Blueprint("health", __name__)

healthcheck = HealthCheck()
envdump = EnvironmentDump()
startTime = datetime.now()


def getUptime():
    return datetime.time() - startTime


def links_data():
    return {"git_repo": current_app.config["GIT_REPO"]}


healthcheck.add_section("links", links_data)


@health.route("/health", methods=["GET"])
def checkhealth():
    response = make_response(healthcheck.run())
    response.headers["content-type"] = "application/health+json"
    return response


@health.route("/env", methods=["GET"])
def checkenvironment():
    response = make_response(envdump.run())
    response.headers["content-type"] = "application/health+json"
    return response
