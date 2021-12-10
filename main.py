import pgsql
import sql
import requests
from pgsql import query
from pgsql import query_create
from pgsql import query_insert
import json
from datetime import datetime
import pandas as pd


def parsing_json():
    lineList = []
    with open('.//datasets//json//movies.json', 'r') as f:
        data = json.loads(f.read())
        lineList.append(data)
        f.close();
    for line in lineList:
        # print(line[0], "\n", line[1], "\n", line[2])
        # print(type(line))
        i = 0
        newList = []
        for i in range(len(line)):
            for key, val in line[i].items():
                for j in [2018, 2019, 2020, 2021]:
                    if j in line[i].values():
                        newList.append(line[i])
        i += 0
        # print(newList)
        # print(newList)
        # _list=[]
        # for col in newList:
        # if col['year'] >= 2018:
        # if 'English' in col['Language']:
        # if col['title'] != ' ':
        # _list.append(col['title'])
        # print(unique(_list))
        # print(len(_list))
        movie_list = []
        for item in newList:
            movie_list.append(item['title'])
            # print(movie_list)
        new_movie_list = {}
        new_movie_list = list(set(movie_list))


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

    parsing_json()
    # get some movie data from the API

    #print(new_movie_list)
    """
    newMovies = {}
    newFile = open("newMovies.json",'w')
    for mv in new_movie_list:
        newMovies[mv]=get_movie_data(mv)
        #print(newMovies)
    #create the new Json file
    json.dump(newMovies,newFile,indent=4)
    """
    with open("newMovies.json", 'r')as f:
        _movies = json.loads(f.read())

# repeat the previous steps
    lan = 'English'
    engMovList = []
    #for i in range(len(_movies)):
    for key,val in _movies.items():
        for k,v in val.items():
            if 'Language' in k:
                if 'English' in v:
                    engMovList.append(val)
    #print(engMovList)
    #print(len(_movies))
    columns = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Awards", "Poster"]
    new_col_sets = []
    for element in engMovList:
       _value = {key: element[key] for key in columns}
       new_col_sets.append(_value)
    #print(len(new_col_sets))
    final_movies = []
    for newEle in new_col_sets:
      if "N/A" not in newEle.values():
          final_movies.append(newEle)
          #print(len(final_movies))

##For a clean data purpose: converting & transforming
    """
    for item in final_movies:
        _tab = []
        _tab.append(item["Title"])


        query_insert(sql.insert_t_movie, _tab)
        #print(_tab)
    """
# finalizing
    for item in final_movies:
        _tab = []
        _tab.append(item["Title"])
        _tab.append(item["Rated"])
        _tab.append(datetime.strptime(item["Released"], "%d %b %Y"))
        #_tab.append(item["Released"])
        _tab.append(int(item["Runtime"][0:3].strip()))
        _tab.append(item["Genre"].split(","))
        _tab.append(item["Director"])
        _tab.append(item["Writer"].split(","))
        _tab.append(item["Actors"].split(","))
        _tab.append(item["Plot"].strip(','))
        _tab.append(item["Awards"].split(","))
        _tab.append(item["Poster"])
        #if 'N/A' not in list(filter(lambda mv: 'N/A' in mv, _tab)):
        query_insert(sql.insert_movie, _tab)

        #print(len(_tab))"""


#r = json.dumps(data, indent=3)
#print("with PrettyPrint: \n", r)







