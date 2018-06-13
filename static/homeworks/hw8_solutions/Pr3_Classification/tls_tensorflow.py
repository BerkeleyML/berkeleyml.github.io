import numpy as np

import tensorflow as tf

n_data = 6000
n_dim = 50

w_true = np.random.uniform(low=-2.0, high=2.0, size=[n_dim])

x_true = np.random.uniform(low=-10.0, high=10.0, size=[n_data, n_dim])
x_ob = x_true + np.random.randn(n_data, n_dim)
y_ob = x_true @ w_true + np.random.randn(n_data)

learning_rate = 0.01
training_epochs = 100
batch_size = 100


def main():
    x = tf.placeholder(tf.float32, [None, n_dim])
    y = tf.placeholder(tf.float32, [None, 1])

    w = tf.Variable(tf.random_normal([n_dim, 1]))

    sigma2 = tf.reduce_sum(tf.square(w)) + 1
    cost = batch_size * tf.log(sigma2)
    cost += 1.0 / sigma2 * tf.reduce_sum(tf.square(y - tf.matmul(x, w)))

    # Adam is a fancier version of SGD, which is insensitive to the learning
    # rate.  Try replace this with GradientDescentOptimizer and tune the
    # parameters!
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # print('optimal', sess.run(cost))
        w_sgd = sess.run(w).flatten()

        for epoch in range(training_epochs):
            avg_cost = 0.
            total_batch = int(n_data / batch_size)
            for i in range(total_batch):
                start, end = i * batch_size, (i + 1) * batch_size
                _, c = sess.run(
                    [optimizer, cost],
                    feed_dict={
                        x: x_ob[start:end, :],
                        y: y_ob[start:end, np.newaxis]
                    })
                avg_cost += c / total_batch
            w_sgd = sess.run(w).flatten()
            print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(avg_cost),
                  "|w-w_true|^2 = {:.9f}".format(np.sum((w_sgd - w_true)**2)))

    # Total learst square: SVD
    X = x_ob
    y = y_ob
    stacked_mat = np.hstack((X, y[:, np.newaxis])).astype(np.float32)
    u, s, vh = np.linalg.svd(stacked_mat)
    w_tls = -vh[-1, :-1] / vh[-1, -1]

    error = np.sum(np.square(w_tls - w_true))
    print("TLS through SVD error: {}".format(error))


if __name__ == "__main__":
    tf.set_random_seed(0)
    np.random.seed(0)
    main()
