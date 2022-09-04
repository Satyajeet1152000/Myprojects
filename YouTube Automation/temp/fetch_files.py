import os
from datetime import date

yt_data_path = "E:\YT_V_Data"
date_fol = "06-Nov-2021"
files = os.listdir(path=yt_data_path)
# print(files)

if date_fol in files:
    path = os.path.join(yt_data_path, date_fol)
    chnl_fol = os.listdir(path)
    
    # print chnl_fol of date_fol
    for i in range(len(chnl_fol)):
        print(f"{i+1}. {chnl_fol[i]}")
    
    choice = True
    while choice!=0:
        choice = int(input("\nEnter folder number: "))
        # choice = 1
        if choice in range(1,len(chnl_fol)+1):
            chnl_fol_name = chnl_fol[choice-1]
            print(f"\n\"{chnl_fol_name}\" contain these videos: ")        
            path = os.path.join(yt_data_path, date_fol, chnl_fol[choice-1])
            videos_fol = os.listdir(path)
            print("--------------------------------------------------")
            for i in range(len(videos_fol)):
                print(f"{i+1}. {videos_fol[i]}")
            print("--------------------------------------------------")
            
            choice = True
            while choice != False:
                choice = int(input("Enter Video number to show detail.: "))
                if choice >= 1 and choice <= len(videos_fol):
                    path = os.path.join(yt_data_path, date_fol, chnl_fol_name, videos_fol[choice-1])
                    video_dtl = os.listdir(path)
                    print(video_dtl)
                    choice = False
                else:
                    print("Wrong input")    
            choice = True
        elif choice == 0:
            pass
        else:
            print("Wrong input")
else:
    print(f"\"{date_fol}\" is not present.")