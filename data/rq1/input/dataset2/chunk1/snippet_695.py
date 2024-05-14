#Source: https://stackoverflow.com/questions/43326698/saving-uploaded-base64-data-gives-typeerror-a-bytes-like-object-is-required-no
app = Flask(__name__)
UPLOAD_FOLDER = app.root_path + '/images/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_base = json.loads(request.form['file'])['output']['image']
        image_base = image_base[image_base.find(',')+1:]
        file_data = io.StringIO(image_base)
        file = FileStorage(file_data, filename=json.loads(from_form)['output']['name'])
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))

    return render_template('index.html', methods=['GET', 'POST'])