import streamlit as st
from tamagotchi import *

st.title("🐾 Mon Tamagotchi")

# Initialisation du Tamagotchi dans la session Streamlit
if "mon_pet" not in st.session_state:
    st.session_state.mon_pet = Tamagotchi("Pixel")

pet = st.session_state.mon_pet

# Affichage des jauges
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Faim (0 = rassasié)", f"{pet.eat} / 100")
with col2:
    st.metric("Énergie", f"{pet.energy} / 100")
with col3:
    st.metric("Bonheur", f"{pet.joy} / 100")

st.divider()

# Boutons d'action
b1, b2, b3 = st.columns(3)

with b1:
    if st.button("🍖 Nourrir"):
        message = pet.to_feed()
        st.success(message)

with b2:
    if st.button("🎾 Jouer"):
        message = pet.play()
        st.info(message)

with b3:
    if st.button("💤 Dormir"):
        message = pet.sleep()
        st.warning(message)
