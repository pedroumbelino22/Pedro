#o que é? Biblioteca que puxa informações financeiras do yahho
import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime

#como usar?

#titulo no site
st.markdown('# Analisando empresas')

#caixa de texto da empresa buscada
st.text_input('Ticker Code', key = 'tickercode',value = 'GOOG')

#titulo das ultimas noticias
st.markdown(f'## Últimas Noticias da {st.session_state.tickercode}:')

#captura nome da empresa
ticker = st.session_state.tickercode

#puxa dados no sistema yf
data = yf.Ticker(ticker)

#tabela data noticias principais e filtro por coluna
data_news = pd.DataFrame(data.news)
data_news2 = data_news[["title","publisher","link","relatedTickers"]]

#Mostrar últimas noticias no site
st.dataframe(data_news2)

#tabela de historico das ações
end_date = datetime.now().strftime('%Y-%m-%d')
data_history = data.history(period = 'max',start = '2022-3-16', end = end_date, interval = '5d')
data_history = data_history.reset_index() #retirar o cabeçalho

#opção de selecionar eixo x e y do gráfico
ex = st.selectbox('Eixo x:', data_history.columns)
ey = st.selectbox('Eixo y:', data_history.columns)

#Mostrar título e gráfico
st.markdown(f'## Gráfico: x: {ex} e y: {ey}')
st.line_chart(data_history, x = ex, y = ey)

print(data_history)
