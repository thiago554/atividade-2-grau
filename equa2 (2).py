
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ========================================
# CONFIGURAÇÃO DA PÁGINA
# ========================================

st.set_page_config(
    page_title="Equação do 2º Grau",
    page_icon="📈",
    layout="centered"
)

st.markdown("""
    <style>
        /* Fundo principal da página */
        .stApp {
            background-color: #0D47A1;
        }
    </style>
""", unsafe_allow_html=True)

# ========================================
# CAMINHO DA IMAGEM
# ========================================

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "unnamed.jpg"

if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )
else:
    st.warning("A imagem unnamed.jpg não foi encontrada. ⚠️")


# ========================================
# TÍTULO
# ========================================

st.title("📈 Equação do 2º Grau")

st.write("Equação no formato:")

st.latex(r"ax^2 + bx + c = 0")


# ========================================
# ENTRADA DOS VALORES
# ========================================

a = st.number_input(
    "Digite o valor de a",
    value=1.0,
    step=1.0
)

b = st.number_input(
    "Digite o valor de b",
    value=0.0,
    step=1.0
)

c = st.number_input(
    "Digite o valor de c",
    value=0.0,
    step=1.0
)


# ========================================
# BOTÃO CALCULAR
# ========================================

if st.button("Calcular", use_container_width=True):

    # ========================================
    # VERIFICA SE É REALMENTE DO 2º GRAU
    # ========================================

    if a == 0:

        st.error(
            "O valor de 'a' não pode ser 0 em uma equação do 2º grau."
        )

    else:

        # ====================================
        # MOSTRA A EQUAÇÃO
        # ====================================

        st.subheader("Equação")

        # Monta a equação visualmente
        if b >= 0:
            parte_b = f"+ {b:g}x"
        else:
            parte_b = f"- {abs(b):g}x"

        if c >= 0:
            parte_c = f"+ {c:g}"
        else:
            parte_c = f"- {abs(c):g}"

        st.latex(
            f"{a:g}x^2 {parte_b} {parte_c} = 0"
        )

        # ====================================
        #
```
