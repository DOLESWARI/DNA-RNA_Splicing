import cv2
import streamlit as st
import numpy as np
from PIL import Image


def convert_to_black_and_white(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def convert_to_xray(image):
    xray_image = cv2.bitwise_not(image)
    return xray_image


def run():
    st.title("Image Converter: Black & White and X-ray Effect")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        bw_image = convert_to_black_and_white(image)
        xray_image = convert_to_xray(bw_image)

        col1, col2 = st.columns(2)

        with col1:
            st.image(bw_image, caption="Black and White Image", width=200, channels="GRAY")
        with col2:
            st.image(xray_image, caption="X-ray Image", width=200, channels="GRAY")


if __name__ == "__main__":
    run()
