import tensorflow as tf
state = tf.Variable(0, name="state")
# print(state.name)
one = tf.constant(1, name="one")
result = state + one
step = tf.assign(state, result)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        print(sess.run(step))