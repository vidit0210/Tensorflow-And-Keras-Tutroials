#Evenly Spaced Vectors:
import tensorflow as tf
#tf.linspace(start,stop,num)
#Range by which it differs : (stop - start)/(num-1)
x = tf.linspace(2.0,5.0,5.0)
with tf.Session() as sess:
    print(sess.run(x))