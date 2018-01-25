
import tensorflow as tf
M=2
N=3
x = tf.zeros([M,N],dtype=tf.int32)
y = tf.zeros_like(x,dtype=tf.float32)
with tf.Session() as sess:
    print(sess.run(fetches=[x,y]))
