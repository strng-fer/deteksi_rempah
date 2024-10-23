import streamlit as st
from PIL import Image

# Daftar kategori rempah-rempah
categories = ['Adas', 'Andaliman', 'Asam Jawa', 'Bawang Bombai', 'Bawang Merah', 'Bawang Putih', 'Biji Ketumbar', 
              'Bukan Rempah', 'Bunga Lawang', 'Cengkeh', 'Daun Jeruk', 'Daun Kemangi', 'Daun Ketumbar', 'Daun Salam', 
              'Jahe', 'Jinten', 'Kapulaga', 'Kayu Manis', 'Kayu Secang', 'Kemiri', 'Kemukus', 'Kencur', 'Kluwek', 
              'Kunyit', 'Lada', 'Lengkuas', 'Pala', 'Saffron', 'Serai', 'Vanili', 'Wijen']

# Informasi singkat tentang beberapa rempah
info_rempah = {
    'Adas': 'Adas adalah tanaman herbal dengan rasa yang sedikit manis, sering digunakan dalam masakan dan sebagai obat herbal.',
    'Andaliman': 'Andaliman dikenal sebagai "lada Batak", memberikan rasa pedas dan sensasi kebas pada masakan.',
    'Asam Jawa': 'Asam Jawa memiliki rasa asam dan manis, sering digunakan dalam masakan Asia Tenggara untuk menambah rasa segar.',
    'Bawang Bombai': 'Bawang bombai memiliki rasa yang lebih manis dan lembut dibandingkan bawang merah, sering digunakan untuk tumisan.',
    'Bawang Merah': 'Bawang merah adalah bumbu dasar banyak masakan Indonesia, dengan rasa yang tajam dan sedikit manis.',
    'Jahe': 'Jahe adalah rempah dengan rasa pedas dan sedikit manis, sering digunakan dalam minuman dan masakan untuk menghangatkan tubuh.',
    'Bawang Putih': 'Bawang putih memiliki aroma dan rasa yang kuat, sering digunakan sebagai bumbu dasar dalam berbagai masakan.',
    'Biji Ketumbar': 'Biji ketumbar memiliki aroma yang khas dan rasa yang sedikit manis, sering digunakan dalam masakan kari dan bubuk rempah.', 
    'Bunga Lawang': 'Bunga lawang memiliki aroma yang kuat dan rasa yang sedikit manis, sering digunakan dalam masakan Cina dan Vietnam.',
    'Cengkeh': 'Cengkeh memiliki aroma yang kuat dan rasa yang pedas, sering digunakan dalam masakan Indonesia dan sebagai bahan pengobatan tradisional.',
    'Daun Jeruk': 'Daun jeruk memiliki aroma yang segar dan rasa yang sedikit pahit, sering digunakan dalam masakan Indonesia untuk menambah aroma.',
    'Daun Kemangi': 'Daun kemangi memiliki aroma yang khas dan rasa yang segar, sering digunakan sebagai lalapan dan dalam masakan Indonesia.',
    'Daun Ketumbar': 'Daun ketumbar memiliki aroma yang segar dan rasa yang sedikit pahit, sering digunakan dalam masakan Asia Tenggara.',
    'Daun Salam': 'Daun salam memiliki aroma yang khas dan rasa yang sedikit pahit, sering digunakan dalam masakan Indonesia untuk menambah aroma.',
    'Jinten': 'Jinten memiliki aroma yang kuat dan rasa yang sedikit pahit, sering digunakan dalam masakan India dan Timur Tengah.',
    'Kapulaga': 'Kapulaga memiliki aroma yang kuat dan rasa yang sedikit manis, sering digunakan dalam masakan India dan Timur Tengah.',
    'Kayu Manis': 'Kayu manis memiliki aroma yang manis dan hangat, sering digunakan dalam masakan dan minuman.',
    'Kayu Secang': 'Kayu secang memiliki aroma yang khas dan rasa yang sedikit manis, sering digunakan sebagai pewarna alami dan bahan pengobatan tradisional.',
    'Kemiri': 'Kemiri memiliki rasa yang gurih dan sering digunakan dalam masakan Indonesia sebagai pengental kuah.',
    'Kemukus': 'Kemukus memiliki aroma yang khas dan sering digunakan dalam ritual keagamaan dan sebagai bahan pengobatan tradisional.',
    'Kencur': 'Kencur memiliki aroma yang khas dan rasa yang sedikit pedas, sering digunakan dalam jamu dan masakan Indonesia.',
    'Kluwek': 'Kluwek atau kepayang memiliki rasa yang gurih dan sering digunakan dalam masakan Indonesia, terutama rawon.',
    'Kunyit': 'Kunyit memiliki aroma yang khas dan rasa yang sedikit pahit, sering digunakan sebagai bumbu masakan dan bahan pengobatan tradisional.',
    'Lada': 'Lada memiliki rasa pedas yang khas dan sering digunakan sebagai bumbu masakan.',
    'Lengkuas': 'Lengkuas memiliki aroma yang khas dan rasa yang sedikit pedas, sering digunakan dalam masakan Indonesia.',
    'Pala': 'Pala memiliki aroma yang khas dan rasa yang sedikit manis, sering digunakan dalam masakan Indonesia dan sebagai bahan pengobatan tradisional.',
    'Saffron': 'Saffron adalah rempah yang mahal dengan aroma yang khas dan rasa yang sedikit pahit, sering digunakan dalam masakan Timur Tengah.',
    'Serai': 'Serai memiliki aroma yang khas dan rasa yang sedikit asam, sering digunakan dalam masakan Asia Tenggara.',
    'Vanili': 'Vanili memiliki aroma yang manis dan sering digunakan dalam makanan penutup dan minuman.',
    'Wijen': 'Wijen memiliki rasa yang gurih dan sering digunakan sebagai taburan pada makanan.'
}

# Fungsi untuk menampilkan gambar rempah
def display_rempah(category):
    image_path_jpg = f'assets/images/{category.lower()}.jpg'  # Jalur gambar
    image_path_jpeg = f'assets/images/{category.lower()}.jpeg'  # Alternatif format

    try:
        image = Image.open(image_path_jpg)  # Coba muat file .jpg
        st.image(image, caption=category, use_column_width=True)
    except FileNotFoundError:
        try:
            image = Image.open(image_path_jpeg)  # Jika gagal, coba .jpeg
            st.image(image, caption=category, use_column_width=True)
        except FileNotFoundError:
            st.write(f"Tidak ada gambar untuk {category}")

# Tampilan kategori rempah
st.title("Deteksi Rempah")
st.subheader("Tentang Dataset")

st.write("Dataset ini terdiri dari 31 folder, masing-masing berisi file gambar dari berbagai rempah-rempah yang umum digunakan dalam masakan Indonesia. Setiap folder didedikasikan untuk jenis rempah tertentu, memastikan struktur yang terorganisir dengan baik untuk memudahkan akses dan analisis. Rempah-rempah yang disertakan berkisar dari yang umum seperti bawang putih dan bawang merah hingga bahan-bahan yang lebih unik seperti daun jeruk purut dan daun kemangi. Dataset ini ideal untuk proyek-proyek yang berkaitan dengan klasifikasi gambar, aplikasi kuliner, dan tujuan pendidikan.")

st.subheader("Daftar Rempah")

# Dropdown untuk memilih rempah
selected_category = st.selectbox("Cek rempah untuk informasi lebih lanjut", categories)

# Menampilkan informasi rempah
if selected_category in info_rempah:
    st.write(f"**{selected_category}**: {info_rempah[selected_category]}")
else:
    st.write(f"**{selected_category}**: Informasi belum tersedia.")

# Menampilkan gambar rempah
display_rempah(selected_category)