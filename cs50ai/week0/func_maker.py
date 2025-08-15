import csv


def main():

    stars_filepath = "/Users/home/Documents/programming/cs50/cs50ai/week0/small/stars.csv"
    file = csv_to_list_object(stars_filepath)
    print(file)
    stars = [(row[0], row[1]) for row in file]
    print(stars)


if __name__ == "___main__":
    main()


# create stars (person_id, movie_id)
def csv_to_list_object(filepath):

    with open(filepath, newline='') as f:
        
        lines = csv.reader(f, delimiter=',')
        next(lines)
    
    return [(line[0], line[1]) for line in lines]

    
    