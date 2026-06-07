import tf2onnx
import tensorflow as tf

print("Loading MNIST model...")
model = tf.keras.models.load_model('mnist.hdf5')
print("Model loaded!")

spec = (tf.TensorSpec((None, 28, 28, 1), tf.float32, name='input'),)
output_path = 'mnist.onnx'

print("Converting to ONNX...")
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, output_path=output_path)
print(f'ONNX model saved to {output_path}')
