#Source: https://stackoverflow.com/questions/62040934/flask-response-throws-filenotfounderror-even-status-of-response-is-200
@app.route("/render/<filter_name>", methods=["POST"])
def render(filter_name: str):
    if request.method == "POST":
        f = request.files["file"]

        with TemporaryDirectory() as tempdir:
            in_dir = TemporaryDirectory(dir=tempdir)
            out_dir = TemporaryDirectory(dir=tempdir)

            image = Image.open(BytesIO(f.read()))

            image.save(in_dir.name + "/image.jpg", "JPEG")

            render_mp4(in_dir.name, out_dir.name, filter_name)


            filename = "image_" + filter_name + ".mp4"

            print(filename)

            fout = open(os.path.join(out_dir.name, filename), "rb")
            print('a')
            response = make_response(fout.read())
            print('b')
            response.headers.set("Content-Type", "video/mp4")
            print('c')
            response.headers.set("Content-Disposition", "attachment", filename=filename)
            print('d')
            return response