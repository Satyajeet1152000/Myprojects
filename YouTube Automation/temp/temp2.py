import datetime
import os

t = datetime.datetime.now()
t = t.strftime("%d/%h/%y %H:%M")
print(t)

f = open(f"{os.getcwd()}\data\Error_log.txt", "a")

f.write(f"\n{t}\t|  Upload_Error\t\t|  Upload button not found.")
f.write(f"\n{t}\t|  Download_Error\t|  Video length > 5 min.")
f.write(f"\n{t}\t|  Selenium_Error\t|  Url Error!")
f.write(f"\n{t}\t|  File_Not_Found\t|  Title.txt file missing in One Media>videoname")
f.write(f"\n{t}\t|  Button_Not_found\t|  Description file not found in.")

f.close()

# Error_log.write(f"\n{t}\t|  Upload_Error\t|  {message}")
# Error_log.write(f"\n{t}\t|  Button_Not_found\t|  {message}")
# Error_log.write(f"\n{t}\t|  Selenium_Error\t|  {message}")
# Error_log.write(f"\n{t}\t|  File_Not_Found\t|  {message}")