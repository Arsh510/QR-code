import streamlit as st
from PIL import Image
import qrcode

st.title("QR code Genator")
st.text("Aim of this project is to whether a candidate is enter the any text to generate \nthe QR code.")

text = st.text_input('Enter the Text')

click = st.button("Click hear to Generate")


if click:

    # st.write(text)

    img = qrcode.make(text)
    image = img.save("QR.png")
    output = Image.open("QR.png")
    st.image(output)
    with open("QR.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="QR.png",
            mime="image/png"
        )
