import streamlit as st
import streamlit as st

# Title of the application
st.title("My Streamlit App")

# Header
st.header("Welcome to my app!")

# Subheader
st.subheader("This is a demo of Streamlit")
# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("car.jpeg")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)