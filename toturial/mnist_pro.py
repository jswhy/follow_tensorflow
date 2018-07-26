import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

data_sets = input_data.read_data_sets("MNIST_data/", one_hot=True)
images_placeholder = tf.placeholder(tf.float32, shape=(None, 784))
labels_placeholder = tf.placeholder(tf.int32, shape=(None, 10))


