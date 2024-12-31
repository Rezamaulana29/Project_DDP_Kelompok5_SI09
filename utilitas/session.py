import streamlit as st

def init_session_state():
    if 'laundry_data' not in st.session_state:
        st.session_state.laundry_data = []
