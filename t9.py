import tensorflow as tf
x=tf.placeholder('float')
y= 2*x
data = tf.random_uniform(shape=[4,5],maxval=10)
with tf.Session() as sess:
    x_data= sess.run(data)
    print(sess.run(y,feed_dict={x:x_data}))