# import numpy as np
import streamlit as st
# import PIL
from PIL import Image
import qrcode

st.title("QR code Genator")
# st.text("Aim of this project is to whether a candidate is qualified for a role based his \n or her education, experience, and other information captured on their resume.")

text = st.text_input('Enter the Text','Enter the Text')


click = st.button("Genorate")


if click:

    # st.write(text)

    img = qrcode.make(text)
    image = img.save("QR.png")
    output = Image.open("QR.png")
    st.image(output)