import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Load the saved model
model = load_model('rempah_detection.keras')

# Define a function to preprocess the uploaded image
def preprocess_image(img):
    img = img.resize((110, 110))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Define your class labels (replace with your actual labels)
categories = ['adas',
              'andaliman',
              'asam jawa',
              'bawang bombai',
              'bawang merah',
              'bawang putih',
              'biji ketumbar',
              'bukan rempah',
              'bunga lawang',
              'cengkeh',
              'daun jeruk',
              'daun kemangi',
              'daun ketumbar',
              'daun salam',
              'jahe',
              'jinten',
              'kapulaga',
              'kayu manis',
              'kayu secang',
              'kemiri',
              'kemukus',
              'kencur',
              'kluwek',
              'kunyit',
              'lada',
              'lengkuas',
              'pala',
              'saffron',
              'serai',
              'vanili',
              'wijen']

# Streamlit app
st.title("Rempah Detection App")

# Upload image through Streamlit
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image
    img_array = preprocess_image(image)

    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = categories[predicted_class_index]

    # Display the results
    st.write("Predicted class:", predicted_class)
