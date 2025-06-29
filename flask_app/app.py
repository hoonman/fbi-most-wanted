from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import sys
import os
from fbi_service import FBIService

app = Flask(__name__)
CORS(app)

service = FBIService()

@app.route("/")
def home():
    return render_template('dashboard.html')

@app.route("/api/most_wanted")
def list_most_wanted():
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("page_size", 20))
    filters = {}
    data, total = service.get_list(page=page, page_size=page_size, filters=filters)
    return jsonify({"results": data, "total": total})

@app.route("/api/most_wanted/<string:item_id>")
def get_details(item_id):
    details = service.get_details(item_id)
    if not details: 
        return jsonify({"error" : "Not found"}), 404
    return jsonify(details)

@app.route("/api/most_wanted/get_field_offices")
def get_field_offices():
    field_offices = service.get_field_offices()
    if not field_offices:
        return jsonify({"error": "Not found"}), 404
    return jsonify(field_offices)


if __name__ == "__main__":
    app.run(debug=True)

