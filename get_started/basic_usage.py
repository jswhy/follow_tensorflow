import tensorflow as tf

# matrix_1 = tf.constant([[3. , 3.]]) #节点 matrix_1 constant()op
# matrix_2 = tf.constant([[2. ],[2.]]) #op matrix_2 constaht()op
# product = tf.matmul(matrix_1, matrix_2) #op matmul()op
# sess = tf.Session()
# result = sess.run([product])
# print(result)
# sess.close()
#
# sess = tf.InteractiveSession()
# x = tf.Variable([1.0, 2.0])
# a = tf.constant([3.0, 3.0])
# x.initializer.run()
# sub = tf.subtract(x, a)
# print(sub.eval())

# state = tf.Variable(0, name = 'counter')
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# init_op = tf.initialize_all_variables() #启动图后变量必须经过初始化才能生效
# with tf.Session() as sess:
#     sess.run(init_op)
#     print(sess.run(state))
#     for _ in range(3):
#         sess.run(update)
#         print(sess.run(state))

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.mul(input1, intermed)

with tf.Session() as sess:
  result = sess.run([mul, intermed])
  print(result)