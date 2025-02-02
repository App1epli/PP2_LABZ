#2_nd exercise: Write a function that returns a sublist of movies with an IMDB score above 5.5

def high_imdb(movies):
    movie_l=[]
    for x in movies:
        if x["imdb"] > 5.5:
            movie_l.append(x["name"])
    return movie_l

movies = [
    {
        "name": "Fight Club",
        "imdb": 8.8,
        "category": "Drama"
    },
    {
        "name": "The Intouchables",
        "imdb": 8.5,
        "category": "Biography"
    },
    {
        "name": "Requiem for a Dream",
        "imdb": 8.3,
        "category": "Drama"
    },
    {
        "name": "The Karate Kid",
        "imdb": 7.2,
        "category": "Action"
    },
    {
        "name": "Saw",
        "imdb": 7.6,
        "category": "Horror"
    },
    {
        "name": "Final Destination",
        "imdb": 6.7,
        "category": "Horror"
    },
    {
        "name": "Scary Movie",
        "imdb": 6.2,
        "category": "Comedy"
    },
    {
        "name": "Dumb and Dumber",
        "imdb": 7.3,
        "category": "Comedy"
    },
    {
        "name": "It",
        "imdb": 7.3,
        "category": "Horror"
    },
    {
        "name": "BoJack Horseman",
        "imdb": 8.8,
        "category": "Animation"
    },
    {
        "name": "Rick and Morty",
        "imdb": 9.1,
        "category": "Animation"
    },
    {
        "name": "Breaking Bad",
        "imdb": 9.5,
        "category": "Crime"
    },
    {
        "name": "The Boys",
        "imdb": 8.7,
        "category": "Action"
    },
    {
        "name": "Disaster Movie",
        "imdb": 2.3,
        "category": "Comedy"
    }
]



print(high_imdb(movies))