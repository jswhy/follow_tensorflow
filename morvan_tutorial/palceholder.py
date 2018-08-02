import tensorflow as tf
import_1 = tf.placeholder(tf.float32)
import_2 = tf.placeholder(tf.float32)
result = tf.multiply(import_1, import_2)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    # sess.run(init)
    print(sess.run(result, feed_dict={import_1: 123.3, import_2: 2.11}))
