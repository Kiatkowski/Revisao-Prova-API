# Monitoramento Meteorológico — Jaraguá do Sul/SC

Aplicação simples em Python que consulta dados climáticos em tempo real (temperatura, umidade, vento, precipitação e sensação térmica) e exibe as informações em um painel web interativo.

## Arquivos do Projeto

* **`consumidor_api.py`**: Faz a requisição HTTP para a API meteorológica e extrai os dados atuais.
* **`front.py`**: Interface visual feita com Streamlit para mostrar os indicadores na tela.
* **`api-meteorologica-offline/`**: API local em FastAPI para testes sem internet.

## Como Executar

1. **Instale as dependências:**
   ```bash
   pip install streamlit requests fastapi uvicorn
   ```

2. **Inicie o painel (Streamlit):**
   ```bash
   python -m streamlit run front.py
   ```

3. *(Opcional)* **Inicie a API local offline:**
   ```bash
   cd api-meteorologica-offline
   uvicorn app.main:app --reload
   ```
