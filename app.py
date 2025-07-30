from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "D:/SpotDLDownloads"  # Update if your folder is elsewhere

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'status': 'error', 'message': 'No URL provided'})

    try:
        result = subprocess.run(['spotdl', url], cwd=DOWNLOAD_FOLDER, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({'status': 'success', 'message': 'Download complete'})
        else:
            return jsonify({'status': 'error', 'message': result.stderr})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
