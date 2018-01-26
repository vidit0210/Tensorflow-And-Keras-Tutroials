#Logistic Regression P number of classes
#P number of Classes
m = 1000
n=15
p=2
import tensorflow as tf
X=tf.placeholder(tf.float32,name='X',shape=[m,n])
Y=tf.placeholder(tf.float32,name='Y',shape=[m,p])

w0 = tf.Variable(tf.zeros([1,p]),name='bias')
w1 = tf.Variable(tf.random_normal([n,1]),name='weights')

Y_hat = tf.matmul(X,w1)+w0

entropy = tf.nn.softmax_cross_entropy_with_logits(Y_hat,Y)
loss = tf.reduce_mean(entropy)

#Regularization Parameters-L1 Regularization
lamda=tf.constant(0.8)
regularization_param = lamda*tf.reduce_sum(tf.abs(w1))
loss += regularization_param

#L2 loss
lamda = tf.constant(0.8)
regularization_param = lamda * tf.nn.l2_loss(w1)

loss+=regularization_param