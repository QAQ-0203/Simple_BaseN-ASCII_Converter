import streamlit as st
import Base_N as bn

st.set_page_config(page_title="Simple BaseN-ASCII Converter", page_icon=None, layout="centered", initial_sidebar_state="auto")
st.title("Simple BaseN-ASCII Converter")

basen = st.number_input(label="Base", min_value=2, max_value=128, key="base")
MAP = st.text_area(label="Map", height=150, key="map")
txt = st.text_area(label="", height=200, key="txt")

col1, col2, col3, col4= st.columns([1.5, 1.5, 5.5, 2.5])
with col1:
    encode_button = st.button("Encode", use_container_width=True)
with col2:
    decode_button = st.button("Decode", use_container_width=True)
with col4:
    copy_button = st.button("Map Generate", use_container_width=True)

if encode_button:
    st.toast('Encode Success', icon="✅")
    st.write(bn.encoder(int(basen), MAP, txt))

if decode_button:
    st.toast('Decode Success', icon="✅")
    st.write(bn.decoder(int(basen), MAP, txt))
