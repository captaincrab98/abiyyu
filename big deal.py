import streamlit as st
import pandas as pd
import random
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="ChemEmotion - Mood dari Makanan", page_icon="🧠", layout="wide")

# Custom CSS untuk mempercantik tampilan
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 0.5em;
        }
        .subtitle {
            font-size: 1.5em;
            text-align: center;
            color: #555;
            margin-bottom: 1.5em;
        }
        .compound-card {
            background-color: #f0f9f9;
            padding: 1em;
            border-radius: 12px;
            margin-bottom: 1em;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        .mood-emoji {
            font-size: 2em;
        }
    </style>
""", unsafe_allow_html=True)

# Title dan subtitle
st.markdown('<div class="main-title">\ud83e\udde0 ChemEmotion</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Prediksi Mood Berdasarkan Senyawa Kimia dalam Makanan</div>', unsafe_allow_html=True)

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

# Pemetaan makanan ke senyawa dominan
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

# Input makanan dari user
with st.container():
    food = st.text_input("\ud83c\udf7d\ufe0f Masukkan nama makanan / bahan masakan:", placeholder="Contoh: Coklat Hitam, Kopi, Pisang").strip().title()

if food:
    if food in food_compounds:
        st.success(f"\u2705 {food} ditemukan dalam database!")
        compounds = food_compounds[food]

        st.markdown("### \ud83e\uddea Senyawa Kimia Terkait:")
        
        for comp in compounds:
            with stylable_container("compound-card", key=comp):
                st.markdown(f"**{comp}**: {compound_effects.get(comp, 'Efek tidak tersedia')}")

        st.markdown("### \ud83c\udf08 Prediksi Mood:")
        emojis = ["😃", "😴", "😵", "🤯", "😌", "😎"]
        mood_summary = random.sample(emojis, k=min(3, len(compounds)))
        st.markdown(f"<div class='mood-emoji'>{' '.join(mood_summary)}</div>", unsafe_allow_html=True)
    else:
        st.warning("\u26a0\ufe0f Makanan tidak ditemukan dalam database. Coba lainnya!")

st.markdown("""---
### \ud83d\udca1 Ingin menambahkan makanan baru?
Versi lanjutan akan mendukung input custom dan analisis AI!
""")
