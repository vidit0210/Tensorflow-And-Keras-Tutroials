#Variables
import tensorflow as tf
rand_t = tf.random_uniform(shape=[50,50],minval=8,maxval=10)
wights = tf.Variable(tf.truncated_normal(shape=[50,50],stddev=1),name="Weight1")
bias1= tf.Variable(tf.zeros([100]),name="biases")
weight2 = tf.Variable(wights.initial_value(),name='w2')
initial_op = tf.global_variables_initializer()
saver = tf.train.Saver()