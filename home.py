import streamlit as st
import cv2
import tensorflow as tf
import numpy as np

# Load model TensorFlow Lite
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
st.title('Deteksi Rempah Realtime')

# Inisialisasi kamera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Gunakan kamera default (0)

# Fungsi untuk melakukan deteksi objek
def deteksi_rempah(frame):
    """
    Melakukan deteksi rempah pada frame gambar.

    Args:
      frame: Frame gambar dari kamera.

    Returns:
      Frame gambar dengan label rempah yang terdeteksi.
    """
    # Preprocess frame
    img = cv2.resize(frame, (110, 110))  # Resize ke 110x110
    img = img / 255.0  # Normalisasi
    img = img.astype('float32')
    img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], img)

    # Run inference
    interpreter.invoke()

    # Get output tensor
    predictions = interpreter.get_tensor(output_details[0]['index'])

    # Mendapatkan label dengan probabilitas tertinggi
    predicted_class = np.argmax(predictions)
    label = categories[predicted_class]
    confidence = predictions[0][predicted_class]

    # Menampilkan label pada frame
    cv2.putText(frame, f'{label} {confidence:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

# Menampilkan video secara realtime
frame_placeholder = st.empty()  # Placeholder untuk menampilkan frame

while(True):
    # Membaca frame dari kamera
    ret, frame = cap.read()

    # Memeriksa apakah frame kosong
    if not ret:
        st.error("Gagal mengambil gambar dari kamera.")
        continue  # Lewati iterasi loop saat ini jika frame kosong

    # Melakukan deteksi rempah
    frame = deteksi_rempah(frame)

    # Menampilkan frame di Streamlit
    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

# Membersihkan resource setelah selesai
cap.release()
