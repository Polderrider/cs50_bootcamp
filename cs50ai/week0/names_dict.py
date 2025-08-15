import csv

filepath = "/Users/home/Documents/programming/cs50/cs50ai/week0/small/people.csv"


with open(filepath, newline='') as f:
    
    lines = csv.reader(f, delimiter=',')
    next(lines)
    # return lines

    # populate names dict with movie star info
    names_dict = {}
    for line in lines:
        name_id, name, yob = line
        
        if name not in names_dict:
            id = set()
            id.add(name_id)
            names_dict[name] = id
        
        else:
            ids = names_dict.get(name)
            ids.add(name_id)
            names_dict[name] = ids
            

print(names_dict)
         




            

        
