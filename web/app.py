import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
import os
import tempfile
from utils.file_parser import detect_format, extract_content
from agents.classifier_agent import ClassifierAgent
from memory.shared_memory import SharedMemory

app = Flask(__name__)
memory = SharedMemory()
classifier = ClassifierAgent(memory)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["file"]
        if file:
            temp_dir = tempfile.mkdtemp()
            filepath = os.path.join(temp_dir, file.filename)
            file.save(filepath)

            fmt = detect_format(filepath)
            content = extract_content(filepath)

            if fmt == 'Unknown' or content is None:
                result = {"error": "Unsupported or unreadable file format."}
            else:
                result = classifier.process(filepath, fmt, content)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
