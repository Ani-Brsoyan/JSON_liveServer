from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/data')
def get_data():
    # This function returns the JSON data from the file
    with open('data.json') as f:
        data = f.read()
    return data

@app.route('/')
def serve_index():
    # This function serves the index.html file
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # This function serves any other static files like CSS
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
