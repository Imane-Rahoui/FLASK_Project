import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():  # put application's code here
    return(render_template('page1.html'))

@app.route('/', methods=['POST'])
def result():  # put application's code here
    algo=request.form['algo']
    print(algo)

    return(render_template('page1.html',myalgo=algo))

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()
