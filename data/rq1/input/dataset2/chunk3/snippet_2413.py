#Source: https://stackoverflow.com/questions/61927908/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
model = load_d2v("doc2vec_model")

def load_d2v(fname):
    model_name = fname
    s3_base_path='s3://sd-flikku/datalake/current_doc2vec_model'
    path = s3_base_path+'/'+model_name  
    command = "aws s3 cp {} {}".format(path,model_name).split()
    print('loading...'+model_name)
    subprocess.call(command)
    model=joblib.load(model_name)
    return model