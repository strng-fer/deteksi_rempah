import streamlit as st

st.set_page_config(
    page_title="Deteksi Rempah",
    page_icon=":herb:", 
)

col1, col2 = st.columns(2)

with col1:
    st.title("Kenali Rempah dengan Mudah")
    st.markdown(" ")
    st.markdown(
        "Aplikasi ini dapat mendeteksi jenis rempah yang ditangkap oleh kamera secara real-time. "
        "Cukup arahkan kamera ke rempah yang ingin diidentifikasi, dan aplikasi akan menampilkan hasilnya."
    )
    st.link_button("Coba Sekarang :sparkles:", "/Deteksi_Rempah_✨") 

with col2:
    st.image("assets/illustrations/rempah-rempah.jpg")  # Ganti dengan gambar yang relevan

st.markdown("")
st.markdown("")
st.image("assets/illustrations/banner_rempah.jpg")   # Ganti dengan gambar banner yang relevan
