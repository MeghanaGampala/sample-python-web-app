import json
import sys
import flask

python_version = sys.version
flash_version = flask.__version__


app_version = {
    "Application": {
        "name": "sample-python-web-application",
        "version": "0.0.1",

    },
    "Python": python_version,
    "Flask": flash_version
    }