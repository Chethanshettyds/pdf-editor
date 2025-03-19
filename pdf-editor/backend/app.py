from flask import Flask, render_template, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from routes.pdf_routes import pdf_bp
from routes.editor_routes import editor_bp

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
ALLOWED_EXTENSIONS = {"pdf"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# Ensure upload directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Register Blueprints
app.register_blueprint(pdf_bp, url_prefix="/pdf")
app.register_blueprint(editor_bp, url_prefix="/editor")

@app.route('/')
def index():
    return render_template("index.html")

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
