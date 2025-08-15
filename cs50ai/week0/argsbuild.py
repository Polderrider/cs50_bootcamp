from sys import argv
from pathlib import Path

# command line accepts only one arg: name of folder holding files
folder_name = argv[1]

# use arg[1] + pathlib to navigate to folder
# Create a path object
dir_path = Path(folder_name)
cwd = Path.cwd()
# return all csv files inside foldername
files = [cwd/file for file in dir_path.glob('*.csv')]



# files = list(dir_path.glob("*.csv"))
print(files)
print(files[1])

# return a list use pathlib to extract file_name + .ext for those files ending in .csv
#  iterate through list using conditional to match correct filepath to function to open file