from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from app import app


@app.route('/uploads')
def upload_files():
   return render_template('uploads.html')
	
@app.route('/uploaders', methods = ['GET', 'POST'])
def uploads_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template('upload-finish.html')
   
@app.route('/results')
def get_results():
   output_dict = {"id":[], "score":[]}
   my_list = []
   with open("output-twt.txt", "r") as f: 
      for line in f:
         output_dict = {}
         stripped_line = line.strip()
         line_list = stripped_line.split()
         output_dict['id'] = line_list[0]
         sub_string = line_list[1]
         output_dict['score'] = float(sub_string[0:10])
         my_list.append(output_dict)
      f.close()
      sorted_list = sorted(my_list, key = lambda i: i['score'], reverse=True)
      top_list = []
      for i in range(20):
         top_list.append(sorted_list[i])
      content = top_list

      
      return  render_template("results.html", content=content) 
		
if __name__ == '__main__':
   app.run(debug = True)