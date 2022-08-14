from flask import request, make_response, abort, render_template, flash
from werkzeug.utils import secure_filename
import pathlib
from app.utils.utils import set_new_version, get_version
import os
from app import create_app

app = create_app()

BASE_DIR = pathlib.Path(__file__).resolve().parent

ALLOWED_EXTENSIONS = {'zip'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/upload/', methods=['GET'])
def upload():
    return render_template('upload.html')


@app.route('/api/uploader', methods=['POST', "GET"])
def uploader():
    if 'file' not in request.files:
        flash('No file part')
        return "dosya seç"
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return "dosya seç"
    if file and allowed_file(file.filename):
        file.filename = 'update.zip'
        filename = secure_filename(file.filename)
        if os.path.exists("./app/media/"+filename):
            os.remove("./app/media/"+filename)
        file.save("./app/media/"+filename)
        set_new_version()
        return 'Yeni versiyon başarıyla yüklendi'
    else:
        return '.zip yüklemeniz gerekmektedir!'
    return 'Hata'


@app.route("/api/update", methods=['GET'])
def download():
    version = request.args.get('version', 0)
    zip_file = open("app/media/update.zip", 'rb')
    if float(get_version()) > float(version):
        response = make_response(zip_file.read())
        response.headers.set('Content-Type', 'zip')
        response.headers.set('Content-Disposition',
                             'attachment', filename='%s.zip' % "update")

        return response
    else:
        return abort(404)



if __name__ == "__main__":
    print(BASE_DIR)
    app.run()