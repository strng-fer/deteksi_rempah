import streamlit as st
import cv2
from tensorflow import keras
import numpy as np

# Load model Keras
model = keras.models.load_model('rempah_detection.tflite')

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

# Fungsi untuk melakukan deteksi objek
def deteksi_rempah(image):
    """
    Melakukan deteksi rempah pada gambar.

    Args:
        image: Gambar yang diunggah.

    Returns:
        Gambar dengan label rempah yang terdeteksi dan string label.
    """
    # Preprocess image
    img = cv2.resize(image, (110, 110))  # Resize ke 110x110
    img = img / 255.0  # Normalisasi
    img = img.astype('float32')
    img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch

    # Melakukan inferensi
    predictions = model.predict(img)

    # Mendapatkan label dengan probabilitas tertinggi
    predicted_class = np.argmax(predictions)
    label = categories[predicted_class]
    confidence = predictions[0][predicted_class]

    # Menampilkan label pada gambar
    cv2.putText(image, f'{label} {confidence:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return image, label


# Menampilkan hasil prediksi
if uploaded_file is not None and predict_button:
    # Membaca gambar yang diupload
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Melakukan deteksi rempah
    image, label = deteksi_rempah(image)

    # Menampilkan gambar di Streamlit
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB")

    # Menampilkan hasil prediksi
    st.write(f"Rempah yang terdeteksi: {label}")
