import tensorflow as tf
import numpy as np

print("Training MNIST model...")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, verbose=1)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc:.4f}")

weights = model.get_weights()
np.savez('mnist_weights.npz', *weights)
print(f"Saved {len(weights)} weight arrays to mnist_weights.npz")

for i, w in enumerate(weights):
    print(f"  weights[{i}]: shape={w.shape}")
