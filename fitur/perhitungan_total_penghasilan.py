import streamlit as st

def perhitungan_total_penghasilan():
    st.header("💰 Total Penghasilan")
    if st.session_state.laundry_data:
        total_earnings = sum(order['Harga'] for order in st.session_state.laundry_data)
        st.write(f"*Total Penghasilan:* Rp {int(total_earnings):,}")
    else:
        st.write("Belum ada pesanan untuk dihitung.")