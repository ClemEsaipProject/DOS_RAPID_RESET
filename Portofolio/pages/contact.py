import streamlit as st
from utils.Cr import generate_rsa_keys, chiffrement_rsa, generer_signature
import base64

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def contact_show():
    st.header("Contactez-moi (Chiffré et Authentifié) 🔒")
    
    # Générer ou récupérer les clés RSA
    if 'private_key' not in st.session_state or 'public_key' not in st.session_state:
        private_key, public_key = generate_rsa_keys()
        st.session_state['private_key'] = private_key
        st.session_state['public_key'] = public_key
    else:
        private_key = st.session_state['private_key']
        public_key = st.session_state['public_key']

    # Formulaire de contact
    with st.form("contact_form"):
        nom = st.text_input("Votre nom")
        email = st.text_input("Votre adresse e-mail")
        message = st.text_area("Votre message")
        submit_button = st.form_submit_button("Envoyer le message chiffré")

        if submit_button:
            # 1. Préparer le message
            message_clair = f"Nom: {nom}\nEmail: {email}\nMessage: {message}".encode('utf-8')

            # 2. Chiffrer le message
            message_chiffre = chiffrement_rsa(message_clair, public_key)
            message_chiffre_b64 = base64.b64encode(message_chiffre).decode('utf-8')

            # 3. Générer une signature
            signature = generer_signature(message_clair, private_key)
            signature_b64 = base64.b64encode(signature).decode('utf-8')

            # Afficher les informations
            st.subheader("Message chiffré (simulé) :")
            st.code(message_chiffre_b64, language='text')

            st.subheader("Signature (simulée) :")
            st.code(signature_b64, language='text')

            st.success("Message chiffré et signature générée ! (Simulé, voir le code source)")

            # Stocker la clé publique pour la démonstration
            st.session_state['public_key_pem'] = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')