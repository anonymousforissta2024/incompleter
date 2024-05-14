#Source: https://stackoverflow.com/questions/74912686/question-about-using-multiprocessing-and-slaves-in-python-getting-error-class
def OnDownloadStudyArchive(output, uri, **request):

    # Offload the call to "SlowComputation" onto one slave process.
    # The GIL is unlocked until the slave sends its answer back.
    host = "Not Defined"
    userprofilejwt = "Not Defined"
    if "headers" in request and "host" in request['headers']:
        host = request['headers']['host']
    if "headers" in request and "userprofilejwt" in request['headers']:
        userprofilejwt = request['headers']['userprofilejwt']
    logging.info("STUDY|DOWNLOAD_ARCHIVE|ID=" + request['groups'][0] + "  HOST=" + host + "  PROFILE=  " + userprofilejwt)
    uri = uri.replace("_slave", '')
    answer = POOL.apply(DelegateStudyArchive(uri), args=(uri), kwds = {})
    pool.close()
    output.AnswerBuffer(answer, 'application/zip')

orthanc.RegisterRestCallback('/studies/(.*)/archive_slave', OnDownloadStudyArchive)