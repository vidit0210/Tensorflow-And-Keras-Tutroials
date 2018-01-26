#multiple Regresssion
#Input are many but many output
m=1000
n=15
P=2
import tensorflow as tf
X= tf.placeholder(tf.float32,name="X",shape=[m,n])
Y=tf.placeholder(tf.float32,name='Y')

w0 = tf.Variable(0.0)
w1 = tf.Variable(0.0)

Y_hat= tf.matmul(X,w1)+w0

loss = tf.reduce_mean(tf.square(Y-Y_hat,),name='loss')

