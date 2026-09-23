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
# CORES E ESTILO
# ========================================

st.markdown("""
    <style>

        .stApp {
            background-color: #E8F5E9;
        }

        h1 {
            color: #2E7D32 !important;
            text-align: center;
        }

        h2, h3 {
            color: #2E7D32 !important;
        }

        p, label {
            color: #1B1B1B !important;
        }

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
# NOME DO PROJETO
# ========================================

st.markdown(
    "<h1>📈 MatFuturo</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>App - Equação do 2º Grau</h3>",
    unsafe_allow_html=True
)


# ========================================
# CAMINHO DA IMAGEM
# ========================================

PASTA_APP = Path(__file__).parent

CAMINHO_LOGO = PASTA_APP / "unnamed.jpg"


# ========================================
# MOSTRA A IMAGEM
# ========================================

if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:

    st.warning(
        "A imagem unnamed.jpg não foi encontrada. ⚠️"
    )


# ========================================
# TÍTULO
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

    # ====================================
    # VERIFICA SE É EQUAÇÃO DO 2º GRAU
    # ====================================

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


        # ====================================
        # CÁLCULO DO DELTA
        # ====================================

        delta = b**2 - 4*a*c

        st.subheader("Cálculo do Delta")

        st.latex(
            rf"\Delta = b^2 - 4ac"
        )

        st.latex(
            rf"\Delta = ({b:g})^2 - 4({a:g})({c:g})"
        )

        st.latex(
            rf"\Delta = {delta:g}"
        )


        # ====================================
        # VERIFICA AS RAÍZES
        # ====================================

        if delta > 0:

            x1 = (-b + np.sqrt(delta)) / (2*a)
            x2 = (-b - np.sqrt(delta)) / (2*a)

            st.success("A equação possui duas raízes reais diferentes.")

            st.subheader("Raízes")

            st.latex(
                rf"x_1 = \frac{{-b + \sqrt{{\Delta}}}}{{2a}}"
            )

            st.latex(
                rf"x_1 = {x1:g}"
            )

            st.latex(
                rf"x_2 = \frac{{-b - \sqrt{{\Delta}}}}{{2a}}"
            )

            st.latex(
                rf"x_2 = {x2:g}"
            )


        elif delta == 0:

            x = -b / (2*a)

            st.success("A equação possui uma raiz real.")

            st.subheader("Raiz")

            st.latex(
                rf"x = \frac{{-b}}{{2a}}"
            )

            st.latex(
                rf"x = {x:g}"
            )


        else:

            st.warning(
                "A equação não possui raízes reais, pois o Delta é menor que zero."
            )
