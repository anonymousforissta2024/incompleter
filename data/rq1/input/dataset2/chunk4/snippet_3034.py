#Source: https://stackoverflow.com/questions/63984206/tensorflow-2-3-typeerror-fetch-argument-none-has-invalid-type-class-nonetype
with tf.compat.v1.Session() as test_b:
    yolo_outputs = (tf.random.normal([19, 19, 5, 1], mean=1, stddev=4, seed = 1),
                    tf.random.normal([19, 19, 5, 2], mean=1, stddev=4, seed = 1),
                    tf.random.normal([19, 19, 5, 2], mean=1, stddev=4, seed = 1),
                    tf.random.normal([19, 19, 5, 80], mean=1, stddev=4, seed = 1))
    scores, boxes, classes = yolo_eval(yolo_outputs)
    print("scores[2] = " + str(scores[2].eval()))
    print("boxes[2] = " + str(boxes[2].eval()))
    print("classes[2] = " + str(classes[2].eval()))
    print("scores.shape = " + str(scores.eval().shape))
    print("boxes.shape = " + str(boxes.eval().shape))
    print("classes.shape = " + str(classes.eval().shape))