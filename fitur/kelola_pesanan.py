import streamlit as st

def kelola_pesanan():
    st.header("🗑 Status Pesanan")
    if st.session_state.laundry_data:
        names = [order['Nama'] for order in st.session_state.laundry_data]
        selected_name = st.selectbox("Pilih pesanan untuk diselesaikan:", names)
        if st.button("Pesanan Selesai"):
            for order in st.session_state.laundry_data:
                if order['Nama'] == selected_name:
                    st.session_state.laundry_data.remove(order)
                    st.success("Pesanan Selesai,Terimakasih Sudah Laundry di kami")
                    break
    else:
        st.write("Tidak ada pesanan untuk dikelola.")