import pgsql
import sql
import requests
from pgsql import query
from pgsql import query_create
from pgsql import query_insert
import json
from datetime import datetime
import pandas as pd



def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


## Using for the purpose of testing data
def unique(list1):
    # initialize a null list
    unique_list = []
    new=[]
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print(x)


if __name__ == '__main__':
    query_create(sql.create_schema)

    #print(get_movie_data('Inside Llewyn Davis'))
    #print(get_movie_data('12 Strong'))
    # get some movie data from the API

    file = open('datasets/json/movies.json')
    data = json.load(file)     #data is a list;
    file.close()
    #movie = []
    for row in data:
        if row['year'] >= 2018:
            dataset = get_movie_data(row['title'])
            # dataset is a dict;
            if dataset['Response'] != 'False' and 'English' in dataset['Language'] and dataset['Title'] != 'N/A' and \
                    dataset['Rated'] != 'N/A' and dataset['Released'] != 'N/A' and dataset['Runtime'] != 'N/A' and \
                    dataset['Genre'] != 'N/A' and dataset['Director'] != 'N/A' and dataset['Writer'] != 'N/A' and \
                    dataset['Actors'] != 'N/A' and dataset['Plot'] != 'N/A' and dataset['Awards'] != 'N/A' and \
                    dataset['Poster'] != 'N/A' and datetime.strptime(dataset['Released'], "%d %b %Y").year > 2017:
                #movie_no_dup = list(set(movie))  #this is a empty list;
                #if dataset['Title'] not in movie_no_dup:
                    _tab = []
                    _tab.append(dataset["Title"])
                    _tab.append(dataset["Rated"])
                    _tab.append(datetime.strptime(dataset["Released"], "%d %b %Y"))
                    # _tab.append(item["Released"])
                    _tab.append(int(dataset["Runtime"][0:3].strip()))
                    _tab.append(dataset["Genre"].split(","))
                    _tab.append(dataset["Director"])
                    _tab.append(dataset["Writer"].split(","))
                    _tab.append(dataset["Actors"].split(","))
                    _tab.append(dataset["Plot"].strip(','))
                    _tab.append(dataset["Awards"].split(","))
                    _tab.append(dataset["Poster"])
                    # if 'N/A' not in list(filter(lambda mv: 'N/A' in mv, _tab)):
                    query_insert(sql.insert_t_movie, _tab)
                    #movie.append(dataset['Title'])
                    #print(len(_tab))




#r = json.dumps(data, indent=3)
#print("with PrettyPrint: \n", r)







