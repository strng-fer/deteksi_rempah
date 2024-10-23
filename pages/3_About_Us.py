import streamlit as st

st.set_page_config(
    page_title="Tentang Kami",
    page_icon=":information:",
)

st.title("Tentang Deteksi Rempah")

st.header("Visi")
st.write(
    "Menjadi platform terdepan dalam identifikasi rempah-rempah "
    "menggunakan teknologi kecerdasan buatan yang mudah diakses dan akurat."
)

st.header("Misi")
st.markdown(
    """
    * Menyediakan aplikasi yang mudah digunakan untuk identifikasi rempah.
    * Memberdayakan masyarakat dengan pengetahuan tentang rempah-rempah.
    * Mendorong pemanfaatan teknologi AI dalam bidang kuliner.
    """
)

st.header("Data yang Digunakan")
st.write(
    "Aplikasi ini dilatih menggunakan dataset gambar rempah-rempah "
    "yang dikumpulkan dari berbagai sumber. Jenis data yang digunakan adalah: "
)
st.markdown(
    """
    * **Gambar:**  Berisi berbagai jenis gambar rempah-rempah.
    * **Label:**  Setiap gambar diberi label dengan nama rempah yang sesuai. 
    """
)

st.write("Link ke data: https://www.kaggle.com/datasets/albertnathaniel12/indonesian-spices-dataset")

st.header("Kode Sumber")
st.write("Kode sumber aplikasi ini tersedia di GitHub:")
st.write("[https://github.com/strng-fer/deteksi_rempah]")

st.header("Pengembang")
st.subheader("Feryadi Yulius") 
st.write(
    "Data Science student at Institut Teknologi Sumatera with a passion for technology, mathematics, data science, and machine learning especially in NLP and Image processing."
    "Fluent both in English and Bahasa Indonesia. Mastering Python, R, and SQL for data analysis. With strong leadership, communication, critical thinking, and analytical skills, envisions making meaningful contributions to data-driven decision-making and technology."
)
st.write("LinkedIn: [https://www.linkedin.com/in/feryadi-yulius/]")

st.markdown("---")
st.write("© 2024 Deteksi Rempah")