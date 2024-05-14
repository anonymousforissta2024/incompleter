#Source: https://stackoverflow.com/questions/73006690/typeerror-builtin-function-or-method-object-is-not-iterable-in-recommendation
movie_list = movies['title'].values
selected_movie_name = st.selectbox("Type or select a movie from the dropdown", movie_list)