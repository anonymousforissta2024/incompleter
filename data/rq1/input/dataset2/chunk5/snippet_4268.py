#Source: https://stackoverflow.com/questions/60412580/attributeerror-nonetype-object-has-no-attribute-read-python
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/web/predict', methods=['POST'])
def web_predict():
    image1 = request.files.get('image1').read()
    image2 = request.files.get('image2').read()

    result = process(image1, image2)
    result = Markup(json2html.convert(result))
    return render_template('index.html', result=result)