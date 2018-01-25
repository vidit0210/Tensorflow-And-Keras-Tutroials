#using Interactive Session
import tensorflow as tf
sess= tf.InteractiveSession()
v1 = tf.constant([2,3])
v2 = tf.constant([3,4])
print(sess.run(fetches=tf.add(v1,v2)))
sess.close()