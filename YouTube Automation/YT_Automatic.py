from functions import *
from upload import *
import os
import time
import shutil #it will help to delete the directory
from colorama import init, Fore, Style

init(convert=True)

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
c_reset = Style.RESET_ALL

print(cyan +"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░                                                                                                   ░░
░░           $$\     $$\                $$$$$$$$\        $$\                                         ░░
░░           \$$\   $$  |               \__$$  __|       $$ |                                        ░░
░░            \$$\ $$  /$$$$$$\  $$\   $$\ $$ |$$\   $$\ $$$$$$$\   $$$$$$\                          ░░
░░             \$$$$  /$$  __$$\ $$ |  $$ |$$ |$$ |  $$ |$$  __$$\ $$  __$$\                         ░░
░░              \$$  / $$ /  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |                        ░░
░░               $$ |  $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|                        ░░
░░               $$ |  \$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\                         ░░
░░               \__|   \______/  \______/ \__| \______/ \_______/  \_______|                        ░░
░░                                                                                                   ░░
░░  $$$$$$\              $$\                                        $$\     $$\                      ░░
░░ $$  __$$\             $$ |                                       $$ |    \__|                     ░░
░░ $$ /  $$ |$$\   $$\ $$$$$$\    $$$$$$\  $$$$$$\$$$$\   $$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   ░░
░░ $$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\ $$  _$$  _$$\  \____$$\\\_$$  _|  $$ |$$  __$$\ $$  __$$\  ░░
░░ $$  __$$ |$$ |  $$ |  $$ |    $$ /  $$ |$$ / $$ / $$ | $$$$$$$ | $$ |    $$ |$$ /  $$ |$$ |  $$ | ░░
░░ $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |$$ | $$ | $$ |$$  __$$ | $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | ░░
░░ $$ |  $$ |\$$$$$$  |  \$$$$  |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ | \$$$$  |$$ |\$$$$$$  |$$ |  $$ | ░░
░░ \__|  \__| \______/    \____/  \______/ \__| \__| \__| \_______|  \____/ \__| \______/ \__|  \__| ░░
░░                                                                                                   ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")

    
#checking for video updates
# time.sleep(3)
while True:
    print(yellow+ "Checking for video updates.")
    print("============================================")
    data = get_latest_video_update()
    # data = []
    if len(data) > 0:
        #Display latest videos updates list
        try:
            print(f"\tTotal Latest Video are :- {len(data)}")
            print("-----------------------------------------")
            for i in range(len(data)):
                print(cyan+ f"{i+1}. {data[i][0]} --> {data[i][1]} --> {data[i][2]}")
                time.sleep(0.3)
            print(yellow+ "-----------------------------------------")
        except:
            time.sleep(1)
            print(red+ "Error! occured while trying show Latest videos List.")
            print(yellow+ "-------------------------------------------------------")
        
        #Now download all videos available in latest video updates
        print("\n======================================")
        print("Now dowloading Videos.")
        print("----------------------------------------")
        print(green)
        for i in range(len(data)):
            try:                   
                message = download_video(data[i][2])
                print(green+ f"{message}")
            except:
                time.sleep(0.5)
                print(red+ "Something Wrong while Downloading")
        print(yellow+ "----------------------------------------")
        
        #now updating database in latest_videos.txt
        try:
            print("=======================================")
            print("Updating Database....")
            print("----------------------------------------")
            update_latest_vid_file()
            print(green+ "Databese is Updated Successfully")      
            print("=========================================")          
        except:
            print(red+ "Something wrong in database updation")
            print(yellow+ "=========================================")                
    else:
        print(red+ "No Video Updates Available.")
        print(yellow+ "============================================\n\n")

    time.sleep(1)
    if len(data) > 0:
        print(yellow+"===============================")
        print(green+"Uploading Videos....")
        print(yellow+"===============================")
    else:
        print(yellow+"===============================")
        print(green+"Uploading other remaining videos.")
        print(yellow+"===============================")
    #now upload all video available in YT_V_Data
    while True:
        try:
            yt_data_path = "E:\YT_V_Data" #main folder where downloaded video will going store
            ch_fol = os.listdir(yt_data_path) #get all channel folder and store in this variable
            upl_counter = 0;
            if len(ch_fol)>0: #checking ch_fol contain any Channel folder
                #this loop helps to check Videos folder from every individual Channel folder
                for i in range(len(ch_fol)): 
                    path = os.path.join(yt_data_path, ch_fol[i])
                    v_fol = os.listdir(path) #this store video folders list from path=E:\YT_V_Data\ch_fol
                    if len(v_fol)>0: #checking v_fol should contain any Video Folder.   
                        video_data = [None]*5 #in python we can't create empty list so i create list with none value of length 5.
                        #this loop helps to fetch videos data from every individual Video Folder.
                        for j in range(len(v_fol)):
                            path = os.path.join(yt_data_path, ch_fol[i],v_fol[j])
                            v_data =  os.listdir(path) #this video's data from path=E:\YT_V_Data\ch_fol\v_fol
                            #this loop helps to create path and pass as argumnet to upload video of every video's data
                            for k in range(len(v_data)):
                                if v_data[k][-4:] == ".mp4": #if v_data contain last '.mp4' word it store at video_data[0] 
                                    video_data[0] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                                    # video_data[0] = E:\YT_V_Data\ch_fol\v_fol\abc.mp4
                                    
                                elif v_data[k] == "title.txt":
                                    video_data[1] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                                    # video_data[1] = E:\YT_V_Data\ch_fol\v_fol\title.txt
                                    
                                elif v_data[k] == "description.txt":
                                    video_data[2] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                                    # video_data[2] = E:\YT_V_Data\ch_fol\v_fol\description.txt
                                    
                                elif v_data[k] == "keywords.txt":
                                    video_data[3] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                                    # video_data[3] = E:\YT_V_Data\ch_fol\v_fol\keywords.txt
                                    
                                elif v_data[k] == "thumbnail.jpg":
                                    video_data[4] = os.path.join(yt_data_path, ch_fol[i],v_fol[j], v_data[k])
                                    # video_data[4] = E:\YT_V_Data\ch_fol\v_fol\thumbnail.jpg

                            message = upload(video_data) #send video data paths to upload function 
                            # message = "aafafsa Uploaded Successfully"
                            print(green+ f"{message}") #print respose from upload function                        
                            time.sleep(0.5)
                            
                            #delete path of successfully uploaded videos
                            if message[-21:] == "Uploaded Successfully":
                                upl_counter = upl_counter + 1
                                shutil.rmtree(path, ignore_errors = False)                    
                                if upl_counter >= 4:
                                    print(green+"Max Upload limit reached. (4 Videos at a time)")
                                    time.sleep(5)
                                    break                     
                    else:
                        print(red+ f"\t'{ch_fol[i]}' --> This folder is empty.")
                        #delete empty channel folder.
                        shutil.rmtree(os.path.join(yt_data_path, ch_fol[i]), ignore_errors = False)
        except:
            print(red+ "Error! while uploading Video.")
    
    time.sleep(180)

