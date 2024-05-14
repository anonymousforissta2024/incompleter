#Source: https://stackoverflow.com/questions/54792795/tensorflow-invalid-type-error-while-defining-a-tf-constant
CONTINUOUS_COLUMNS = ["age", "id", "sessions", "amount", "averageSessionDuration", "numberOfActiveDays"]
continuous_cols = {k: tf.constant(df[k].values) for k in CONTINUOUS_COLUMNS}