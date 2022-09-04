from functions import * #this file contain all function for downloading videos
import shutil #it will help to delete the directory
from upload import * #this will help to upload video to youtube using selenium webdriver
import os
import time
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

choice = True
while choice != 6:  #never exit till user press 4 for exit
    #--Choice set no.1----
    print(yellow+"--------------------------------------")
    print("1. Check for latets videos updates.")
    print("2. Get Video of Specific channel.")
    print("3. Download video from url.")
    print("4. Upload video")
    print("5. Download videos from file contain url. ")
    print("6. Exit")
    print("--------------------------------------"+magenta)
    choice = int(input("Enter Choice: "))
    # os.system("cls")  #clearing terminal outputs
    # print(c_reset)
    
    if choice == 1: #Check for latets videos updates
        print("Checking for latest videos.")
        print("-------------------------------------------------------")
        data = get_latest_video_update() 
        
        #check get_latest_video_update have some updates
        if len(data) > 0:
            print(yellow+"Available video updates are below:")
            print("--------------------------------------------------------")
            for i in  range(len(data)):
                #show updates data as Channel_name --> video_title --> video_link
                print(cyan+ f"{i+1}. {data[i][0]} --> {data[i][1]} --> {data[i][2]}")
            print(yellow+ "---------------------------------------------------------")           
            
            choice = True            
            while choice: #never exit till user press 5
                print(yellow+"------------------------------------------------")                
                choice = input(magenta+"Do You want to download videos.(y/n): ")
                print(yellow+"------------------------------------------------\n")
                
                if choice == 'y' or choice == 'Y':
                    print(yellow+ "=========================================") 
                    print(yellow+ "Downloading Videos.................")                     
                    print(yellow+ "=========================================")   
                    
                    for i in range(len(data)):
                        try:                   
                            message = download_video(data[i][2])
                            print(green+ f"{message}")
                            print(c_reset)                            
                        except Exception as e:
                            print(red+"Something Wrong while Downloading{err}".format(e.__class__.__name__))
                    
                    print(yellow+ "=========================================\n\n")                      
                              
                            
                    print(c_reset)
                    print(yellow+ "=========================================")                        
                    print(yellow+ "Updating Database....")
                    print(yellow+ "=========================================")                        
                    try:
                        update_latest_vid_file()
                        print(green+"Databese is Updated Successfully")
                        print(yellow+ "=========================================")                        
                                        
                    except:
                        print(red+"Something wrong in database updation")  
                        print(yellow+ "=========================================")                        
                                
                    break #go to previous choice set no.2 after succesfully run this condition                                           
                                                
                elif choice == 'n' or choice == 'N': #Do Nothing or simple go back or exit from this while loop
                    break                
                else:
                    print(red+"Wrong Input")
                    
        else:
            print(red+"No Video Updates Available")
    
    elif choice == 2: #Get Video of Specific channel
        print(c_reset)
        #open chnl_url_id.txt file to fetch channel data and store in channel_detail variable
        with open(f"{os.getcwd()}/data/chnl_url_id.txt","r", encoding='utf-8') as lvd:
            data = lvd.readlines()   
            channel_detail = []
            for i in data:
                channel_detail.append((i.split('###'))) #seperate data as single string seperated by ####
                
        print(yellow+"--------------------------------------")
        for i in range(len(channel_detail)):
            print(cyan+ f"{i+1}. {channel_detail[i][0]}") #print channels name to download video from that channel using Sr.no.
        
        print(yellow+ "--------------------------------------")
        ch_choice =  int(input(magenta+"Enter Channel No.: "))  #get channel Sr.no.
        max_v =  int(input("Total no.(<10) of Videos: "))  #get max_v value to fetch maximum videos from get_video()
        print(yellow+ "--------------------------------------")
        
        print(c_reset)
        #check max should be >=1 and <=10 And choice should be >=1 and <= total no.of channels available in chnl_url_id.txt file     
        if (max_v>= 1 and max_v <= 10) and (ch_choice<=len(channel_detail) and ch_choice>=1):
            #data var have first video title and then video url
            data = get_video(channel_detail[ch_choice-1][2], max_v) #channel_detail[ch_choice-1][2]== channel_url and max_v
            print(yellow+ f"\"{channel_detail[ch_choice-1][0]}\" Videos are:") #print requested channel name for get_video() 
            print("-----------------------------------------")
            for i in range(len(data)):
                #print Sr.no.  Video_title       Video_url
                print(cyan+ f"{i+1}. {data[i][0]} --> {data[i][1]}")
            
            #===================going for downloading processes of data========================
            choice = True            
            while choice: #never exit till user press 5
                print(yellow+"------------------------------------------------")                
                choice = input(magenta+"Do You want to download videos.(y/n): ")
                print(yellow+"------------------------------------------------")
                
                if choice == 'y' or choice == 'Y':
                    for i in range(len(data)):
                        message = download_video(data[i][1])
                        print(green+ f"{message}")
                        print(c_reset)
                    break                                           
                                                
                elif choice == 'n' or choice == 'N': #Do Nothing or simple go back or exit from this while loop
                    break                
                else:
                    print(red+"Wrong Input")
        else:
            print(red+"Wrong Input in max_v or channel Sr.no.")
            
    elif choice == 3: #Download video from url
        vurl = input("Paste YouTube Video url: ")
        message = download_video(vurl)
        print(green+ f"{message}")
    
    elif choice == 4: #Upload video
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
                        # message = "uploaded"
                        print(green+ f"{message}") #print respose from upload function                        
                        time.sleep(0.5)
                        
                        #delete path of successfully uploaded videos
                        if message[-21:] == "Uploaded Successfully":
                            upl_counter = upl_counter + 1
                            shutil.rmtree(path, ignore_errors = False)                    
                            if upl_counter >= 4:
                                print(green+"Max Upload limit reached. (4 Videos at a time)")
                                time.sleep(5)
                                quit()         
                                                       
                else:
                    print(red+ f"\t'{ch_fol[i]}' --> This folder is empty.")
                    #delete empty channel folder.
                    shutil.rmtree(os.path.join(yt_data_path, ch_fol[i]), ignore_errors = False)
                    time.sleep(1)
                    print(green+ f"\t'{ch_fol[i]}' --> This Empty folder has been deleted successfully.")
                    
        else:
            print(red+ f"YT_V_Data is empty.")
            
    elif choice == 5: #Download videos from file contain url
        f_path = input(yellow+"Enter file path: ")
        print("------------------------------------------")
        print(c_reset)
        
        with open(f_path, "r") as l:
            links = l.readlines()
            
            
        for i in range(len(links)):
            try:
                print(yellow+f"{i+1}.")                 
                message = download_video(links[i])
                print(green+ f"{message}")
                print(c_reset)                            
            except:
                print(red+"Something Wrong while Downloading")
        
    elif choice == 6: #Exit
        print(red+ "Exited")
                
    else:
        print(red+ "Wrong input")