import streamlit as st
from fitur.masukkan_pesanan import masukkan_pesanan
from fitur.tampilkan_daftar_pesanan import tampilkan_daftar_pesanan 
from fitur.perhitungan_total_penghasilan import perhitungan_total_penghasilan
from fitur.kelola_pesanan import kelola_pesanan
from utilitas.session import init_session_state

# Inisialisasi session_state
init_session_state()

# Streamlit Layout
st.title("🧺 Aplikasi Laundry")
st.sidebar.title("Menu")

# Definisikan menu sebagai variabel
menu_options = ["Masukkan Pesanan", "Tampilkan Daftar Pesanan", 
                "Perhitungan Total Penghasilan", "Kelola Pesanan"]
menu = st.sidebar.radio("Pilih Fitur:", menu_options)

# Fungsi untuk menampilkan fitur berdasarkan pilihan
def display_feature(menu):
    try:
        if menu == "Masukkan Pesanan":
            masukkan_pesanan()
        elif menu == "Tampilkan Daftar Pesanan":
            tampilkan_daftar_pesanan()
        elif menu == "Perhitungan Total Penghasilan":
            perhitungan_total_penghasilan()
        elif menu == "Kelola Pesanan":
            kelola_pesanan()
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# Tampilkan fitur yang dipilih
display_feature(menu)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Selamat datang di Aplikasi Laundry Kami! Nikmati kemudahan dalam mengelola semua kebutuhan laundry Anda hanya dengan beberapa klik. Kami siap membantu Anda menghemat waktu dan tenaga!")

# Memuat CSS dari file terpisah
try:
    with open("styles.css", "r") as f:
        st.markdown("<style>" + f.read() + "</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("File CSS tidak ditemukan.")