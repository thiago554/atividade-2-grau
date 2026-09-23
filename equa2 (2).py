import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ========================================
# CONFIGURAÇÃO DA PÁGINA
# ========================================

st.set_page_config(
    page_title="MatFuturo - Equação do 2º Grau",
    page_icon="📈",
    layout="centered"
)

# ========================================
# CORES E ESTILO DA ESCOLA
# ========================================

st.markdown("""
    <style>

        /* Fundo principal */
        .stApp {
            background-color: #E8F5E9;
        }

        /* Título principal */
        h1 {
            color: #2E7D32 !important;
            text-align: center;
        }

        /* Subtítulos */
        h2, h3 {
            color: #2E7D32 !important;
        }

        /* Textos */
        p, label {
            color: #1B1B1B !important;
        }

        /* Botão */
        .stButton > button {
            background-color: #43A047;
            color: white;
            border-radius: 10px;
            border: none;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
        }

        .stButton > button:hover {
            background-color: #2E7D32;
            color: white;
        }

    </style>
""", unsafe_allow_html=True)


# ========================================
# CABEÇALHO
# ========================================

st.markdown(
    "<h1>📈 MatFuturo</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>App - Equação do 2º Grau</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Cores da escola: verde</p>",
    unsafe_allow_html=True
)


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
# TÍTULO DA CALCULADORA
# ========================================

st.title("Equação do 2º Grau")

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
