import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from object_detect import ObjectDetector
from PIL import Image

UPLOAD_FOLDER = os.getcwd() + '/images/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
objectdetect = ObjectDetector()

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('analyse_file', filename=filename))
    return render_template('upload.html')

@app.route('/images/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/analyse/<filename>')
def analyse_file(filename):
    image_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image = Image.open(image_location)
    image_np = objectdetect.load_image_into_numpy_array(image)
    objects, image_analysed_np = objectdetect.detect(image_np)
    image_analysed = Image.fromarray(image_analysed_np)
    image_analysed.save(image_location, image.format)
    objects = ','.join(objects)
    os.system('say You have uploaded a lovely photo of %s ' %(objects))
    return render_template('analyse.html',
                image='/images/uploads/' + filename,
                objects=objects)

@app.route('/hello')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
