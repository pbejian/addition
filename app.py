import streamlit as st

st.title("Addition")

# Résultat : même couleur que le texte normal, en gras
st.markdown("""
<style>
input:disabled {
    color: inherit !important;
    -webkit-text-fill-color: currentColor !important;
    opacity: 1 !important;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


def lire_nombre(texte):
    """Renvoie un int si possible, sinon un float (ValueError si invalide)."""
    texte = texte.strip().replace(",", ".")
    try:
        return int(texte)
    except ValueError:
        return float(texte)


def calculer():
    try:
        st.session_state.somme = lire_nombre(st.session_state.a) + lire_nombre(st.session_state.b)
        st.session_state.erreur = False
    except ValueError:
        st.session_state.somme = None
        st.session_state.erreur = True


def calculer_si_a_rempli():
    # Entrée dans la 2e case : on calcule seulement si la 1re est remplie
    if st.session_state.a.strip():
        calculer()


if "somme" not in st.session_state:
    st.session_state.somme = None
    st.session_state.erreur = False

col1, col2, col3 = st.columns([4, 1, 4], vertical_alignment="center")
with col1:
    st.text_input("Nombre 1", key="a")
with col2:
    st.markdown("<h3 style='text-align:center'>+</h3>", unsafe_allow_html=True)
with col3:
    st.text_input("Nombre 2", key="b", on_change=calculer_si_a_rempli)

st.button("Calculer", on_click=calculer)

if st.session_state.erreur:
    st.error("Entre deux nombres valides.")

resultat = "" if st.session_state.somme is None else str(st.session_state.somme)
st.text_input("Somme", value=resultat, disabled=True)