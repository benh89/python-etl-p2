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


if __name__ == '__main__':
    lineList = []
    with open('.//datasets//json//movies.json', 'r') as f:
        data = json.loads(f.read())
        lineList.append(data)
        f.close();
    #print(lineList)

    ##for row in lineList:  --> that will be error!!
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
            print(_tab)