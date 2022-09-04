import time

def upload(video_data):
    video_path = video_data[0]    
    # video_data[1] --> title   
    # video_data[2] --> description
    # video_data[3] --> keyword
    video_thumbnail_path = video_data[4]
      
    
    with open(video_data[1], "r", encoding='utf-8') as f:
        video_title = f.readline() 
        
    with open(video_data[2], "r", encoding='utf-8') as f:
        video_description = f.read()
            
    with open(video_data[3], "r", encoding='utf-8') as f:
        data = f.readlines()
        video_keyword = ""
        for i in range(len(data)):
            video_keyword = video_keyword + data[i]        
        video_keyword = video_keyword.replace('\n', '')
        
    
    a = str(video_title.split()[0])    
    counter = 0    
    with open("D:\\Programs\\python\\pytube\\data\\uploaded_videos.txt", 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in range(len(data)):
            if a in data[i]:
                counter = counter + 1
            else:
                pass
    
    # print(counter)  
    if counter == 0:           
            
        # print(video_title)
        # time.sleep(0.5)
        # print(video_description)
        # time.sleep(0.5)
        # print(video_keyword)
        # time.sleep(1.5)
        
        db_update(video_title)
        message = f"{video_title}--> is uploaded Successfully"    
        return message
    else:
        message = f"{video_title}--> is already uploaded."    
        return message


def db_update(title):
    data_path = "D:/Programs/python/pytube/data"    
    with open(f"{data_path}/uploaded_videos.txt","a", encoding='utf-8') as f:
        f.write(f"{title}\n")