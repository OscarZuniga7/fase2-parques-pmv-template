import streamlit as st

st.set_page_config(
    page_title="Gestión de Parques Naturales",
    page_icon="🌳",
    layout="wide"
)

st.title("🌳 Sistema Integral de Gestión de Parques Naturales")

st.caption(
    "UNAB – TDFI103 Bases de Datos | "
    "Proyecto Semestral Fase 2 – Caso 1"
)

st.success("Aplicación Streamlit inicializada correctamente.")

st.subheader("Bienvenidos al Producto Mínimo Viable (PMV)")

st.write(
    "Esta aplicación permitirá gestionar parques naturales, "
    "especies, visitantes y excursiones utilizando MySQL."
)

st.info(
    "Próximamente incorporaremos autenticación, "
    "inscripciones, operaciones CRUD y dashboard."
)
