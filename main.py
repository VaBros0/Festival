from api import get_films

def display_film_card(film, index=None):
    st.image(film['posterUrl'], width=200)
    st.write(f"Фильм: {film['nameRu']}")
    st.write(f"Рейтинг: {film['ratingKinopoisk']}")

    if isinstance(film['genres'], list):
        genres = film['genres']
        genres_str = ', '.join([g['genre'] for g in genres])
        st.write(f"Жанры: {genres_str}")
    else:
        st.write(film['genres'])

    if 'kinopoiskId' in film:
        button_key = f"add_{film['kinopoiskId']}"
    else:
        button_key = f"add_{film['nameRu']}_{film['year']}"

    # Задача: Сделать так, чтобы при первом нажатии фильм добавлялся в избранное
    if st.button(f"Добавить в избранное: {film['nameRu']}", key=button_key):
        if 'favorites' not in st.session_state:
            st.session_state['favorites'] = []
        else:
            st.session_state['favorites'].append(film)
            st.success(f"Фильм {film['nameRu']} успешно добавлен в избранное!")
    

st.title('Фильмотека')
films = get_films()

for index, film in enumerate(films):
    if index > 0:
        display_film_card(film, index=index)

st.sidebar.title("Избранное")
