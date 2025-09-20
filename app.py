import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
import cv2

# Load the trained model
model = tf.keras.models.load_model("mnist_model.h5")

st.title("🖊️ Handwritten Digit Recognition")

# Canvas for drawing
canvas = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas.image_data is not None:
    # Convert to grayscale and resize to 28x28
    img = cv2.cvtColor(canvas.image_data.astype("uint8"), cv2.COLOR_RGBA2GRAY)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Predict digit
    pred = model.predict(img)
    digit = np.argmax(pred)

    st.subheader(f"Predicted Digit: {digit}")
    st.bar_chart(pred[0])
