import streamlit as st
import random
import time

st.set_page_config(page_title="ChemEmotion - Mood dari Makanan", page_icon="🧠", layout="wide")

# Custom CSS untuk mempercantik
st.markdown(
    """
    <style>
    .title {
        font-size:50px; 
        font-weight:bold; 
        text-align:center;
        color: #4CAF50;
    }
    .subtitle {
        font-size:20px;
        text-align:center;
        color: gray;
    }
    .mood-emoji {
        font-size:50px;
        text-align:center;
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul Besar
st.markdown('<div class="title">🧠 ChemEmotion</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Prediksi Mood Berdasarkan Senyawa Kimia dalam Makanan</div>', unsafe_allow_html=True)
st.markdown("---")

# Database senyawa dan efek emosi
compound_effects = {
    "Kafein": "Energi meningkat, waspada, bisa cemas berlebih",
    "Triptofan": "Menenangkan, meningkatkan serotonin",
    "Feniletilamin": "Rasa senang seperti jatuh cinta",
    "Theobromine": "Menenangkan otak, mirip kafein tapi lebih lembut",
    "Tirosin": "Fokus dan motivasi, prekursor dopamin",
    "Gula": "Ledakan energi sesaat, lalu lelah",
    "Flavonoid": "Antioksidan, meningkatkan aliran darah ke otak",
    "Asam amino BCAA": "Meningkatkan performa otak & otot",
    "Asam lemak omega-3": "Menurunkan stres, meningkatkan konsentrasi"
}

food_compounds = {
    "Coklat Hitam": ["Kafein", "Feniletilamin", "Theobromine", "Flavonoid"],
    "Keju": ["Triptofan", "Tirosin"],
    "Kopi": ["Kafein", "Tirosin"],
    "Pisang": ["Triptofan", "Gula"],
    "Ikan Salmon": ["Asam lemak omega-3", "Triptofan"],
    "Teh Hijau": ["Flavonoid", "Theobromine"],
    "Telur": ["Tirosin", "BCAA"],
    "Nasi Putih": ["Gula"],
    "Oatmeal": ["Triptofan", "Flavonoid"]
}

# Session state untuk reset input
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = ""

# Container untuk input makanan
with st.container():
    st.subheader("🍽️ Pilih Makanan atau Bahan Masakan:")
    
    col_input, col_reset = st.columns([4, 1])

    with col_input:
        selected = st.selectbox(
            "Pilih dari daftar makanan:",
            [""] + list(food_compounds.keys()),
            index=0,
            key="selected_food"
        )
    with col_reset:
        if st.button("🔄 Reset"):
            st.session_state.selected_food = ""

# Logika jika makanan dipilih
if st.session_state.selected_food:
    food = st.session_state.selected_food
    with st.spinner('🔍 Menganalisis makananmu...'):
        time.sleep(1)  # loading efek

        if food in food_compounds:
            st.success(f"✅ {food} ditemukan!")

            compounds = food_compounds[food]
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🧪 Senyawa Kimia Terkait:")
                for comp in compounds:
                    st.markdown(f"- **{comp}**")
            
            with col2:
                st.subheader("🎯 Efek Emosi:")
                for comp in compounds:
                    st.markdown(f"- {compound_effects.get(comp, 'Efek tidak tersedia')}")

            st.markdown("---")
            st.subheader("🌈 Mood Gabungan:")
            emojis = ["😃", "😴", "😵", "🤯", "😌", "😎", "😍", "🤓"]
            mood_summary = random.sample(emojis, k=min(3, len(compounds)))
            st.markdown(f"<div class='mood-emoji'>{' '.join(mood_summary)}</div>", unsafe_allow_html=True)

        else:
            st.warning("⚠️ Makanan tidak ditemukan dalam database. Coba lainnya!")

st.markdown("---")
st.info("💡 Ingin menambahkan makanan baru? Versi mendatang akan mendukung input custom dan analisis AI! 🚀")
