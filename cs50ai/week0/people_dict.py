import csv
from sys import argv
from pathlib import Path


def main():

    # 1 command line arg: name of folder holding files
    stars, names_dict, people_dict, movie_dict = load_data(argv[1])

    

    print(f'stars:', len(stars))
    print(f'names:', len(names_dict))
    print(f'people:', len(people_dict))
    print(f'movies:', len(movie_dict))

    """   print(f'stars:', stars)
    print(f'names:', names_dict)
    print(f'people:', people_dict)
    print(f'movies:', movie_dict) """
   



####################################################
#                                                  #
#                   FUNCTIONS                      #
#                                                  #
####################################################


def load_data(folder_name):
    # path object for files folder
    dir_path = Path(folder_name)
    
    # return all csv files inside folder
    filepaths = list(dir_path.glob('*.csv'))
    # filepaths = [file for file in dir_path.glob('*.csv')]

    # create dicts to hold csv data 
    for filepath in filepaths:
        path = str(Path.cwd()/filepath)
        
        if 'stars' in path:
            stars = create_stars_dict(path)
        elif 'people' in path:
            names_dict = create_names_dict(path)
            people_dict = create_people_dict(path, stars)
        elif 'movies' in path:
            movie_dict = create_movie_dict(path, stars)
    return stars, names_dict, people_dict, movie_dict


def read_csv(file):
    """ generator returnss reads one line at at time of a given csv file into memory which avoids large datasets being read into memory  """

    with open(file, "r") as f:
        rows = csv.reader(f)
        rows.__next__()
        for row in rows:
            yield row


def create_stars_dict(file):
        return [(row[0], row[1]) for row in read_csv(file)]


def create_names_dict(file):
    names_dict = {}
    for row in read_csv(file):
        name_id, name, yob = row
        
        if name not in names_dict:
            id = set()
            id.add(name_id)
            names_dict[name] = id
        else:
            ids = names_dict.get(name)
            ids.add(name_id)
            names_dict[name] = ids
    
    return names_dict


def create_people_dict(file, stars_file):

    # populate people data dict 
    people_dict = {}
    for row in read_csv(file):

        person_id, name, yob = row

        people_data = {}
        people_data["name"] = name
        people_data["born"] = yob

        # populate people_dict with movie_data {title:  , yor:  , movie_stars (id->name)} 
        # return all movie_names from stars_list for each person_id        
        movie_names = set()
        for record in stars_file:
            if person_id == record[0]:
                movie_names.add(record[1])
        people_data["movies"] = movie_names

        people_dict[person_id] = people_data

    return people_dict


def create_movie_dict(file, stars_file):
    movies_dict = {}
    for row in read_csv(file):
        movie_id, title, release_year = row

        movie_data = {}
        movie_data["title"] = title
        movie_data["released"] = release_year

        actor_names = set()
        for record in stars_file:
            if movie_id == record[1]:
                actor_names.add(record[0])
        movie_data["actors"] = actor_names
    
        movies_dict[movie_id] = movie_data

    return movies_dict
   


if __name__ == "__main__":
    main()



    








""" 
# str -> str
# return person_id(s) for a given name

name1 = "Kevin Bacon"
name1_id = names_dict[name1]


# return movie_name(s) from stars.csv when given person_id
    # str list of tuples -> str
    # movie_names()

while stars:

 """





            

        
