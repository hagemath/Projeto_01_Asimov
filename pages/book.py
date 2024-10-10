import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')

#importando os arquivos csv
df_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
df_reviews = pd.read_csv("datasets/customer reviews.csv")

#colocando o seletor para cada um dos livros
books = df_100_books['book title'].unique()
book = st.sidebar.selectbox("Escolha o seu livro", books)


#conectando os filtros
df_book_select = df_100_books[df_100_books['book title'] == book]
df_review_select = df_reviews[df_reviews['book name'] == book]

#Criando cartoes
book_name = df_book_select['book title'].iloc[0]

book_price = f"$ {df_book_select['book price'].iloc[0]}"

book_year = df_book_select['year of publication'].iloc[0]

book_rating = df_book_select['rating'].iloc[0]

book_genre = df_book_select['genre'].iloc[0]

#fazendo desing
st.title(book_name)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric('Price', book_price)
col2.metric('Rating', book_rating)
col3.metric('Year', book_year)

st.divider()

#colocando o review
for text in df_review_select.values:
    message = st.chat_message(f'{text[4]}')
    message.write(f"**{text[2]}**")
    message.write(text[5])