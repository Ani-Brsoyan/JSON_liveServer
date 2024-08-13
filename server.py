from flask import Flask, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

@app.route('/data')
def get_data():
    json_directory = '/home/ani/PlayFiles/JSandMore/multiJsonSimServer'  # Replace with your directory path
    data = []

    for file in os.listdir(json_directory):
        if file.endswith('.json'):
            file_path = os.path.join(json_directory, file)
            try:
                with open(file_path) as f:
                    file_data = json.load(f)
                    data.extend(file_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from file {file}: {e}")
            except Exception as e:
                print(f"Error reading file {file}: {e}")

    return jsonify(data)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
