from msilib.sequence import tables
import requests as req
import json

# data = req.get(f'http://localhost/new/api/faculty/single_read.php?email=rehan@gmail.cm')
# x = json.loads(data.text)
# print(x)


# print(x["total_student"])

# import matplotlib.pyplot as plt
# import numpy as np


# labels = ['1 July', '2 July', '3 July', '4 July', 'Today']
# present = [20, 34, 30, 35, 27]
# absent = [25, 32, 34, 20, 25]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, present, width, label='Present')
# rects2 = ax.bar(x + width/2, absent, width, label='Absent')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Students')
# ax.set_title('Total Attendance')
# ax.set_xticks(x, labels)
# ax.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

# fig.tight_layout()

# plt.show()

# user = "mca"
# url = "http://localhost/new/api/faculty/query.php"
# bdata = {'query' : f"select subject_short_name from subject where semester= 1"}
# x = req.put(url, json=bdata)
# x = json.loads(x.text)
# print(x)
# for i in range(0,len(x)):
#     print(f'{x[i]["subject_short_name"]}')
#     print()

# print(len(x))
# print(x[0]["subject_short_name"])




