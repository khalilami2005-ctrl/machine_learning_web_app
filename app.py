import streamlit as st
from streamlit_drawable_canvas import st_canvas
from tensorflow import keras
import cv2
import numpy as np

st.set_page_config(page_title="MNIST Digit Recognizer", page_icon="✏️")

st.title("MNIST Digit Recognizer")
st.markdown("Draw a digit (0-9) on the canvas below and let the model predict it!")

model = keras.models.load_model('mnist.hdf5')

canvas_result = st_canvas(
    fill_color="#ffffff",
    stroke_width=10,
    stroke_color='#ffffff',
    background_color="#000000",
    height=150,
    width=150,
    drawing_mode='freedraw',
    key="canvas",
)

if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
    col1, col2 = st.columns(2)
    with col1:
        st.write("Input Image")
        img_display = cv2.resize(img, (192, 192), interpolation=cv2.INTER_NEAREST)
        st.image(img_display, clamp=True)

    if st.button('Predict'):
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pred = model.predict(img_grey.reshape(1, 28, 28, 1), verbose=0)
        result = int(np.argmax(pred[0]))
        confidence = float(np.max(pred[0]))
        with col2:
            st.write(f"## Prediction: **{result}**")
            st.write(f"Confidence: **{confidence:.2%}**")
            st.bar_chart(pred[0], height=200)
