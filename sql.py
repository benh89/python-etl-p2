create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl2;
    
    DROP TABLE IF EXISTS petl2.movie_list;
    DROP TABLE IF EXISTS petl2.t_movie_list;
    
    CREATE TABLE IF NOT EXISTS petl2.movie_list (
        title text,
        rated text,
        released text,
        runtime text, 
        genre text[],
        director text,
        writers text[],
        actors text[],
        plot text,
        awards text,
        poster text
        );
    CREATE TABLE IF NOT EXISTS petl2.t_movie_list (
        title text
 

        );
''')

insert_movie = ('''
    INSERT INTO petl2.movie_list
   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
''')
insert_t_movie = ('''
    INSERT INTO petl2.t_movie_list (Title)
   VALUES(%s);
''')

