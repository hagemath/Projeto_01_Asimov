#importando as biblotecas
import streamlit as st
import pandas as pd
import plotly. express as px

#configurando a tela do streamlit
st.set_page_config(layout="wide")

#lendo os arquivos csv
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100 = pd.read_csv("datasets/Top-100 Trending Books.csv")


#colocando os filtros de seleção
price_max = df_top_100["book price"].max()
price_min = df_top_100["book price"].min()

#definindo o filtro
filter = st.sidebar.slider('Price Range', price_min, price_max, price_max)

#colocando o filtro no df
df_books = df_top_100[df_top_100["book price"] <= filter]
df_books
#contruindo os gráficos
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books['book price'])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
