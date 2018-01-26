import  tensorflow as tf
#Start an Interactive Session
sess = tf.InteractiveSession()

#Define a 5 by 5 Identity Matrix
I_matrix = tf.eye(5)
print(I_matrix.eval())

X= tf.Variable(tf.eye(10))
X.initializer.run()
print(X.eval())
#Create a Random Matrix 5 by 10
A=tf.Variable(tf.random_normal([5,10]))
A.initializer.run()

#Multiply two matrices
product = tf.matmul(A,X)
print(product.eval())

b = tf.Variable(tf.random_uniform([5,10],maxval=2,dtype=tf.int32))
b.initializer.run()
print(b.eval())
b_new = tf.cast(b,dtype=tf.float32)

t_sum = tf.add(product,b_new)
t_sub = product-b_new
print("A*X _b\n",t_sum.eval())
print("A*X -b\n",t_sub.eval())
