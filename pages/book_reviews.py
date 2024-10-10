import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')

#importando os Df
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100 = pd.read_csv("datasets/Top-100 Trending Books.csv")

#fazendo o selectbox
books = df_top_100["book title"].unique()
book = st.sidebar.selectbox('Qual livro você quer selecionar?', books)

#criando o filtro
df_book = df_top_100[df_top_100['book title'] == book]
df_review = df_reviews[df_reviews['book name'] == book]

#criando cartões
book_title = df_book['book title'].iloc[0]

book_genre = df_book['genre'].iloc[0]

book_price = f"$ {df_book['book price'].iloc[0]}"

book_rating = df_book['rating'].iloc[0]

book_year = df_book['year of publication'].iloc[0]

#fazendo o desing na pagina
st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric('Price', book_price) 
col2.metric('Rating', book_rating)
col3.metric('year', book_year)


st.divider()

for row in df_review.values:
    massage = st.chat_message(f"{row[4]}")
    massage.write(f"**{row[2]}**")
    massage.write(row[5])

