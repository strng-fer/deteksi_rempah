import streamlit as st
from PIL import Image
import numpy as np
from tensorflow import keras

# Load model Keras
model = keras.models.load_model('rempah_detection_final.keras')

# Daftar kategori rempah
categories = ['adas', 'andaliman', 'asam jawa', 'bawang bombai', 'bawang merah', 'bawang putih', 'biji ketumbar',
              'bukan rempah', 'bunga lawang', 'cengkeh', 'daun jeruk', 'daun kemangi', 'daun ketumbar', 'daun salam',
              'jahe', 'jinten', 'kapulaga', 'kayu manis', 'kayu secang', 'kemiri', 'kemukus', 'kencur', 'kluwek',
              'kunyit', 'lada', 'lengkuas', 'pala', 'saffron', 'serai', 'vanili', 'wijen']

# Judul aplikasi Streamlit
st.title('Deteksi Rempah')

# Pilihan sumber gambar
source = st.radio("Sumber Gambar:", ("Upload Gambar", "Ambil Gambar"))

# Fungsi untuk melakukan deteksi objek
def deteksi_rempah(image):
    """
    Melakukan deteksi rempah pada gambar.

    Args:
        image: Gambar yang diunggah atau diambil dari kamera (objek PIL.Image).

    Returns:
        Tuple berisi string label dan confidence score.
    """
    # Preprocess image
    img = image.resize((110, 110))  # Resize ke 110x110
    img = img.img_to_array(img) # Normalisasi
    img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch

    # Prediksi
    predictions = model.predict(img)

    # Mendapatkan label dengan probabilitas tertinggi
    predicted_class = np.argmax(predictions)
    label = categories[predicted_class]
    confidence = predictions[0][predicted_class]

    return label, confidence

# Menampilkan hasil prediksi
if source == "Upload Gambar":
    # Upload gambar
    uploaded_file = st.file_uploader("Upload Gambar Rempah", type=["jpg", "jpeg", "png"])

    # Tombol prediksi
    predict_button = st.button("Prediksi")

    if uploaded_file is not None and predict_button:
        # Membaca gambar yang diupload
        image = Image.open(uploaded_file)

        # Melakukan deteksi rempah
        label, confidence = deteksi_rempah(image)

        # Menampilkan gambar di Streamlit
        st.image(image, channels="RGB")

        # Menampilkan hasil prediksi
        st.write(f"Rempah yang terdeteksi: {label} ({confidence:.2f})")

elif source == "Ambil Gambar":
    # Ambil gambar dari kamera
    camera_image = st.camera_input("Ambil Gambar Rempah")

    if camera_image is not None:
        # Membaca gambar yang diambil dari kamera
        image = Image.open(camera_image)

        # Melakukan deteksi rempah
        label, confidence = deteksi_rempah(image)

        # Menampilkan gambar di Streamlit
        st.image(image, channels="RGB")

        # Menampilkan hasil prediksi
        st.write(f"Rempah yang terdeteksi: {label} ({confidence:.2f})")
      
