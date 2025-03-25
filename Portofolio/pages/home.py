import streamlit as st
import os
import streamlit.components.v1 as components



def home_show():
    

    col1, col2= st.columns(2)
    with col1:
        st.title("Ma passion , mon métier 💡")
        st.subheader("Ingénierie, Sécurité, Réflexion : Exploration d'un esprit curieux.")
        # Courts paragraphes de présentation
        st.write("""
            Bienvenue ! Je suis un étudiant ingénieur en cybersécurité, passionné par la complexité du monde numérique. 
            Au-delà des lignes de code et des protocoles de sécurité, je suis fasciné par la philosophie et les mécanismes de l'économie. 
            Ce portfolio est une fenêtre ouverte sur mes explorations, mes projets et mes réflexions.
    """)
        st.write("""
        Mon objectif ? Obtenir mon diplôme et contribuer à un avenir numérique plus sûr et plus éthique. 
        Mais aussi, continuer à explorer les liens fascinants entre la technologie, la société et l'esprit humain.
    """)
         # Aperçu des centres d'intérêt
        st.subheader("Mes Passions 🔍")
        st.write("- 🛡️ Cybersécurité : Protéger les données et les systèmes.")
        st.write("- 💻 Développement : Créer des solutions innovantes.")
        st.write("- 🧠 Philosophie : Comprendre le monde et notre place dedans.")
        st.write("- 📈 Économie : Analyser les forces qui façonnent notre société.")
    with col2:
    # Citation inspirante
        components.iframe("https://tryhackme.com/api/v2/badges/public-profile?userPublicId=3974252", width=400)
        st.markdown("> \"Je pense, donc je suis vulnérable... mais je me protège !\" 😉 - *Clément WAHAGA,35ans*")

    

    

   

    # Appel à l'action
    st.markdown("---")
    st.write("Envie d'en savoir plus ? 👇")
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"Découvrez mes compétences techniques", key="skills")
    with col2:
        st.button("Explorez mes projets", key="projects_button")