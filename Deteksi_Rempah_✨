import streamlit as st
import sys
from helpers.object_detection import realtime_video_detection

st.set_page_config(
    page_title="Deteksi Rempah Realtime",
    page_icon=":herb:",
)

sys.path.append("helpers")

st.header("Deteksi Rempah :herb:", divider="green")  # Ubah header dan divider

try:
    realtime_video_detection()
except Exception as e:
    st.error(f"Terjadi error: {e}")
