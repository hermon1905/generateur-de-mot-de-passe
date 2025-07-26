import random 
import string 
import streamlit as st 

# --------------------------configuration de la page streamlit -------------------------
st.set_page_config(
    page_title="Generateur de mot de passe",
    page_icon="🌀"
)

chiffres = string.digits # les chiffres de 0 à 9
ponctuation = string.punctuation # les ponctuation , caracteres spéciaux
alphabet_letters = string.ascii_letters # les lettres de l'alphabet miniscule comme majuscule 

def gen_mdp(longueur):
    caracteres = chiffres + ponctuation + alphabet_letters 
    mot_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_passe

# longueur = int(input("choisissez la longueur du mot de passe :"))
# mdp = gen_mdp(longueur)

# ------------------configuration de l'app streamlit -----------------------
st.subheader("BIENVENUE DANS NOTRE APPLICATION DE GENERATION DE MOT DE PASSE ")
st.write("Pour generer un mot de passe il faut : chosir la longueur du mot de passe ,ensuite  appuyer sur le boutton de generation.")

longueur = st.number_input("choisissez la longueur du mot de passe :", min_value=8, max_value=30, step=1)

# Bouton de génération
if st.button("Générer un nouveau mot de passe"):
    mot_de_passe = gen_mdp(longueur)
    st.success(gen_mdp(longueur))


