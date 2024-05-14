#Source: https://stackoverflow.com/questions/62040934/flask-response-throws-filenotfounderror-even-status-of-response-is-200
@app.route("/render/<filter_name>", methods=["POST"])
def render(filter_name: str):
    if request.method == "POST":
        f = request.files["file"]

        tempdir = tempfile.mkdtemp()
        in_dir = tempfile.mkdtemp(prefix="image_", dir=tempdir)
        out_dir = tempfile.mkdtemp(prefix="image_", dir=tempdir)

        image = Image.open(BytesIO(f.read()))
        image.save(in_dir.name + "/image.jpg", "JPEG")

        render_mp4(in_dir.name, out_dir.name, filter_name)

        filename = "image_" + filter_name + ".mp4"
        fout = open(os.path.join(out_dir.name, filename), "rb")

        response = make_response(fout.read())
        response.headers.set("Content-Type", "video/mp4")
        response.headers.set("Content-Disposition", "attachment", filename=filename)
        shutil.rmtree(tempdir)

        return response