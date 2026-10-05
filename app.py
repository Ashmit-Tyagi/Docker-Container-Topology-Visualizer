from flask import Flask, render_template, request, jsonify
import tempfile
import os

from src.parser import parse_compose_file
from src.graph_builder import build_graph


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/parse", methods=["POST"])
def parse_file():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "error": "No file was uploaded."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "Please select a Compose YAML file."
        }), 400

    if not file.filename.endswith((".yml", ".yaml")):
        return jsonify({
            "success": False,
            "error": "Please upload a .yml or .yaml file."
        }), 400

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".yml"
        ) as temp_file:

            file.save(temp_file.name)
            temp_path = temp_file.name

        services = parse_compose_file(temp_path)
        graph = build_graph(services)

        return jsonify({
            "success": True,
            "services": services,
            "graph": graph
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


if __name__ == "__main__":
    app.run(debug=True)