import tensorflow as tf
x = tf.ones([3,5],dtype=tf.float32)
y = tf.ones_like(x,dtype=tf.int64)
with tf.Session() as sess:
    print(sess.run(fetches=[x,y]))