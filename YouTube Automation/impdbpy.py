import imdb

def search_for_movie(movie_title):
    mdb = imdb.IMDb()    
    
    movie_title = movie_title.lower()
    remove_word = ['trailer', 'official', 'teaser', 'hd', 'trailers', 'cinema', '4k', 'uhd', '|', '#', 'new', 'hindi']
    for i in range(len(remove_word)):
        if remove_word[i] in movie_title:
            movie_title = movie_title.replace(remove_word[i],"")
            
    movie_title = movie_title.split()
    
    search_m = movie_title[0]
    movie_data = ""
    try:
        for i in range(len(movie_title)):
            movie = mdb.search_movie(search_m)
            
            m_title = movie[0]['title'].lower()
            m_year = movie[0]['year'] 
            
            # print(f"{m_title}  {m_year}")
                    
            # if (search_m == m_title) and (m_year == 2022 or m_year == 2021):
            if (m_year >= 2021):
                m_id =  movie[0].getID()
                movie = mdb.get_movie(m_id)
                
                try:
                    plot = movie['plot']
                    movie_data = f"Plot: \n\t{str(plot).replace('[','').replace(']', '')}"
                except:
                    pass
                
                try:                
                    directors = movie['directors']
                    movie_data = movie_data + f"\n\nDirected by:"
                    for i in range(len(directors)):
                        movie_data = movie_data + f"\n\t{directors[i]}"
                except:
                    pass
                
                try:
                    writer = movie['writer']
                    movie_data = movie_data + f"\n\nWritten by:"
                    for i in range(len(writer)):
                        movie_data = movie_data + f"\n\t{writer[i]}"
                except:
                    pass

                try:
                    producers = movie['producers']
                    movie_data = movie_data + f"\n\nProduced by:"
                    for i in range(len(producers)):
                        movie_data = movie_data + f"\n\t{producers[i]}"
                except:
                    pass
                
                try:
                    cast = movie['cast']
                    movie_data = movie_data + f"\n\nCast:"
                    for i in range(len(cast)):
                        movie_data = movie_data + f"\n\t{cast[i]}"
                except:
                    pass
                
                return movie_data
            else:
                # if i+1 == len(movie_title):
                    # return movie_data 
                search_m = search_m + " " + movie_title[i+1]
    except:
        return ""
    

print(search_for_movie("Jurassic World: Dominion"))