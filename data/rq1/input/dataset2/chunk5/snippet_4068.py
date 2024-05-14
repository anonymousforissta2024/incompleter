#Source: https://stackoverflow.com/questions/54792795/tensorflow-invalid-type-error-while-defining-a-tf-constant
df = pd.read_csv(
      tf.gfile.Open("/data/historical.csv"),
      skipinitialspace=True)