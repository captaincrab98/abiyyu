import streamlit as st
import pandas as pd

# ======= CSS Styling dan Animasi =======
st.markdown("""
    <style>
    @keyframes moveBackground {
        0% { background-position: 0 0; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0 0; }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .fade-title {
        font-size: 30px;
        font-weight: bold;
        color: #2c6e49;
        text-align: center;
        animation: fadeIn 1.5s ease-in-out;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    .good {
        color: #388e3c;
        font-weight: bold;
        animation: fadeIn 1s ease-in;
    }

    .bad {
        color: #d32f2f;
        font-weight: bold;
        animation: fadeIn 1s ease-in;
    }

    .neutral {
        color: #fbc02d;
        font-weight: bold;
        animation: fadeIn 1s ease-in;
    }
    </style>
""", unsafe_allow_html=True)

# ======= Judul Aplikasi =======
st.markdown('<div class="fade-title">🍽️ Deteksi Senyawa Organik dalam Makanan</div>', unsafe_allow_html=True)

# ======= Sidebar Navigasi =======
menu_pilihan = st.sidebar.radio("Navigasi", ["Home", "Kamus Senyawa", "Tentang Kami"])

# ======= Kamus Senyawa Organik =======
organic_compounds = {
    "Aflatoksin": {"kategori": "Toksin alami", "fungsi": "Racun dari jamur.", "efek": "Berbahaya", "skor": 10},
    "Vitamin C": {"kategori": "Vitamin", "fungsi": "Antioksidan, meningkatkan daya tahan tubuh.", "efek": "Baik", "skor": 95},
    "Asam Amino": {"kategori": "Asam Amino Esensial", "fungsi": "Penyusun protein, penting untuk pertumbuhan.", "efek": "Baik", "skor": 90},
    "Lemak Jenuh": {"kategori": "Lemak", "fungsi": "Sumber energi, tapi jika berlebih meningkatkan kolesterol.", "efek": "Netral", "skor": 50},
    "Asam Benzoat": {"kategori": "Pengawet legal", "fungsi": "Pengawet makanan.", "efek": "Netral", "skor": 55},
    "Fruktosa": {"kategori": "Gula alami", "fungsi": "Pemanis alami, sumber energi.", "efek": "Berbahaya jika berlebihan", "skor": 40},
    "Asam Oksalat": {"kategori": "Asam organik alami", "fungsi": "Ditemukan dalam bayam, bisa membentuk batu ginjal jika berlebih.", "efek": "Berbahaya jika berlebihan", "skor": 35},
    "Purina": {"kategori": "Senyawa nitrogen alami", "fungsi": "Terkandung dalam daging merah, bisa memicu asam urat jika berlebihan.", "efek": "Berbahaya jika berlebihan", "skor": 30},
    "Kafein": {"kategori": "Alkaloid", "fungsi": "Stimulasi sistem saraf pusat.", "efek": "Netral", "skor": 70},
    "Sodium": {"kategori": "Mineral", "fungsi": "Membantu mengatur keseimbangan cairan tubuh.", "efek": "Baik jika dalam jumlah wajar", "skor": 75},
    "Asam Folat": {"kategori": "Vitamin", "fungsi": "Penting untuk pembentukan sel darah merah.", "efek": "Baik", "skor": 80},
    "Glukosa": {"kategori": "Gula", "fungsi": "Sumber energi utama bagi tubuh.", "efek": "Baik jika dalam jumlah wajar", "skor": 85},
    "Kolesterol": {"kategori": "Lemak", "fungsi": "Penting untuk membran sel, produksi hormon.", "efek": "Berbahaya jika berlebih", "skor": 40},
    "Sorbitol": {"kategori": "Pemanis buatan", "fungsi": "Pengganti gula yang lebih rendah kalori.", "efek": "Netral", "skor": 60},
    "Asam Laktat": {"kategori": "Asam organik", "fungsi": "Hasil samping fermentasi.", "efek": "Netral", "skor": 65},
    "Fruktosamin": {"kategori": "Asam organik", "fungsi": "Pengukur kadar glukosa darah.", "efek": "Baik", "skor": 80},
    "Glutamat Monosodium (MSG)": {"kategori": "Bahan tambahan makanan", "fungsi": "Meningkatkan rasa umami.", "efek": "Netral", "skor": 50},
    "Tanin": {"kategori": "Alkaloid", "fungsi": "Ditemukan dalam teh dan anggur, memiliki sifat astringen.", "efek": "Netral", "skor": 60},
    "Tiamin (Vitamin B1)": {"kategori": "Vitamin", "fungsi": "Membantu metabolisme karbohidrat.", "efek": "Baik", "skor": 85},
    "Magnesium": {"kategori": "Mineral", "fungsi": "Membantu fungsi otot dan saraf.", "efek": "Baik", "skor": 90},
    "Zat Besi": {"kategori": "Mineral", "fungsi": "Penting untuk pembentukan hemoglobin.", "efek": "Baik", "skor": 90},
    "Kalsium": {"kategori": "Mineral", "fungsi": "Penting untuk kesehatan tulang.", "efek": "Baik", "skor": 95},
    "Bromelain": {"kategori": "Enzim", "fungsi": "Membantu pencernaan protein.", "efek": "Baik", "skor": 85}
}

# ======= Pemetaan Makanan -> Senyawa =======
makanan_to_senyawa = {
    "Jeruk": ["Vitamin C", "Asam Amino", "Fruktosa", "Asam Folat"],
    "Kacang Tanah": ["Asam Amino", "Lemak Jenuh", "Aflatoksin", "Tiamin (Vitamin B1)"],
    "Tahu": ["Asam Amino", "Asam Folat", "Magnesium"],
    "Ikan Asin": ["Asam Amino", "Magnesium", "Kalsium"],
    "Minuman Bersoda": ["Asam Benzoat", "Fruktosa", "Kafein"],
    "Sereal": ["Vitamin C", "Lemak Jenuh", "Asam Amino", "Kalsium"],
    "Daging Sapi": ["Asam Amino", "Lemak Jenuh", "Purina", "Zat Besi"],
    "Sayur Bayam": ["Vitamin C", "Asam Amino", "Asam Oksalat", "Kalsium"],
    "Makanan Kaleng": ["Asam Benzoat", "Tanin"],
    "Kopi": ["Kafein", "Sodium"],
    "Anggur": ["Tanin", "Vitamin C", "Glukosa"],
    "Tomat": ["Asam Oksalat", "Vitamin C"],
    "Pisang": ["Fruktosa", "Tiamin (Vitamin B1)", "Magnesium"],
    "Apel": ["Fruktosa", "Vitamin C"],
    "Susu": ["Kalsium", "Asam Laktat"],
    "Teh Hijau": ["Tanin", "Vitamin C", "Magnesium"],
    "Soya": ["Asam Amino", "Magnesium"],
    "Salmon": ["Asam Amino", "Magnesium"],
    "Nanas": ["Bromelain", "Vitamin C"],
    "Madu": ["Fruktosa", "Glukosa"],
    "Paprika": ["Vitamin C", "Kalsium"]
}

# ======= Fungsi Menampilkan Senyawa =======
def tampilkan_senyawa(judul, daftar_senyawa):
    if daftar_senyawa:
        st.subheader(judul)
        for senyawa in daftar_senyawa:
            data = organic_compounds[senyawa]
            efek = data["efek"]
            skor = data["skor"]
            kelas = "good" if efek == "Baik" else "bad" if "Berbahaya" in efek else "neutral"
            st.markdown(f'<h4 class="{kelas}">{senyawa}</h4>', unsafe_allow_html=True)
            st.write(f"**Kategori:** {data['kategori']}")
            st.write(f"**Fungsi:** {data['fungsi']}")
            st.write(f"**Efek:** {data['efek']}")
            st.progress(skor)
    else:
        st.info(f"Tidak ada {judul.lower()}.")

# ======= Halaman Home =======
if menu_pilihan == "Home":
    menu = st.selectbox("Pilih Metode Deteksi", ("Deteksi dari Nama Makanan", "Deteksi dari File CSV"))

    if menu == "Deteksi dari Nama Makanan":
        makanan_input = st.text_input("Masukkan nama makanan:")
        if st.button("Cari Senyawa"):
            if makanan_input:
                makanan = makanan_input.strip().title()
                if makanan in makanan_to_senyawa:
                    baik, berbahaya, netral = [], [], []
                    for senyawa in makanan_to_senyawa[makanan]:
                        efek = organic_compounds[senyawa]["efek"]
                        (baik if efek == "Baik" else berbahaya if "Berbahaya" in efek else netral).append(senyawa)
                    tampilkan_senyawa("✅ Senyawa Baik untuk Tubuh", baik)
                    tampilkan_senyawa("⚠️ Senyawa Berbahaya jika Berlebihan", berbahaya)
                    tampilkan_senyawa("🔶 Senyawa Netral", netral)
                else:
                    st.warning("Data senyawa belum tersedia untuk makanan tersebut.")
            else:
                st.warning("Mohon masukkan nama makanan.")

    elif menu == "Deteksi dari File CSV":
        uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file, encoding="utf-8")
                st.write("Data yang diupload:")
                st.dataframe(df)

                if 'Makanan' in df.columns:
                    df = df.dropna(subset=['Makanan'])
                    for makanan in df['Makanan']:
                        makanan = makanan.strip().title()
                        st.markdown(f"## 🍽️ {makanan}")
                        if makanan in makanan_to_senyawa:
                            baik, berbahaya, netral = [], [], []
                            for senyawa in makanan_to_senyawa[makanan]:
                                efek = organic_compounds[senyawa]["efek"]
                                (baik if efek == "Baik" else berbahaya if "Berbahaya" in efek else netral).append(senyawa)
                            tampilkan_senyawa("✅ Senyawa Baik untuk Tubuh", baik)
                            tampilkan_senyawa("⚠️ Senyawa Berbahaya jika Berlebihan", berbahaya)
                            tampilkan_senyawa("🔶 Senyawa Netral", netral)
                        else:
                            st.warning("Data senyawa belum tersedia untuk makanan ini.")
                else:
                    st.error("File harus memiliki kolom 'Makanan'.")
            except Exception as e:
                st.error(f"Gagal membaca file: {e}")

# ======= Kamus Senyawa =======
elif menu_pilihan == "Kamus Senyawa":
    st.subheader("📖 Kamus Senyawa Organik")
    senyawa_dipilih = st.selectbox("Pilih Senyawa", sorted(organic_compounds.keys()))
    if senyawa_dipilih:
        data = organic_compounds[senyawa_dipilih]
        efek = data["efek"]
        skor = data["skor"]
        kelas = "good" if efek == "Baik" else "bad" if "Berbahaya" in efek else "neutral"
        st.markdown(f'<h3 class="{kelas}">{senyawa_dipilih}</h3>', unsafe_allow_html=True)
        st.write(f"**Kategori:** {data['kategori']}")
        st.write(f"**Fungsi:** {data['fungsi']}")
        st.write(f"**Efek:** {data['efek']}")
        st.progress(skor)

# ======= Tentang Kami =======
elif menu_pilihan == "Tentang Kami":
    st.subheader("👩‍🔬 Tentang Aplikasi Ini")
    st.markdown("""
    Aplikasi **Deteksi Senyawa Organik dalam Makanan** dikembangkan untuk memberikan edukasi mengenai kandungan senyawa dalam makanan sehari-hari.

    **🎯 Tujuan:**
    - Membantu mengenali senyawa alami dan tambahan pada makanan.
    - Memberikan informasi efek senyawa terhadap kesehatan.

    **🧠 Fitur Utama:**
    - Deteksi senyawa dari input makanan atau file CSV.
    - Kamus senyawa interaktif lengkap.
    - Visualisasi efek senyawa dengan skor warna.

    **👨‍💻 Pengembang:**  
    [kelompok 5 PMIP E2]  
    2025
    """)
