#Tnormals
import  tensorflow as tf
t_random = tf.random_normal([2,3],mean=2,stddev=2)
trun_normal = tf.truncated_normal([2,3],mean=3,stddev=1)
uniform = tf.random_uniform([2,3],maxval=4)
crop = tf.random_crop(uniform,size=[1,1])
with tf.Session() as sess:
    print(sess.run(fetches=[crop]))