#!/usr/bin/env python3
from flask import Flask, request
from src.controllers import *
import json
from flask_cors import CORS
from html import unescape
import requests
import time


from flask import Flask
from src.controllers import process_image_controller

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024


@app.route("/api/process-image-file", methods=["POST"])
def process_raw_image():
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.data.decode("utf-8"))
            file_name = data["file"]
            result = process_image_controller(file_name)
            return result
        else:
            return {"response": "not json structure"}
    else:
        return {"response": "not post structure"}


@app.route("/api/process-regions", methods=["POST"])
def process_region_image():
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.data.decode("utf-8"))
            file_name = data["file"]
            result = process_regions_controller(file_name)
            return result
        else:
            return {"response": "not json structure"}
    else:
        return {"response": "not post structure"}


@app.route("/api/process_image", methods=["POST"])
def process_image():
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.data.decode("utf-8"))
            base64_image = data["base64image"]
            result = process_image_controller(base64_image)

            return {"base64image": result["base64image"]}
        else:
            return {"response": "not json structure"}
    else:
        return {"response": "not post structure"}


@app.route("/api/compute_pixels", methods=["POST"])
def compute_pixels():
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.data.decode("utf-8"))
            base64_image = data["base64image"]
            result = process_image_controller(base64_image)

            return {"num_pixel": result["num_pixel"]}
        else:
            return {"response": "not json structure"}
    else:
        return {"response": "not post structure"}


@app.route("/api/convert_image", methods=["POST"])
def convert_image2base64():
    if request.method == "POST":
        if "multipart/form-data" in request.content_type:
            image_file = request.files.get("file")
            image_data = load_image(image_file=image_file)
            result = convert_image_controller(image_data)

            return result
        else:
            return {"response": "not file image structure"}
    else:
        return {"response": "not post structure"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
