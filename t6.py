import tensorflow as tf
range_t = tf.range(start=4,limit=100,delta=2)
with tf.Session() as sess:
    print(sess.run(range_t))