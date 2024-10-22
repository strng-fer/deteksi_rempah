import streamlit as st
import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load model Keras
model = keras.models.load_model('rempah_detection.keras')

# Daftar kategori rempah
categories = ['adas', 'andaliman', 'asam jawa', 'bawang bombai', 'bawang merah', 'bawang putih', 'biji ketumbar',
              'bukan rempah', 'bunga lawang', 'cengkeh', 'daun jeruk', 'daun kemangi', 'daun ketumbar', 'daun salam',
              'jahe', 'jinten', 'kapulaga', 'kayu manis', 'kayu secang', 'kemiri', 'kemukus', 'kencur', 'kluwek',
              'kunyit', 'lada', 'lengkuas', 'pala', 'saffron', 'serai', 'vanili', 'wijen']

# Judul aplikasi Streamlit
st.title('Deteksi Rempah')

# Upload gambar
uploaded_file = st.file_uploader("Upload Gambar Rempah", type=["jpg", "jpeg", "png"])

# Tombol prediksi
predict_button = st.button("Prediksi")

if uploaded_file is not None and predict_button:
    # Membaca gambar yang diupload
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Preprocess image
    img = cv2.resize(img, (110, 110))  # Resize ke 110x110
    img_array = img / 255.0  # Normalisasi
    img_array = img_array.astype('float32')
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch

    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = categories[predicted_class_index]

    # Display the results
    st.write("Predicted class:", predicted_class)

    # Display the uploaded image
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")
