#Source: https://stackoverflow.com/questions/47941740/file-not-found-error-even-though-file-was-found
for root, dirs, files in os.walk(corpus_name):
    for file in files:
        if file.endswith(".v4_gold_conll"):
            f= open(file)
            lines = f.readlines()
            tokens = [line.split()[3] for line in lines if line.strip() 
and not line.startswith("#")]
    print(tokens)