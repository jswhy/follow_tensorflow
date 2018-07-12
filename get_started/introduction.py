import tensorflow as tf
import numpy as np

# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype("float32")# shape is (100, 1)
y_data = x_data * 0.1 + 0.3 # shape is (100, 1)


W = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) #W shape is (1,)
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data)) # MSE mean-square error
optimizer = tf.train.GradientDescentOptimizer(0.5) # optimizer target
train = optimizer.minimize(loss) # target direction

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print("%s steps haven been done, W is: %s, b is: %s" %(step, float(sess.run(W)),  float(sess.run(b))))

sess.close()