from flask import Flask

UPLOAD_FOLDER = "D:\Kuliah\PDB\giraph-pagerank-twitter\\upload-api"

app = Flask(__name__,  template_folder='templates')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024