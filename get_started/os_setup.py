#just use anaconda
import tensorflow as tf
hello = tf.constant("HELLO, TENSORFLOW!")
sess = tf.Session()
print(sess.run(hello))
sess.close()
a = tf.constant(10)
b = tf.constant(20)
with tf.Session() as sess:
    print(sess.run(a + b))
