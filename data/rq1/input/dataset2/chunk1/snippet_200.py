#Source: https://stackoverflow.com/questions/60146977/filenotfounderror-on-file-upload-using-flask
@jwt_required()
def post(request):
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'No file part in the request',
        }, 200
    file = request.files['file']
    if file.filename == '':
        return {
            'success': False,
            'message': 'No file selected for uploading',
        }, 200
    if file and allowed_file(file.mimetype):
        filepath = makepath(file.mimetype)
        file.save(filepath)
        post = post_repo.create(
            current_identity.id,
            request.form['matchId'],
            request.form['teamSelected'],
            request.form['content'],
            request.form['postType'],
            filepath,
            request.form['location']
        )
        if post:
            return {
                'success': True,
                'message': 'Post successfully created',
                'post': post_repo.to_dto(post),
            }, 201
    return {
        'success': False,
        'message': 'File extension not allowed',
    }, 200