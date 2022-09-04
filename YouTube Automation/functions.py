from pytube import YouTube,Playlist,Channel
from pytube.cli import on_progress
import requests #this will only use for to download thumbnail
import os 
import shutil
import datetime
import imdb

data_path = os.getcwd() + "/data"
v_storage_path = "E:/YT_V_Data"
max_v_len = 300 #minute

t = datetime.datetime.now()
t = t.strftime("%d/%h/%y %H:%M")

try:    
    with open(f"{data_path}/chnl_url_id.txt","r", encoding='utf-8') as f:
        data = f.readlines() 
        #channel_urls list store only urls of channel from chnl_url_id file
        channel_urls = []
        for url in data:
            channel_urls.append((url.split('###')[2]))
except:
    print("'chnl_url_id.txt' file not found.(functions.py)")
    with open(f"{os.getcwd()}\data\Error_log.txt", "a") as Error_log:
        Error_log.write(f"\n{t}\t|  File_Not_Found\t|  'chnl_url_id.txt' file not found.(functions.py)")
    

#----------get_latest_video------------------------
def get_latest_video_update():
    with open(f"{data_path}/channel_video_data.txt","r", encoding='utf-8') as f:
        data = f.readlines() 
        pre_vid = [] #store last fetched video's id for further comparision
        for id in data:
            pre_vid.append((id.split('####')[1]))
    
    # print(f"len pre vid: {len(pre_vid)}")
    # print(pre_vid) 
    # print(f"len channel urls: {len(channel_urls)}")   
    # print("============================")
    #data store list of details(ch_name,cur_v_title,cur_v_url) and return by get_latest_video_update function
    data = []
    
    
    #if data is present then this if part will execute And compaire previous and current data
    if len(pre_vid) > 0: 
        for i in range(len(channel_urls)):        
            ch_name = Channel(channel_urls[i]).channel_name #fetch channel name from channel url 
            cur_v_url =str(Channel(channel_urls[i]).video_urls[:1]) #fetch cur_v_url using channel url in string format
            cur_vid = YouTube(cur_v_url).video_id #fetch cur_vid using cur_vid_url 
            cur_v_title = YouTube(cur_v_url).title #fetch cur_v_title using cur_v_url
            cur_v_len = YouTube(cur_v_url).length #fetch cur-v_lenght using cur_v_url
            
            # print(f"{}")
            try:            
                if cur_vid not in pre_vid:
                    # print(f"{cur_vid} -- {ch_name}")
                    # print("\t yes not in pre vid")
                    if (cur_v_len <max_v_len and ('trailer' in cur_v_title.lower())) or ch_name == "JoBlo Movie Clips": #check video length must be less than 5min
                        data.append([ch_name,cur_v_title,cur_v_url])
            except:
                pass
    
        #if someone delete channel_video_data file or erase previous data then this else will execute
        #this will not compaire previous and current data  
    else:
        for i in range(len(channel_urls)):        
            ch_name = Channel(channel_urls[i]).channel_name #fetch channel name from channel url 
            cur_v_url =str(Channel(channel_urls[i]).video_urls[:1]) #fetch cur_v_url using channel url in string format
            cur_vid = YouTube(cur_v_url).video_id #fetch cur_vid using cur_vid_url 
            cur_v_title = YouTube(cur_v_url).title #fetch cur_v_title using cur_v_url
            cur_v_len = YouTube(cur_v_url).length #fetch cur-v_lenght using cur_v_url
            
            if cur_v_len <max_v_len and ('trailer' in cur_v_title.lower()): #check video length must be less than 5min
                data.append([ch_name,cur_v_title,cur_v_url])
    
    return data #return final data by function            
    
        
#----------------update latest_video file----------------
def update_latest_vid_file():
    try:
        with open(f"{data_path}/channel_video_data.txt","w", encoding='utf-8') as f:
            for i in range(len(channel_urls)):            
                v_url = str(Channel(channel_urls[i]).video_urls[:1]) #fetchh video url using channel urls                        
                ch_name = Channel(channel_urls[i]).channel_name
                v_id = YouTube(v_url).video_id
                v_title = YouTube(v_url).title    
                    
                f.write(f"{ch_name}####{v_id}####{v_title}\n")
    except:
        print("'channel_video_data.txt' file not found.(functions.py)")
        with open(f"{os.getcwd()}\data\Error_log.txt", "a") as Error_log:
            Error_log.write(f"\n{t}\t|  File_Not_Found\t|  'channel_video_data.txt' file not found.(functions.py)")


#-------------get videos for specific channel--------
def get_video(chnl_url,max_v):
    #fetch list of videos using channel url 
    ch_name = Channel(chnl_url).channel_name
    urls =Channel(chnl_url).video_urls[:max_v]    
    data = [] #store video's title and url
    for i in range(len(urls)):
        v_title = YouTube(urls[i]).title
        v_len = YouTube(urls[i]).length #fetch cur-v_lenght using cur_v_url
        
        if (v_len <max_v_len and ('trailer' in v_title.lower())) or ch_name == "JoBlo Movie Clips": #check video length must be less than 5min   
            data.append([v_title,urls[i]])  #urls[i] because video urls are in list type   
    return data

#-------------download Videos------------------------- 
def download_video(vid_url):
    v_len = YouTube(vid_url).length #fetch cur-v_lenght using cur_v_url
    v_title = YouTube(vid_url).title 
        
    #fetching channel url using video url with YouTube class
    #then fetching channel name using channel url with Channel url
    chnl_name = Channel(YouTube(vid_url).channel_url).channel_name
    
    #windown did't allow to create file name that include these chars \/"?|>:<*
    #So to prevent from error while creating folder and file name this for loop removes 
    #these characters from video title  
    not_include = '\/"?|>:<*'
    for i in range(len(not_include)):
        if not_include[i] in v_title:
            v_title = v_title.replace(not_include[i],"")
    
    #set path where downloaded data going to be store
    path = f"{v_storage_path}/{chnl_name}/{v_title}"
    
    try:            
        v = YouTube(vid_url, on_progress_callback=on_progress)
        #download video file in highest resolution from YouTube to path
        v.streams.get_highest_resolution().download(path)
        print()
        
        try:
            # create file that contain video keywords to path
            with open(f"{path}/keywords.txt","w", encoding='utf-8') as d:
                kw = YouTube(vid_url).keywords
                for i in range(len(kw)):
                    d.write(f"{kw[i]},\n")
                    
            #create file that contain video title(same as on YouTube) to path 
            #because on top we remove special characters from title to create file name   
            with open(f"{path}/title.txt","w", encoding='utf-8') as d:
                d.write(YouTube(vid_url).title.title())                
                
            
            des_intro = f'#{YouTube(vid_url).title.title().replace(" ", "")} #Official #Trailer #2022\n\n... Like/Dislike the video, Sharing is Caring, and Hit the bell icon. Witty Comments pinned.\n'
            des_outro = "\n\n▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\nThanks for Watching.\nAnd don't forget to Like and  Subscribe.\nhttps://www.youtube.com/channel/UCvxCCtzEsEPPBBpkzPd9zxA?sub_confirmation=1"
            des_mid = search_for_movie(v_title)
            
            #create file that contain video Description to path    
            with open(f"{path}/description.txt","w", encoding='utf-8') as d:
                d.write(f"{des_intro}\n\n{YouTube(vid_url).description}\n\n")
                d.write(des_mid)
                d.write(f"\n\n{des_outro}")
                
                
            #download video thumbnail in highest resolution to path      
            response = requests.get(f"https://img.youtube.com/vi/{YouTube(vid_url).video_id}/maxresdefault.jpg")
            with open(f"{path}/thumbnail.jpg","wb") as d:
                d.write(response.content)    
                
            return f"Download Complete --> {v_title}" #send massage in return with video title    
        except:
            shutil.rmtree(path, ignore_errors = False)
            return "Error! while creating other(keywords,title,description,thumbnail) files."
    except Exception as e:
        with open(f"{os.getcwd()}\data\Error_log.txt", "a") as Error_log:
            Error_log.write(f"\n{t}\t|  Download_Error\t|  Error! While downloading video. {v_title}")
        return f"Error! While downloading video. {e.__class__.__name__}"


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