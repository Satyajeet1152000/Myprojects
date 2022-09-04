from upload import *
import time

video_data = [
                ["E:\\YT_V_Data\\ONE Media\\THE MATRIX AWAKENS Trailer (NEW, 2022)\\THE MATRIX AWAKENS Trailer (NEW 2022).Mp4",
                "E:\\YT_V_Data\\ONE Media\\THE MATRIX AWAKENS Trailer (NEW, 2022)\\title.txt",
                "E:\\YT_V_Data\\ONE Media\\THE MATRIX AWAKENS Trailer (NEW, 2022)\\description.txt",
                "E:\\YT_V_Data\\ONE Media\\THE MATRIX AWAKENS Trailer (NEW, 2022)\\keywords.txt",
                "E:\\YT_V_Data\\ONE Media\\THE MATRIX AWAKENS Trailer (NEW, 2022)\\thumbnail.jpg"
                ],
                ['E:\\YT_V_Data\\ONE Media\\SPIDER-MAN NO WAY HOME Iron Spider-Man with Gliders Trailer (NEW, 2021)\\SPIDER-MAN NO WAY HOME Iron Spider-Man with Gliders Trailer (NEW 2021).mp4', 
                'E:\\YT_V_Data\\ONE Media\\SPIDER-MAN NO WAY HOME Iron Spider-Man with Gliders Trailer (NEW, 2021)\\title.txt', 
                'E:\\YT_V_Data\\ONE Media\\SPIDER-MAN NO WAY HOME Iron Spider-Man with Gliders Trailer (NEW, 2021)\\description.txt', 
                'E:\\YT_V_Data\\ONE Media\\SPIDER-MAN NO WAY HOME Iron Spider-Man with Gliders Trailer (NEW, 2021)\\keywords.txt', 
                'E:\\YT_V_Data\\ONE Media\\SPIDER-MAN NO WAY HOME Iron Spider-Man with Gliders Trailer (NEW, 2021)\\thumbnail.jpg'
                ]
            ]

for i in range(2):
    print(upload(video_data[i]))
    time.sleep(2)
