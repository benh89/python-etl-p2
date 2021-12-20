create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl2;
    
    DROP TABLE IF EXISTS petl2.t_movie_list;

    CREATE TABLE IF NOT EXISTS petl2.t_movie_list (
        title text,
        rated TEXT,
        released DATE,
        runtime INT,
        genre TEXT[],
        director TEXT,
        writers TEXT[],
        actors TEXT[],
        plot TEXT,
        awards TEXT,
        poster TEXT
        );
''')

insert_t_movie = ('''
    INSERT INTO petl2.t_movie_list 
   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
''')

