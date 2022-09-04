import os
import shutil
from upload import *

yt_data_path = "E:\YT_V_Data"

ch_fol = os.listdir(yt_data_path)
# print(ch_fol)

if len(ch_fol)>0:
    for i in range(len(ch_fol)):        
        path = os.path.join(yt_data_path, ch_fol[i])
        v_fol = os.listdir(path)
        if len(v_fol)>0:   
            video_data = [None]*5         
            for j in range(len(v_fol)):                    
                print(f"\t {v_fol[j]} is now uploading")
                path = os.path.join(yt_data_path, ch_fol[i],v_fol[j])
                v_data =  os.listdir(path)
                for k in range(len(v_data)):
                    if v_data[k][-4:] == ".mp4":
                        video_data[0] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                        
                    elif v_data[k] == "title.txt":
                        video_data[1] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                        
                    elif v_data[k] == "description.txt":
                        video_data[2] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                        
                    elif v_data[k] == "keywords.txt":
                        video_data[3] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                        
                    elif v_data[k] == "thumbnail.jpg":
                        video_data[4] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                    
                print(video_data)
                # print(upload(video_data))                                
                # shutil.rmtree(path, ignore_errors = False)
            # print("------------------------------------")
        else:
            print(f"\t'{ch_fol[i]}' --> This folder is empty.")
else:
    print(f"YT_V_Data is empty.")
