import csv

filepath = "/Users/home/Documents/programming/cs50/cs50ai/week0/small/movies.csv"


with open(filepath, newline='') as f:
    
    lines = csv.reader(f, delimiter=',')

    next(lines)
    # populate movie data dict
    movies_dict = {}
    for line in lines:
        movie_id, title, release_year = line

        movie_data = {}
        movie_data["title"] = title
        movie_data["release year"] = release_year
        movie_data["movie stars"] = "data"
        movies_dict[movie_id] = movie_data

        
    
    

print(movies_dict)
         




            

        
