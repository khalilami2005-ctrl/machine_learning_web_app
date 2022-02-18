import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import numpy as np
import requests
from PIL import Image


st.title("MNIST Digit Recognizer")

SIZE = 192

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
    img_rescaling = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
    st.write('Input Image')
    st.image(img_rescaling)

if st.button('Predict'):
    url = 'http://localhost:8000/predict/'
    # im = Image.fromarray(img)
    # im.save("your_file.png")
    data = cv2.imencode('.png', img)[1].tobytes()
    files = {'file': open('your_file.png', 'rb')}
    response = requests.post(url, files=files)
    print(response)
    try:
        data = response.json()
        print(data)
    except requests.exceptions.RequestException:
        print(response.text)
