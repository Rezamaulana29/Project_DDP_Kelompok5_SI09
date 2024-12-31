import streamlit as st
from utilitas.harga import harga

def masukkan_pesanan():
    st.header("📥 Masukkan Pesanan")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Nama Pelanggan:")
    
    with col2:
        service = st.selectbox("Pilih Layanan:", list(harga.keys()))
    
    weight = st.number_input("Berat Cucian (kg):", min_value=0.0, step=0.1)
    
    if st.button("Tambahkan Pesanan"):
        if name and service and weight > 0:
            order = {
                'Nama': name,
                'Layanan': service,
                'Berat': weight,
                'Harga': weight * harga[service]
            }
            st.session_state.laundry_data.append(order)
            st.success("Pesanan berhasil ditambahkan!")
        else:
            st.warning("Harap isi semua kolom dengan benar.")