#Adding 2 numbers
import tensorflow as tf

v1 = tf.constant([1,2,3,4])
v2 = tf.constant([5,6,7,8])
v3 = tf.add(v1,v2)
with tf.Session() as sess:
    print(sess.run(fetches=[v1,v2,v3]))