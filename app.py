import streamlit as st

st.set_page_config(page_title="Mi cuenta bancaria", page_icon="🏦", layout="wide")
st.title("🏦 Mi cuenta bancaria")
st.write("Explora cómo puede crecer tu ahorro durante 10 años.")
st.info("Selecciona Cuenta bancaria en el menú izquierdo para abrir la calculadora.")
st.markdown("""
### ¿Qué puedes hacer?
- Cambiar el saldo inicial, el depósito mensual y la tasa anual.
- Consultar el saldo, las aportaciones y los intereses de cada año.
- Filtrar los años y las series que aparecen en las gráficas.
- Descargar los datos filtrados en CSV.
""")
st.caption("Simulación educativa en unidades monetarias; no representa una oferta bancaria.")
