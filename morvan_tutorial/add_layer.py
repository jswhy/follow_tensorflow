import tensorflow as tf
def add_layer(inputs, input_size, output_size, activation_func = None):
    Weights = tf.Variable(tf.random_uniform([input_size,output_size]))
    bias = tf.Variable(tf.zeros([1, output_size]) + 0.1)
    output = tf.matmul(inputs, Weights) + bias
    if activation_func == None:
        return output
    else:
        return activation_func(output)