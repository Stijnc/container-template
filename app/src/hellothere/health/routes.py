from os import getenv
from flask import Blueprint, current_app, jsonify
from flask.helpers import make_response
from healthcheck import HealthCheck, EnvironmentDump
from time import time, gmtime, ctime
from datetime import datetime

health = Blueprint("health", __name__)

healthcheck = HealthCheck()
envdump = EnvironmentDump()
startTime = datetime.now()

def getUptime():
    return datetime.time() - startTime

def uptime_check():
    uptime = getUptime
    return True, 3

def links_data():
    return {"git_repo": current_app.config["GIT_REPO"]}


healthcheck.add_section("links", links_data)
healthcheck.add_section("aa", uptime_check)
healthcheck.add_check(uptime_check)

@health.route("/health", methods=["GET"])
def checkhealth():
    response = make_response(healthcheck.run())
    response.headers['content-type'] = "application/health+json"
    return response

@health.route("/env", methods=["GET"])
def checkenvironment():
    response = make_response(envdump.run())
    response.headers['content-type'] = "application/health+json"
    return response
