from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    folder = 'D:/a'  # Path to the folder containing the files
    files = os.listdir(folder)  # Get the list of files in the folder
    return render_template('index.html', files=files, get_file_size=get_file_size)

@app.route('/files/<path:filename>')
def serve_file(filename):
    folder = 'D:/a'  # Path to the folder containing the files
    return send_from_directory(folder, filename)

def get_file_size(filename):
    folder = 'D:/a'  # Path to the folder containing the files
    filepath = os.path.join(folder, filename)
    return os.path.getsize(filepath)

if __name__ == '__main__':
    app.run(debug=True)
