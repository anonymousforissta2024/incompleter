#Source: https://stackoverflow.com/questions/61927908/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
import subprocess
import joblib

save_d2v_to_s3_current_doc2vec_model(model_doc,"doc2vec_model")

def save_d2v_to_s3_current_doc2vec_model(model,fname):
    model_name = fname
    joblib.dump(model,model_name)
    s3_base_path = 's3://sd-flikku/datalake/current_doc2vec_model'
    path = s3_base_path+'/'+model_name
    command = "aws s3 cp {} {}".format(model_name,path).split()
    print('saving...'+model_name)
    subprocess.call(command)