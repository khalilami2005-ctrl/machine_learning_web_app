from fastapi import FastAPI, File, UploadFile, Form
from streamlit_drawable_canvas import st_canvas
from tensorflow import keras
import cv2
from cv2 import *
import numpy as np
import io
import base64
import uvicorn



app = FastAPI(debug=True)

model_new = keras.models.load_model('mnist.hdf5')

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    contents = await image.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pred = model_new.predict(img_grey.reshape(1, 28, 28, 1))
    return {"result": float(np.argmax(pred[0])), "percent": pred[0].tolist()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)