import media
import fresh_tomatoes

# defined the frist movie
finding_nemo = media.movie(
    "Finding Nemo", "Finding Nemo",
    "https://tse2.mm.bing.net/th?id=OIP.JAw89TrQBkzqKdg5aEXCZgHaKj&pid=15.1&P=0\
    &w=300&h=300",
    "https://youtu.be/eMZsqKwoGdE"
)

# defined the second movie
school_of_rock = media.movie(
    "School of Rock", "school_of_rock",
    "https://tse2.mm.bing.net/th?id=OIP.Qus56aXZpxlUh7EZQbOCRwHaK-&pid=15.1&P=0\
    &w=300&h=300",
    "https://youtu.be/GLojx1W1BBA"
)

# defined the third movie
Hermano = media.movie(
    "Hermano", "Hermano",
    "http://www.impawards.com/intl/misc/2010/posters/hermano.jpg",
    "https://youtu.be/YxWDDwEdMO4"
)

# put it movies array
movies = [finding_nemo, school_of_rock, Hermano]
# open movies
fresh_tomatoes.open_movies_page(movies)
