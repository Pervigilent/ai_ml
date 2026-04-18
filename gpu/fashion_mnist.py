import tensorflow as tf
import numpy as np

# -----------------------
# 1. Load dataset
# -----------------------
fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Normalize and flatten
x_train = x_train.reshape(-1, 784).astype(np.float32) / 255.0
x_test  = x_test.reshape(-1, 784).astype(np.float32) / 255.0

# Convert labels to int32 tensors
y_train = tf.convert_to_tensor(y_train, dtype=tf.int32)
y_test  = tf.convert_to_tensor(y_test, dtype=tf.int32)

# -----------------------
# 2. Define model params
# -----------------------
input_size = 784
hidden1 = 128
hidden2 = 64
num_classes = 10

# Initialize weights
W1 = tf.Variable(tf.random.normal([input_size, hidden1], stddev=0.1))
b1 = tf.Variable(tf.zeros([hidden1]))

W2 = tf.Variable(tf.random.normal([hidden1, hidden2], stddev=0.1))
b2 = tf.Variable(tf.zeros([hidden2]))

W3 = tf.Variable(tf.random.normal([hidden2, num_classes], stddev=0.1))
b3 = tf.Variable(tf.zeros([num_classes]))

# -----------------------
# 3. Forward pass
# -----------------------
def forward(x):
    z1 = tf.matmul(x, W1) + b1
    a1 = tf.nn.relu(z1)

    z2 = tf.matmul(a1, W2) + b2
    a2 = tf.nn.relu(z2)

    logits = tf.matmul(a2, W3) + b3
    return logits

# -----------------------
# 4. Loss function
# -----------------------
def loss_fn(logits, labels):
    return tf.reduce_mean(
        tf.nn.sparse_softmax_cross_entropy_with_logits(
            labels=labels, logits=logits
        )
    )

# -----------------------
# 5. Accuracy
# -----------------------
def accuracy_fn(logits, labels):
    preds = tf.argmax(logits, axis=1, output_type=tf.int32)
    return tf.reduce_mean(tf.cast(preds == labels, tf.float32))

# -----------------------
# 6. Training loop
# -----------------------
learning_rate = 0.01
batch_size = 128
epochs = 10

train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(60000).batch(batch_size)

for epoch in range(epochs):
    epoch_loss = 0
    num_batches = 0

    for x_batch, y_batch in train_dataset:
        with tf.GradientTape() as tape:
            logits = forward(x_batch)
            loss = loss_fn(logits, y_batch)

        # Compute gradients
        grads = tape.gradient(loss, [W1, b1, W2, b2, W3, b3])

        # Gradient descent update
        W1.assign_sub(learning_rate * grads[0])
        b1.assign_sub(learning_rate * grads[1])
        W2.assign_sub(learning_rate * grads[2])
        b2.assign_sub(learning_rate * grads[3])
        W3.assign_sub(learning_rate * grads[4])
        b3.assign_sub(learning_rate * grads[5])

        epoch_loss += loss.numpy()
        num_batches += 1

    print(f"Epoch {epoch+1}, Loss: {epoch_loss / num_batches:.4f}")

# -----------------------
# 7. Evaluate
# -----------------------
test_logits = forward(x_test)
test_acc = accuracy_fn(test_logits, y_test)

print(f"Test Accuracy: {test_acc.numpy():.4f}")
