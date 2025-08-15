import csv


def open_and_read_one_line_at_a_time_using_yield(file):

    with open(file, "r") as f:
        rows = csv.reader(f)
        rows.__next__()
        for row in rows:
            yield row



for row in open_and_read_one_line_at_a_time_using_yield('small/movies.csv'):
    print(row)
