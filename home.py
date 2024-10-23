import streamlit as st

st.set_page_config(
    page_title="Deteksi Rempah",
    page_icon=":herb:",
)

#  Gambar latar belakang 
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://unsplash.com/photos/a-bowl-of-spices-on-a-table-Mt7ZxezO7_k");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("---") 
st.image("assets/illustrations/banner_rempah.webp")

col1, col2 = st.columns([3, 2]) 

st.title("Rahasia Rempah di Ujung Jari Anda") 
st.subheader("Identifikasi rempah dengan cepat dan mudah!")

if st.button("Cek rempahmu di sini🔎"): 
    with st.spinner("Memuat..."):  
        st.switch_page("pages/1_Deteksi_Rempah.py")