import streamlit as st
import pandas as pd

def tampilkan_daftar_pesanan():
    st.header("📋 Daftar Pesanan")
    
    if st.session_state.laundry_data:
        # Mengubah data pesanan menjadi DataFrame
        data = {
            "Nama": [order['Nama'] for order in st.session_state.laundry_data],
            "Layanan": [order['Layanan'] for order in st.session_state.laundry_data],
            "Berat (kg)": [order['Berat'] for order in st.session_state.laundry_data],
            "Harga (Rp)": [int(order['Harga']) for order in st.session_state.laundry_data]
        }
        
        df = pd.DataFrame(data)
        
        # Menampilkan DataFrame sebagai tabel
        st.table(df)
    else:
        st.write("Belum ada pesanan.")