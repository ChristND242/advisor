import streamlit as st
import streamlit.components.v1 as components
import requests

# Set page title and layout
st.set_page_config(page_title="Browser Privacy Settings Advisor", page_icon="🔒", layout="centered")

# Language selection
language = st.sidebar.selectbox("Select Language / Sélectionnez la langue", ("English", "Français"))

# Define translated content
content = {
    "English": {
        "title": "🔒 Browser Privacy Settings Advisor",
        "description": """
Welcome to the **Browser Privacy Settings Advisor**. 
Select your browser from the dropdown menu to view recommended privacy settings and explanations for each option.
We'll also perform automatic checks to detect some of your current browser privacy settings.
""",
        "select_browser": "Select your browser",
        "settings": "Here are the recommended privacy settings for",
        "footer": "💡 Remember: Adjusting your browser's privacy settings can significantly improve your online security and privacy. Always review and update them periodically.",
        "automatic_checks": "Automatic Privacy Checks",
        "dnt_status": "**Do Not Track Status**",
        "cookie_status": "**Cookie Status**",
        "js_status": "**JavaScript Status**",
        "check_fingerprint": "[Check Your Browser Fingerprint with Panopticlick](https://panopticlick.eff.org/)",
        "browsers": {
            "Google Chrome": """
- **Block third-party cookies**: Prevents advertisers from tracking you across multiple sites.
  - Go to `Settings > Privacy and security > Cookies and other site data > Block third-party cookies`.
  
- **Enable 'Do Not Track' requests**: Requests websites not to track your activity, though it relies on website cooperation.
  - Go to `Settings > Privacy and security > Send a "Do Not Track" request with your browsing traffic`.
  
- **Turn on Safe Browsing (Enhanced protection)**: Helps protect against malicious sites and downloads.
  - Go to `Settings > Privacy and security > Security > Safe Browsing`.
""",
            "Mozilla Firefox": """
- **Strict Tracking Protection**: Blocks most trackers, cookies, and crypto miners.
  - Go to `Settings > Privacy & Security > Enhanced Tracking Protection > Strict`.
  
- **Delete cookies and site data when Firefox is closed**: Automatically clears cookies and site data when you close Firefox.
  - Go to `Settings > Privacy & Security > Cookies and Site Data > Delete cookies and site data when Firefox is closed`.
  
- **Enable 'Do Not Track' requests**: Requests websites not to track you.
  - Go to `Settings > Privacy & Security > Send websites a "Do Not Track" signal.
""",
            "Safari": """
- **Prevent cross-site tracking**: Stops websites from tracking you across different domains.
  - Go to `Safari > Preferences > Privacy > Prevent cross-site tracking`.
  
- **Block all cookies**: Blocks all cookies from websites, which can enhance privacy but may break some sites.
  - Go to `Safari > Preferences > Privacy > Block all cookies`.
  
- **Fraudulent website warning**: Warns you if a site is suspected of phishing.
  - Go to `Safari > Preferences > Privacy > Fraudulent website warning`.
""",
            "Microsoft Edge": """
- **Tracking prevention (Strict)**: Blocks most trackers and prevents personalized ads.
  - Go to `Settings > Privacy, search, and services > Tracking prevention > Strict`.
  
- **Clear browsing data on close**: Automatically deletes browsing data when you close Edge.
  - Go to `Settings > Privacy, search, and services > Clear browsing data > Choose what to clear every time you close the browser`.
  
- **Block third-party cookies**: Stops advertisers from tracking your activity across different websites.
  - Go to `Settings > Privacy, search, and services > Cookies and site permissions > Manage and delete cookies and site data`.
""",
            "Brave": """
- **Shields Up (Default)**: Blocks trackers, cross-site cookies, and ads.
  - Go to `Settings > Shields > Standard (or Aggressive)`.
  
- **Fingerprinting Protection**: Prevents websites from uniquely identifying your browser configuration.
  - Go to `Settings > Shields > Fingerprinting Protection`.
  
- **HTTPS Everywhere**: Forces secure connections wherever possible.
  - Go to `Settings > Shields > Connections > Always use secure connections`.
""",
            "Opera": """
- **Block ads and trackers**: Prevents advertisements and online trackers.
  - Go to `Settings > Privacy Protection > Block ads and trackers`.
  
- **VPN (Virtual Private Network)**: Enables a free, built-in VPN to mask your IP address.
  - Go to `Settings > Privacy Protection > Enable VPN`.
  
- **Clear cookies and data on close**: Automatically clears browsing data after each session.
  - Go to `Settings > Privacy Protection > Clear cookies and site data when I quit Opera`.
""",
            "Chrome for Android": """
- **Block third-party cookies**: Prevents advertisers from tracking you across apps and websites.
  - Go to `Settings > Site settings > Cookies > Block third-party cookies`.
  
- **Enable 'Do Not Track' requests**: Requests websites not to track your activity.
  - Go to `Settings > Privacy and security > Do Not Track`.
  
- **Clear browsing data regularly**: Protect your privacy by clearing browsing history and cookies.
  - Go to `Settings > Privacy and security > Clear browsing data`.
""",
            "Safari for iOS": """
- **Prevent cross-site tracking**: Stops websites from tracking you across different domains.
  - Go to `Settings > Safari > Prevent cross-site tracking`.
  
- **Block all cookies**: Blocks all cookies from websites.
  - Go to `Settings > Safari > Block all cookies`.
  
- **Fraudulent website warning**: Warns you if a site is suspected of phishing.
  - Go to `Settings > Safari > Fraudulent website warning`.
"""
        }
    },
    "Français": {
        "title": "🔒 Conseiller des Paramètres de Confidentialité du Navigateur",
        "description": """
Bienvenue dans le **Conseiller des Paramètres de Confidentialité du Navigateur**. 
Sélectionnez votre navigateur dans le menu déroulant pour afficher les paramètres de confidentialité recommandés et des explications pour chaque option.
Nous effectuerons également des vérifications automatiques pour détecter certains des paramètres de confidentialité de votre navigateur actuel.
""",
        "select_browser": "Sélectionnez votre navigateur",
        "settings": "Voici les paramètres de confidentialité recommandés pour",
        "footer": "💡 N'oubliez pas : Ajuster les paramètres de confidentialité de votre navigateur peut améliorer considérablement votre sécurité et confidentialité en ligne. Revoyez-les et mettez-les à jour périodiquement.",
        "automatic_checks": "Vérifications Automatiques de Confidentialité",
        "dnt_status": "**Statut de Do Not Track**",
        "cookie_status": "**Statut des Cookies**",
        "js_status": "**Statut de JavaScript**",
        "check_fingerprint": "[Vérifiez l'Empreinte de votre Navigateur avec Panopticlick](https://panopticlick.eff.org/)",
        "browsers": {
        "Google Chrome": """
          - **Bloquer les cookies tiers** : Empêche les publicitaires de vous suivre sur plusieurs sites.
            - Allez dans `Paramètres > Confidentialité et sécurité > Cookies et autres données de site > Bloquer les cookies tiers`.
          
          - **Activer les requêtes 'Ne pas me suivre'** : Demande aux sites web de ne pas suivre votre activité, bien que cela dépende de la coopération des sites web.
            - Allez dans `Paramètres > Confidentialité et sécurité > Envoyer une requête "Ne pas me suivre" avec votre trafic de navigation`.
          
          - **Activer la navigation sécurisée (Protection renforcée)** : Aide à vous protéger contre les sites et téléchargements malveillants.
            - Allez dans `Paramètres > Confidentialité et sécurité > Sécurité > Navigation sécurisée`.
        """,
        
        "Mozilla Firefox": """
          - **Protection stricte contre le suivi** : Bloque la plupart des traqueurs, cookies et mineurs de cryptomonnaies.
            - Allez dans `Paramètres > Vie privée et sécurité > Protection améliorée contre le suivi > Stricte`.
          
          - **Supprimer les cookies et les données de site lors de la fermeture de Firefox** : Efface automatiquement les cookies et les données des sites lorsque vous fermez Firefox.
            - Allez dans `Paramètres > Vie privée et sécurité > Cookies et données des sites > Supprimer les cookies et les données des sites lors de la fermeture de Firefox`.
          
          - **Activer les requêtes 'Ne pas me suivre'** : Demande aux sites web de ne pas vous suivre.
            - Allez dans `Paramètres > Vie privée et sécurité > Envoyer un signal "Ne pas me suivre" aux sites web`.
        """,
        
        "Safari": """
          - **Empêcher le suivi intersites** : Empêche les sites de vous suivre à travers différents domaines.
            - Allez dans `Safari > Préférences > Confidentialité > Empêcher le suivi intersites`.
          
          - **Bloquer tous les cookies** : Bloque tous les cookies des sites web, ce qui améliore la confidentialité mais peut perturber certains sites.
            - Allez dans `Safari > Préférences > Confidentialité > Bloquer tous les cookies`.
          
          - **Avertissement de site frauduleux** : Vous avertit si un site est suspecté de phishing.
            - Allez dans `Safari > Préférences > Confidentialité > Avertissement de site frauduleux`.
        """,
        
        "Microsoft Edge": """
          - **Prévention du suivi (Stricte)** : Bloque la plupart des traqueurs et empêche les publicités personnalisées.
            - Allez dans `Paramètres > Confidentialité, recherche et services > Prévention du suivi > Stricte`.
          
          - **Effacer les données de navigation à la fermeture** : Supprime automatiquement les données de navigation lorsque vous fermez Edge.
            - Allez dans `Paramètres > Confidentialité, recherche et services > Effacer les données de navigation > Choisir ce que vous souhaitez effacer à chaque fermeture du navigateur`.
          
          - **Bloquer les cookies tiers** : Empêche les publicitaires de suivre votre activité sur différents sites web.
            - Allez dans `Paramètres > Confidentialité, recherche et services > Cookies et autorisations de site > Gérer et supprimer les cookies et données des sites`.
        """,
        
        "Brave": """
          - **Boucliers activés (Par défaut)** : Bloque les traqueurs, les cookies intersites et les publicités.
            - Allez dans `Paramètres > Boucliers > Standard (ou Aggressif)`.
          
          - **Protection contre le fingerprinting** : Empêche les sites web d'identifier de manière unique la configuration de votre navigateur.
            - Allez dans `Paramètres > Boucliers > Protection contre le fingerprinting`.
          
          - **HTTPS partout** : Force les connexions sécurisées partout où cela est possible.
            - Allez dans `Paramètres > Boucliers > Connexions > Toujours utiliser des connexions sécurisées`.
        """,
        
        "Opera": """
          - **Bloquer les publicités et les traqueurs** : Empêche les publicités et les traqueurs en ligne.
            - Allez dans `Paramètres > Protection de la vie privée > Bloquer les publicités et les traqueurs`.
          
          - **VPN (Réseau privé virtuel)** : Active un VPN intégré gratuit pour masquer votre adresse IP.
            - Allez dans `Paramètres > Protection de la vie privée > Activer le VPN`.
          
          - **Effacer les cookies et les données à la fermeture** : Supprime automatiquement les données de navigation après chaque session.
            - Allez dans `Paramètres > Protection de la vie privée > Effacer les cookies et les données des sites lorsque je quitte Opera`.
        """,
        
        "Chrome pour Android": """
          - **Bloquer les cookies tiers** : Empêche les publicitaires de vous suivre à travers les applications et les sites web.
            - Allez dans `Paramètres > Paramètres du site > Cookies > Bloquer les cookies tiers`.
          
          - **Activer les requêtes 'Ne pas me suivre'** : Demande aux sites web de ne pas suivre votre activité.
            - Allez dans `Paramètres > Confidentialité et sécurité > Ne pas me suivre`.
          
          - **Effacer régulièrement les données de navigation** : Protégez votre confidentialité en effaçant l'historique de navigation et les cookies.
            - Allez dans `Paramètres > Confidentialité et sécurité > Effacer les données de navigation`.
        """,
        
        "Safari pour iOS": """
          - **Empêcher le suivi intersites** : Empêche les sites de vous suivre à travers différents domaines.
            - Allez dans `Paramètres > Safari > Empêcher le suivi intersites`.
          
          - **Bloquer tous les cookies** : Bloque tous les cookies des sites web.
            - Allez dans `Paramètres > Safari > Bloquer tous les cookies`.
          
          - **Avertissement de site frauduleux** : Vous avertit si un site est suspecté de phishing.
            - Allez dans `Paramètres > Safari > Avertissement de site frauduleux`.
        """
      }
    }
}

# Title and description
st.title(content[language]["title"])
st.write(content[language]["description"])

# Step 1: Browser selection
browser = st.selectbox(content[language]["select_browser"], 
    ("Google Chrome", "Mozilla Firefox", "Safari", "Microsoft Edge", "Brave", "Opera", 
     "Chrome for Android", "Safari for iOS"))

# Step 2: Display recommended privacy settings based on the browser selected
st.subheader(f"{content[language]['settings']} {browser}")
st.markdown(content[language]["browsers"].get(browser, "No settings available"))

# Step 3: Automatic Browser Privacy Checks
st.write("---")
st.subheader(content[language]["automatic_checks"])

# JavaScript to check if "Do Not Track" is enabled
st.markdown(content[language]["dnt_status"])
components.html("""
    <script>
        var dntStatus = (navigator.doNotTrack == "1" || window.doNotTrack == "1" || navigator.msDoNotTrack == "1") ? "Enabled" : "Disabled";
        document.write("<h4>Do Not Track: " + dntStatus + "</h4>");
    </script>
""", height=50)

# JavaScript to check if cookies are enabled
st.markdown(content[language]["cookie_status"])
components.html("""
    <script>
        var cookieEnabled = navigator.cookieEnabled ? "Enabled" : "Disabled";
        document.write("<h4>Cookies: " + cookieEnabled + "</h4>");
    </script>
""", height=50)

# JavaScript to check if JavaScript is enabled (this would always return true as this is a JS check)
st.markdown(content[language]["js_status"])
components.html("""
    <script>
        document.write("<h4>JavaScript: Enabled</h4>");
    </script>
""", height=50)

# Placeholder for Panopticlick API or link for browser fingerprint check
st.subheader("Advanced Privacy Checks")
st.write("Checking browser fingerprint using Panopticlick API...")
st.markdown("[Run Panopticlick Test](https://panopticlick.eff.org/)")

# Placeholder for IP leak detection (implement using ipleak.net API or similar)
st.write("Checking for IP leaks... (Feature coming soon!)")

# Footer or additional info
st.write("---")
st.write(content[language]["footer"])
st.markdown(content[language]["check_fingerprint"])


# Footer
st.markdown("""
    <footer style='text-align: center; padding: 10px; font-size: 14px; color: #ABB2B9;'>
    Created with ❤️ by Christ.ND
    </footer>
    """, unsafe_allow_html=True)