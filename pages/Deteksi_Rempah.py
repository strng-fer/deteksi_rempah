from PIL import Image
import tensorflow as tf
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
#logo = Image.open('assets/Logo.png')
st.set_page_config(
    page_title='Rempah Detection😱', 
    page_icon='😱', 
    layout='wide'
)

selected_tab = option_menu(
    menu_title=None,
    options=["Upload", "Take a Photo"],
    icons=["upload", "camera"],
    menu_icon="cast",
    default_index=0,
    key="nav", 
    orientation="horizontal"
)

# Load pre-trained Keras model
@st.cache_resource()  # Gunakan st.cache_resource() untuk model Keras
def load_model():
    try:
        model_path = r'rempah_detection_final.keras'  # Ganti dengan path model .keras Anda
        model = tf.keras.models.load_model(model_path)
        return model
    except IOError:
        st.error(f"Model tidak ditemukan di path: {model_path}")
        return None

model = load_model()

if model is None:
    st.stop()
    
    
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

# Create int_label dictionary
int_label = {i: class_name for i, class_name in enumerate(categories)}


def preprocess_image(image_path):
    """Memuat dan memproses gambar."""
    img = tf.keras.utils.load_img(image_path, target_size=(110, 110))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)   
    return img_array

def predict_uploaded_image(uploaded_file, model, transform, categories):
    """Predicts the class of an uploaded image using the provided model."""
    image = Image.open(uploaded_file).convert('RGB')  

    # Save the image to a temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        image.save(temp_file.name)
        image_path = temp_file.name

    # Now use the temporary file path for preprocessing
    image = transform(image_path)  # Preprocessing
    img_array = np.array(image)  # Convert to numpy array

    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = categories[predicted_class_index] 
    return predicted_class

if selected_tab == "Upload": 
    # Membuat form untuk upload file
    uploaded_file = st.file_uploader("Pilih gambar Anda", type=["jpg", "png", "jpeg"])

    # Memprediksi jenis batik
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Gambar yang diunggah', use_column_width=True)

        if st.button('Prediksi'):
            with st.spinner('Sedang memprediksi...'):
                predicted_class = predict_uploaded_image(uploaded_file, model, preprocess_image, int_label) 

            st.write(f'Prediksi: **{predicted_class}**')



elif selected_tab == "Take a Photo":
    # Membuat form untuk mengambil foto
    picture = st.camera_input("Ambil foto batik Anda")

    # Memprediksi jenis batik
    if picture is not None:
        image = Image.open(picture).convert('RGB')
        st.image(image, caption='Gambar yang diambil', use_column_width=True)

        if st.button('Prediksi Foto'):
            with st.spinner('Sedang memprediksi...'):
                predicted_class = predict_uploaded_image(picture, model, preprocess_image, int_label)

            st.write(f'Prediksi: **{predicted_class}**')
