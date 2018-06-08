import json
from itertools import *
import matplotlib.pyplot as plt

filenames = [
    "data/dblp-ref/dblp-ref-0.json",
    "data/dblp-ref/dblp-ref-1.json",
    "data/dblp-ref/dblp-ref-2.json",
    "data/dblp-ref/dblp-ref-3.json"
]

wanted_features = [
    "authors",
    # "references",
    "year",
    # "id",
    # "title"
]

def filter_goods(d):
    return {i: maybe(lambda i: d[i], i) for i in wanted_features}
    # return {i: d[i] for i in wanted_features}

def read_data(filename):
    """returns an list of dictionaries"""
    with open(filename, "r") as file:
        return [filter_goods(json.loads(line)) for line in file]

def line_data(line):
    return json.load

def get_all_features(filename):
    """gets the set of all features from a filename
    this waws used to verify that the features were consistent"""
    s = set()
    with open(filename, "r") as file:
        for line in file:
            s = s.union(json.loads(line).keys())
        return s

def get_all_authors(filename):
    """gets the set of all authors from a filename"""
    s = set()
    with open(filename, "r") as file:
        for line in file:
            try:
                authors = json.loads(line)["authors"]
            except KeyError as e:
                print(e)
                authors = []
            s = s.union(authors)
    return s

def get_all_id(filename):
    """gets the set of all ids from a filename"""
    s = set()
    with open(filename, "r") as file:
        for line in file:
            try:
                id = json.loads(line)["id"]
            except KeyError as e:
                print(e)
                id = []
            s = s.union(id)
        return s

def get_all_year(filename):
    """gets the set of all years from a filename"""
    s = set()
    with open(filename, "r") as file:
        for line in file:
            try:
                year = json.loads(line)["year"]
            except KeyError as e:
                print(e)
                year = None
            s.add(year)
        return s

def maybe(f, x):
    try:
        return f(x)
    except Exception as e:
        return None

def main():
    pass

def since_first(years):
    if years == []:
        return []
    else:
        new_years = years.copy()
        new_years.sort()
        new_years = [i - new_years[0] for i in new_years]
        return new_years

def get_author_dict():
    out = dict()
    for filename in filenames:
        for d in read_data(filename):
            for author in d["authors"]:
                try:
                    out[author].append(d["year"])
                except KeyError:
                    out[author] = [d["year"]]
    return out

def map_dict(d_in, f):
    d_out = dict()
    return {key: f(d_in[key]) for key in d_in.keys()}

def to_years_since(d_in):
    return map_dict(d_in, since_first)

def get_yearly_events():
    pass

def count_uniq(vals):
    pass

def get_latest_year(d_in):
    return max(map(max, d_in.values()))

if __name__ == '__main__':
    for filename in filenames:
        print(get_all_year(filename))
    # print(list(read_data("data/dblp-ref/dblp-ref-0.json")))
