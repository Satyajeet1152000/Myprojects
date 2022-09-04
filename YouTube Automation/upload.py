from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
import datetime
from colorama import init, Fore, Style


def upload(video_data):
    init(convert=True)

    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    blue = Fore.BLUE
    magenta = Fore.MAGENTA
    cyan = Fore.CYAN
    c_reset = Style.RESET_ALL
    
    driver_path = os.getcwd() + "\\chromedriver_win32\\chromedriver.exe"
    
    #Chrome
    browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe" #chrome.exe
    user_data_path = "C:/Users/Satyajeet/AppData/Local/Google/Chrome/User Data" #chrome user data
    profile = "Default" #chrome profile for satyajeet914

    option = webdriver.ChromeOptions()

    option.add_argument(f"--user-data-dir={user_data_path}")
    option.add_argument(f"--profile-directory={profile}")
    option.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.add_argument("--disable-gpu")
    option.add_argument('--no-sandbox') # Bypass OS security model
    option.add_argument('start-maximized') 
    option.add_argument('disable-infobars')
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-application-cache")
    option.add_argument("--disable-infobars")
    option.binary_location = browser_path

    # Creating Instance of Chrome
    browser = webdriver.Chrome(executable_path = driver_path, chrome_options = option)
    
    #this will crete log error in Error_log.txt file.
    Error_log = open(f"{os.getcwd()}\data\Error_log.txt", "a")
    t = datetime.datetime.now()
    t = t.strftime("%d/%h/%y %H:%M")
    
    
    video_path = video_data[0]  #--> Videp file Path  
    # video_data[1] --> title   
    # video_data[2] --> description
    # video_data[3] --> keyword
    video_thumbnail_path = video_data[4] # --> video thumbnail path

    #=======================================Browser Operation========================================    
    try:
        try:                        
            with open(video_data[1], "r", encoding='utf-8') as f:
                video_title = f.readlines()                        
        except:
            print(red+ "\tCan't find title.txt file      ")
            Error_log.write(f"\n{t}\t|  File_Not_found\t|  Can't find title.txt file.")
            video_title = "Video_Title Not Added."
            pub_priv_status = private
            
        print(blue+ f"{video_title} -->  Uploading......")
        browser.implicitly_wait(5) # Wait up 5 sec before throwing an error if selenium cannot find the element (!important)
        browser.get("https://studio.youtube.com")
        try:
            upl_btn = browser.find_element_by_xpath('/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[1]/div[1]/ytcp-quick-actions/a[1]/ytcp-icon-button').click()
            time.sleep(0.5)
            try:
                file = browser.find_element_by_xpath("//input[@type='file']")
                file.send_keys(video_path)
                time.sleep(0.4)
                print(green+ "\tFile Uploading.....")
                # time.sleep(4)
                upl_pro_msg = ['Uploading 100% ...',
                                'Upload complete ... Processing will begin shortly',
                                'Processing 15% ...',
                                'Processing 55% ...',
                                'Processing 95% ...',
                                'Processing 5% .... Processing will begin shortly',
                                'Processing 15% .... Processing will begin shortly',
                                'Processing 75% .... Processing will begin shortly',
                                'Processing 35% .... Processing will begin shortly',
                                'Processing 55% .... Processing will begin shortly',
                                'Processing 25% .... Processing will begin shortly',
                                'Checks complete. No issues found.'
                                ]
                
                public = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[2]'
                private = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]/div[2]'
                pub_priv_status = public
            
            
                #=====================Title===================                      
                try:
                    title =browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-mention-input/div')
                    title.send_keys(Keys.CONTROL, "a")
                    title.send_keys(video_title)
                    print(green+ "\tTitle Added")                                                        
                    time.sleep(0.2)
                except:
                    message = "Can't find title textbox."
                    print(message)
                    Error_log.write(f"\n{t}\t|  Element_Not_found\t|  {message}")
                    Error_log.close()
                    return message
                    
                #==========Description======================   
                try:
                    with open(video_data[2], "r", encoding='utf-8') as f:
                        video_description = f.readlines()
                    
                    # print(type(video_description))    
                    
                    # video_description = video_description.replace("\t", "         ")
                        
                                 
                    try:
                        description = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-mention-input/div')
                        time.sleep(1)   
                        
                        for i in range(len(video_description)):
                            try:
                                video_description[i] = video_description[i].replace("\t", "       ")
                                description.send_keys(video_description[i])
                                time.sleep(0.1)
                            except:
                                for j in range(len(video_description[i])):
                                    try:
                                        description.send_keys(video_description[i][j])
                                    except:
                                        description.send_keys("")
                            
                                        
        
                        time.sleep(0.5)
                        print(green+ "\tDescription Added")
                                
                             
                        # try:                                
                        #     description.send_keys(video_description)
                        #     time.sleep(0.3)
                        # except Exception as e:
                            # print(e.__class__.__name__)
                            # print(e)                            
                        
                    except Exception as e:
                        message = "Can't find description textbox."
                        print(red+ f"\t{message}  {e.__class__.__name__}")
                        Error_log.write(f"\n{t}\t|  Element_Not_found\t|  {message}")
                except:
                    print(red+ "\tCan't find description.txt file")
                    Error_log.write(f"\n{t}\t|  File_Not_found\t|  Can't find description.txt file.")
                    pub_priv_status = private
                    try:
                        description = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div')
                        description.send_keys(Keys.CONTROL, "a")
                        description.send_keys("")
                        print(green+ "\tDescription Added")
                        time.sleep(0.3)
                    except:
                        message = "Can't find description textbox."
                        print(red+ f"\t{message}")
                        Error_log.write(f"\n{t}\t|  Element_Not_found\t|  {message}")
                                            
                #============Thumbnail==================   
                try:    
                    thumbnail = browser.find_element_by_xpath("//input[@type='file']")
                    thumbnail.send_keys(video_thumbnail_path)
                    print(green+ "\tThumbnail Uploaded             ")
                    time.sleep(0.2)
                except:
                    print(red+ "\tUnable to upload Thumbnail.")
                    Error_log.write(f"\n{t}\t|  File_Not_found\t|  Thumbnail file not found.")
                    Error_log.write(f"\n{t}\t|  Upload_Error\t\t|  Unable to uplaod thumbnail.")
                
                #============Not_for_kid=============
                try:
                    browser.implicitly_wait(5)
                    not_for_kid = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]')
                    if not_for_kid.is_selected():
                        print(green+ "\tnot_for_kid radio button is already selected.")
                    else:            
                        not_for_kid.click()
                        print(green+ "\tnot_for_kid radio button is selected.")
                    time.sleep(0.3)
                except:
                    print(red+ "\tError! not_for_kid selection   ")
                    Error_log.write(f"\n{t}\t|  Element_Not_found\t|  not_for_kids radio button not found.")
                    
                #============Show More===========
                try:
                    show_more = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/div/ytcp-button/div').click()
                    time.sleep(0.4)
                except:
                    print(red+ "\tShow More button not found     ")
                    Error_log.write(f"\n{t}\t|  Element_Not_found\t|  Show More button not found.")
                
                #==========Video Tags==============    
                try:
                    with open(video_data[3], "r", encoding='utf-8') as f:
                        data = f.readlines()
                        video_keyword = ""
                        for i in range(len(data)):
                            video_keyword = video_keyword + data[i]        
                        video_keyword = video_keyword.replace('\n', '')
                    
                    try:         
                        # time.sleep(100)
                        tags = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[3]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input')
                        tags.send_keys(video_keyword)
                        tags.send_keys(Keys.RETURN)
                        print(green+ "\tTags added       ")
                        time.sleep(0.2)
                    except:
                        print(red+ "\tCan't find tags textbox.       ")
                        Error_log.write(f"\n{t}\t|  Element_Not_found\t|  Can't find tags textbox.")
                except:
                    print(red+ "\tCan't find keyword.txt file.   ")
                    Error_log.write(f"\n{t}\t|  File_Not_found\t|  Can't find keyword.txt file.")
                    try:                                
                        tags = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[3]/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input')
                        tags.send_keys(f"{video_title},movie,trailer,official trailer,scene")
                        tags.send_keys(Keys.RETURN)
                        print(green+ "\tTags added       ")
                        time.sleep(0.2)
                    except:
                        print(red+ "\tCan't find tags textbox.       ")
                        Error_log.write(f"\n{t}\t|  Element_Not_found\t|  Can't find tags textbox.")       

                               
                #==============1st Next Button==========
                try:
                    next_btn = browser.find_element_by_xpath('//*[@id="next-button"]/div').click()
                    time.sleep(1)                        
                    try:
                        add_end_screen = browser.find_element_by_xpath('//*[@id="endscreens-button"]/div').click()
                        time.sleep(1)                            
                        try:
                            browser.implicitly_wait(3)
                            select_end_screen = browser.find_element_by_xpath('/html/body/ytve-endscreen-modal/ytve-modal-host/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-endscreen-editor-options-panel/div[2]/div/ytve-endscreen-template-picker/div/div/div/div[4]').click()
                            time.sleep(0.8)
                            try:
                                save_end_screen = browser.find_element_by_xpath('/html/body/ytve-endscreen-modal/ytve-modal-host/ytcp-dialog/tp-yt-paper-dialog/div[1]/div/div[2]/div[2]/ytcp-button/div').click()
                                time.sleep(1)
                                print(green+ "\tEnd Screen Saved ")
                            except:
                                print(red+ "\tEnd_Screen_Save_Btn not found. ")
                                Error_log.write(f"\n{t}\t|  Element_Not_found\t|  End_Screen_Save_Btn not found.")       

                        except:
                            print(red+ "\tUnable to select End_Screen.   ")
                            Error_log.write(f"\n{t}\t|  Element_Not_found\t|  Unable to select End_Screen.")       
                    except:
                        print(red+ "\tEnd_Screen_button not found.   ")
                        Error_log.write(f"\n{t}\t|  Element_Not_found\t|  End_Screen_button not found.")   
                except:
                    print(red+ "\t1st Next_button not found.     ") 
                    Error_log.write(f"\n{t}\t|  Element_Not_found\t|  1st Next_button not found.")       
                                            
                    while True:
                        upl_progress = browser.find_element_by_xpath('/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-video-upload-progress/span').text
                        if upl_progress not in upl_pro_msg:
                            print(cyan+ f"{upl_progress}",end="\r")
                            time.sleep(0.5)
                        else:
                            time.sleep(2)
                            db_update(video_title)
                            browser.quit()
                            message = f"{video_title}--> is Uploaded Successfully"
                            Error_log.close()
                            return message
                            break
                
                #==============2nd Next Button==========
                try:
                    next_btn = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div').click()
                    time.sleep(1.5)
                except:
                    print(red+ "\t2nd Next_button not found.     ")
                    Error_log.write(f"\n{t}\t|  Element_Not_found\t|  2nd Next_button not found.")       
                                            
                    while True:
                        upl_progress = browser.find_element_by_xpath('/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-video-upload-progress/span').text
                        if upl_progress not in upl_pro_msg:
                            print(cyan+ f"{upl_progress}",end="\r")
                            time.sleep(0.5)
                        else:
                            time.sleep(5)
                            db_update(video_title)
                            browser.quit()
                            message = f"{video_title}--> is Uploaded Successfully" 
                            Error_log.close()   
                            return message
                            break                        
                    
                
                #==============3rd Next Button==========                    
                try:
                    
                    next_btn = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]').click()
                    time.sleep(0.5)
                    #============Publish Button===================
                    try:
                        publish_btn = browser.find_element_by_xpath(pub_priv_status).click()
                        print(green+ "\tPublish mode Selected          ")                                  
                        time.sleep(1)
                        try:
                            save_btn = browser.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]').click()
                            time.sleep(2)
                            while True:
                                upl_progress = browser.find_element_by_xpath('/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-video-upload-progress/span').text
                                if upl_progress not in upl_pro_msg:
                                    print(cyan+ f"{upl_progress}",end="\r")
                                    time.sleep(0.5)
                                else:
                                    time.sleep(2)
                                    db_update(video_title)
                                    browser.quit()
                                    message = f"{video_title}--> is Uploaded Successfully"  
                                    Error_log.close()  
                                    return message
                                    break
                        except:
                            print(red+ "\tSave button not found.         ")
                            Error_log.write(f"\n{t}\t|  Element_Not_found\t|  Save button not found.")
                            
                            while True:
                                upl_progress = browser.find_element_by_xpath('/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-video-upload-progress/span').text
                                if upl_progress not in upl_pro_msg:
                                    print(cyan+ f"{upl_progress}",end="\r")
                                    time.sleep(0.5)
                                else:
                                    time.sleep(5)
                                    db_update(video_title)
                                    browser.quit()
                                    message = f"{video_title}--> is Uploaded Successfully"
                                    Error_log.close()    
                                    return message
                                    break   
                    except:
                        print(red+ "\tUnable to select private/public")
                        Error_log.write(f"\n{t}\t|  Element_Not_found\t|  Unable to select private/public")
                        while True:
                            upl_progress = browser.find_element_by_xpath('/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-video-upload-progress/span').text
                            if upl_progress not in upl_pro_msg:
                                print(cyan+ f"{upl_progress}",end="\r")
                                time.sleep(0.5)
                            else:
                                time.sleep(5)
                                db_update(video_title)
                                browser.quit()
                                message = f"{video_title}--> is Uploaded Successfully" 
                                Error_log.close()   
                                return message
                                break   
                        
                except:
                    print(red+ "\t3rd Next_button not found.     ")
                    Error_log.write(f"\n{t}\t|  Element_Not_found\t|  3rd Next_button not found.")
                                            
                    while True:
                        upl_progress = browser.find_element_by_xpath('/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-video-upload-progress/span').text
                        if upl_progress not in upl_pro_msg:
                            print(cyan+ f"{upl_progress}",end="\r")
                            time.sleep(0.5)
                        else:
                            time.sleep(5)
                            db_update(video_title)
                            browser.quit()
                            message = f"{video_title}--> is Uploaded Successfully"
                            Error_log.close()    
                            return message
                            break       
            except Exception as e:
                message = f"Unable to locate file/Error in file type. {e.__class__.__name__}"
                Error_log.write(f"\n{t}\t|  Upload_Error\t\t|  {message}")
                Error_log.close()
                browser.quit()
                return message
        except:                
            message = "Unable to locate upload button."
            Error_log.write(f"\n{t}\t|  Element_Not_found\t|  {message}")
            Error_log.close()
            browser.quit()
            return message        
    except Exception as e:
        message = "Page load Error " + e.__class__.__name__
        Error_log.write(f"\n{t}\t|  Selenium_Error\t|  {message}")
        Error_log.close()
        browser.quit()
        return message  
    
        
def db_update(title):
    data_path = "D:/Programs/python/pytube/data"
    try:
        with open(f"{data_path}/uploaded_videos.txt","a", encoding='utf-8') as f:
            f.write(f"{title}\n")
    except:
        Error_log.write(f"\n{t}\t|  File_Not_Found\t|  uploaded_videos.txt file not found.")
