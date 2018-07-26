import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = 7.7 * x_data + 23.1


weights = tf.Variable(tf.random_uniform([1], -10, 10))
biases = tf.Variable(tf.zeros([1]))
y = weights * x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.6)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for _ in range(5000):
  if _ % 30 ==0:
      sess.run(train)
      print("%s steps have been done" %_,"W is:",sess.run(weights),"b is:" ,sess.run(biases))