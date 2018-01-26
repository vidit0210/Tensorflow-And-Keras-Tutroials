import tensorflow as tf
#Create two random Matrices
a= tf.Variable(tf.random_normal([4,5],stddev=2))
b= tf.Variable(tf.random_normal([4,5],stddev=2))

#Element Wise Multiplication
A= a * b

#Multiplication with a scalar of 2
B = tf.scalar_mul(2,A)

#Elemenet Division ,its result be
C= tf.div(a,b)

D=tf.mod(a,b)

init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    writer = tf.summary.FileWriter('graphs',sess.graph)
    a,b,A_R,B_R,C_R,D_R =  sess.run(fetches=[a,b,A,B,C,D])
    print("a\n",a,"\nb\n",b,"\n A*B \n",A_R)