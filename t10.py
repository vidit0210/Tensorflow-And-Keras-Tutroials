import tensorflow as tf
import numpy as np
a = np.array([7,8,9])
b = tf.convert_to_tensor(value=a)
with tf.Session() as sess:
    print(sess.run(fetches=b))