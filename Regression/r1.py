#Standard Regression Model
import tensorflow as tf
X=tf.placeholder(tf.float32,name="X")
Y= tf.placeholder(tf.float32,name="Y")
#Variables For Coeffients initialized to 0
w0=tf.Variable(0.0)
w1=tf.Variable(0.0)
#Linear Regression Model
Y_hat = tf.add(tf.mul(X,w1),w0)
loss = tf.square(Y-Y_hat,name='loss')