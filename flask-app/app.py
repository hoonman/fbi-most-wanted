from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import sys
import os
from fbi_service import FBIService
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'python-scripts'))

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



if __name__ == "__main__":
    app.run()


# follow this guide: https://chatgpt.com/share/6858f35d-bbb8-8007-a345-2edf81f7b629