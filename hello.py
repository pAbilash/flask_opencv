## python -m http.server
## from the output folder to open http on 8000 port

from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import recog
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'D:\\input_folder'
app.config['OUTPUT_FOLDER'] = 'D:\\output_folder'
@app.route('/main1')
def main_page():
   return render_template('image_load1.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], 'inp.jpg'))
      #name = os.system("python recog.py")
      name = recog.identify_face()
      print(name)
      if len(name)==0:
          name="Not Able to Recognize!!"
      else:
          name='Hi '+name[0].split(':')[0]+'!'
      return render_template('image_load.html',ident=name)
      #return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(host= '0.0.0.0', debug = True)
