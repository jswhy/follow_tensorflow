import tensorflow as tf

state = tf.Variable(0, name = "state")
one = tf.constant(1, name = "one")

train_step = tf.assign(state, state + one)

init = tf.global_variables_initializer()
print(state.name, train_step)
with tf.Session() as sess:
    sess.run(init)
    for i in range(10):
        print(sess.run(train_step))