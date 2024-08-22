#!/usr/bin/env python
import logging
import sys
import os
from flask import Flask, request
from pathlib import Path
from beamline_setup import BeamlineSetup
from conf_writer import write_config_files


log = logging.getLogger(__name__)


app = Flask(__name__, static_folder="./ui/build", static_url_path="")
app.config.from_object("settings")


beamline_setup = BeamlineSetup()


def setup_logging():
    # write log to stdout
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        # timestamps in ISO 8601 format
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )


def get_mxcube_config_dir() -> Path:
    return Path(app.config["MXCUBE_CONFIG_DIR"])


def get_mxcube_restart_command() -> str:
    return Path(app.config["MXCUBE_RESTART_COMMAND"])


def restart_mxcube():
    restart_command = get_mxcube_restart_command()
    log.info(f"restarting MXCuBE with '{restart_command}' command")
    res = os.system(restart_command)
    if res == 0:
        log.info(f"restarted MXCuBE successfully")
    else:
        log.info(f"error restarting MXCuBE, exit status: {res}")


@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/api/config", methods=["GET"])
def get_config():
    return beamline_setup.dict()


@app.route("/api/config", methods=["POST"])
def apply_config():
    global beamline_setup
    beamline_setup = BeamlineSetup(**request.get_json())

    write_config_files(get_mxcube_config_dir(), beamline_setup)
    restart_mxcube()

    return "ok"


setup_logging()
