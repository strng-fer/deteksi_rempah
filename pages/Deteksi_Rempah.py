import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import cv2
import tensorflow as tf
import numpy as np

# Load model TFLite
interpreter = tf.lite.Interpreter(model_path='rempah_detection.tflite')
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Daftar kategori rempah
categories = ['adas', 'andaliman', 'asam jawa', 'bawang bombai', 'bawang merah', 'bawang putih', 'biji ketumbar',
              'bukan rempah', 'bunga lawang', 'cengkeh', 'daun jeruk', 'daun kemangi', 'daun ketumbar', 'daun salam',
              'jahe', 'jinten', 'kapulaga', 'kayu manis', 'kayu secang', 'kemiri', 'kemukus', 'kencur', 'kluwek',
              'kunyit', 'lada', 'lengkuas', 'pala', 'saffron', 'serai', 'vanili', 'wijen']

# Judul aplikasi Streamlit
st.title('Deteksi Rempah Realtime')

# Class untuk memproses video stream
class RempahDetection(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Preprocess frame
        img = cv2.resize(img, (110, 110))  # Resize ke 110x110
        img = img / 255.0  # Normalisasi
        img = img.astype('float32')
        img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch

        # Set input tensor
        interpreter.set_tensor(input_details[0]['index'], img)

        # Melakukan inferensi
        interpreter.invoke()

        # Get output tensor
        predictions = interpreter.get_tensor(output_details[0]['index'])

        # Mendapatkan label dengan probabilitas tertinggi
        predicted_class = np.argmax(predictions)
        label = categories[predicted_class]
        confidence = predictions[0][predicted_class]

        # Menampilkan label pada frame
        cv2.putText(img, f'{label} {confidence:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        return img

# Konfigurasi WebRTC 
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# Menjalankan WebRTC Streamer
webrtc_streamer(key="rempah_detection", 
                video_processor_factory=RempahDetection,
                rtc_configuration=RTC_CONFIGURATION)
cv2.putText(img, f'{label} {confidence:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
