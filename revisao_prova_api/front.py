import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Atualizando painel..."):
        dados = obter_dados_meteorologicos()

    st.success("Painel atualizado.")
    st.subheader("Indicadores principais")

    col1, col2, col3 = st.columns(3)
    col1.metric(
        "🌡️ Temperatura",
        f"{dados['Temperatura']:.1f} °C"
    )
    col2.metric(
        "💧 Umidade",
        f"{dados['Umidade_rel']} %"
    )
    col3.metric(
        "🤒 Sensação Térmica",
        f"{dados['Sensacao']:.1f} °C"
    )


except Exception as erro:
    st.error(f"Erro ao carregar os dados: {erro}")
