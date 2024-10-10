import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title("Ache o seu :red[Livro]")
st.divider()
#importando os arquivos csv
df_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
df_100_books = df_100_books.drop('url', axis=1)
df_reviews = pd.read_csv("datasets/customer reviews.csv")

#criando o filtro
price_max = df_100_books['book price'].max()
price_min = df_100_books['book price'].min()
genre = df_100_books['genre'].unique()

filter = st.sidebar.slider("Price Range", price_min, price_max, price_max)
filter2 = st.sidebar.selectbox('Qual gênero você quer?', genre)
df_books = df_100_books[(df_100_books['book price'] <= filter)]
df_books

st.title("Aqui temos os :red[Gráficos]")

#fazendo os gráficos
col1, col2 = st.columns(2)
fig = px.bar(df_books['year of publication'].value_counts())
fig2 = px.histogram(df_books.groupby('genre')[['rating']].mean().sort_values('rating'))

col1.plotly_chart(fig)
col2.plotly_chart(fig2)


