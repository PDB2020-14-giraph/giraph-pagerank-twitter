from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from app import app


@app.route('/uploads')
def upload_files():
   return render_template('upload.html')
	
@app.route('/uploaders', methods = ['GET', 'POST'])
def uploads_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)