import streamlit as st
import cv2
import numpy as np
import tensorflow as tf

# Load model TFLite
interpreter = tf.lite.Interpreter(model_path='rempah_detection.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

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
        image: Gambar yang diunggah atau diambil dari kamera.

    Returns:
        Gambar dengan label rempah yang terdeteksi dan string label.
    """
    # Preprocess image
    img = cv2.resize(image, (110, 110))  # Resize ke 110x110
    img = img / 255.0  # Normalisasi
    img = img.astype('float32')
    img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], img)

    # Run inference
    interpreter.invoke()

    # Get output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Mendapatkan label dengan probabilitas tertinggi
    predicted_class = np.argmax(output_data)
    label = categories[predicted_class]
    confidence = output_data[0][predicted_class]

    # Menampilkan label pada gambar
    cv2.putText(image, f'{label} {confidence:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return image, label

# Menampilkan hasil prediksi
if source == "Upload Gambar":
    # Upload gambar
    uploaded_file = st.file_uploader("Upload Gambar Rempah", type=["jpg", "jpeg", "png"])

    # Tombol prediksi
    predict_button = st.button("Prediksi")

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

elif source == "Ambil Gambar":
    # Ambil gambar dari kamera
    camera_image = st.camera_input("Ambil Gambar Rempah")

    if camera_image is not None:
        # Membaca gambar yang diambil dari kamera
        file_bytes = np.asarray(bytearray(camera_image.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Melakukan deteksi rempah
        image, label = deteksi_rempah(image)

        # Menampilkan gambar di Streamlit
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB")

        # Menampilkan hasil prediksi
        st.write(f"Rempah yang terdeteksi: {label}")
