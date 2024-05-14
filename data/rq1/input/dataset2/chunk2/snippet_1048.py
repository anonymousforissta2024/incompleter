#Source: https://stackoverflow.com/questions/52008881/flask-attributeerror-blueprint-object-has-no-attribute-response-class
@bp.route('/output_stream', methods=['GET', 'POST'])
def output_stream():
    def generate():
        if request.method == "POST":
            ...
            ...
            for line in iter(lambda: stdout.readline(2048), ""):
                data_buffer += line
                print(line, end="")
                yield line + '\n'
                if re.search(r'Done', line):
                    print('No more data')
                    break

            print('finished.')

            client.close()

    return bp.response_class(generate(), mimetype='text/plain')