import streamlit as st

def projects_show():
    st.header("🚀 Mes Projets")

    # Tabs pour catégoriser les projets
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🛡️ Cybersécurité", "💻 Développement", "📊 Data Science", "🎓 Académiques", "🏆 Open Source"
    ])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔐 Pentest d'une Application Web")
            st.write("""
            - **Objectif :** Identifier et corriger des vulnérabilités sur une plateforme e-commerce.
            - **Outils utilisés :** Burp Suite, Kali Linux, Metasploit, OWASP ZAP.
            - **Résultat :** Détection de plusieurs failles (XSS, SQLi) et mise en place de correctifs.
            """)
            st.link_button("🔗 Voir sur GitHub", "https://github.com/monprojet")

        with col2:
            st.subheader("🔎 Analyse de Malware")
            st.write("""
            - **Objectif :** Étudier le comportement d'un malware en environnement sandbox.
            - **Outils :** Wireshark, IDA Pro, Python.
            - **Résultat :** Identification des mécanismes d'obfuscation et proposition de contre-mesures.
            """)
            st.link_button("🔗 Voir sur GitHub", "https://github.com/monprojet")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📱 Application Mobile de Gestion de Tâches")
            st.write("""
            - **Technologies :** Flutter, Firebase, Python (Backend).
            - **Description :** Une app permettant de gérer ses tâches avec rappels et notifications.
            """)
            st.link_button("🔗 Démo en ligne", "https://monapp.com")

        with col2:
            st.subheader("🌐 Site Web de Sécurisation des Mots de Passe")
            st.write("""
            - **Technologies :** React, Node.js, MongoDB.
            - **Description :** Générateur et coffre-fort de mots de passe avec chiffrement AES.
            """)
            st.link_button("🔗 Voir sur GitHub", "https://github.com/monprojet")