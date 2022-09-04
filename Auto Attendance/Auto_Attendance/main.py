from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.config import Config

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np

from QrCodeGen import QRCodeGenerator
import os
import requests as req
import json
import globalVar


class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    errorLabel = ObjectProperty(None)

    def validate(self):      
        print(self.email.text)
        # data = req.get(f'http://localhost/new/api/faculty/single_read.php?email=rehan@gmail.com')
        data = req.get(f'http://localhost/new/api/faculty/single_read.php?email={self.email.text}')

        data = json.loads(data.text)
        print(data) 
        # print(data["email"])
        # print(type(data["name"]))

        if data == "Faculty not found.":
            if self.email.text == "" or self.password.text == "":
                self.errorLabel.text = "Please Enter all fields."
            else:
                self.errorLabel.text = "User not Found."
        else:
            if (self.email.text == data["email"] and self.password.text == str(data["password"])):
            # if (self.email.text == "s" and self.password.text == "s"):
                #save global variable
                
                globalVar.facultyname = data["name"]
                globalVar.faculty_branch = data["branch_name"]
                self.parent.current = "DeptSelection" # switching the current screen
            else:
                self.errorLabel.text = "Please Enter correct Password."   
          
class DeptSelection(Screen):
    # all department lists
    rowsForSem = int(globalVar.faculty_total_sem/6 + 1)
    rowsForSub = int(globalVar.faculty_total_sem/6 + 1)
 
    faculty_welcome_label = ObjectProperty(None)

    def on_enter(self):
        self.ids.displaySemButton.clear_widgets()
        self.ids.displaySubButton.clear_widgets()

        print("facultyname=",globalVar.facultyname,"\nuser's branch = ",globalVar.faculty_branch )

        # # deselect togglebutton group 'sub' when press back button
        # try:
        #     tb = next((t for t in ToggleButton.get_widgets('sem') if t.state=='down'), None)
        #     tb.state = 'normal' if tb else None

        #     tb = next((t for t in ToggleButton.get_widgets('sub') if t.state=='down'), None)
        #     tb.state = 'normal' if tb else None
        # except:
        #     pass

        try: 
            url = "http://localhost/new/api/faculty/query.php"            
            bdata = {'query' : f"select total_num_of_sem from branch where branch_name= '{globalVar.faculty_branch }'"}
            data = req.put(url, json=bdata)
            data = json.loads(data.text)
            print(data[0]["total_num_of_sem"])
            globalVar.faculty_total_sem = int(data[0]["total_num_of_sem"])
        except:
            print("def on_enter(self): Error")

        faculty_total_sem = globalVar.faculty_total_sem
        self.faculty_welcome_label.text = "Hello, " + globalVar.facultyname

        for i in range(1,faculty_total_sem+1):
            self.ids.displaySemButton.add_widget(ToggleButton(text=f"{i}",
            size_hint= (None,None),
            size=(0.17*self.width , 0.07*self.height),
            on_press=self.displaySubButton,
            group="sem"))
        
    # Display subjects according to semester
    def displaySubButton(self,button):
        print(button.text," semester selected")
        self.ids.displaySubButton.clear_widgets()

        try:
            url = "http://localhost/new/api/faculty/query.php"
            bdata = {'query' : f"select subject_short_name from subject where semester= {button.text}"}
            data = req.put(url, json=bdata)
            data = json.loads(data.text)
            # print(data[0]["subject_short_name"])
        except:
            print(" def displaySubButton Error")

        for i in range(0,len(data)):
            self.ids.displaySubButton.add_widget(ToggleButton(text=f"{data[i]['subject_short_name']}",
            size_hint= (None,None),
            size=(0.17*self.width , 0.07*self.height),
            group="sub"))

    def validate(self):
        try:
            tb = next((t for t in ToggleButton.get_widgets('sem') if t.state=='down'), None)
            selected_sem = tb.text if tb else None
            print(selected_sem)

            tb = next((t for t in ToggleButton.get_widgets('sub') if t.state=='down'), None)
            selected_sub = tb.text if tb else None
            print(selected_sub)


        except:
            pass

        if  selected_sem != None and selected_sub != None:
            globalVar.selected_sem = selected_sem
            globalVar.selected_sub = selected_sub            
            self.parent.current = "DisplayQR" # switching the current screen

class DisplayQR(Screen):
    qrLabel = ObjectProperty(None)
    
    qrImagePath = f"{os.getcwd()}\\Auto_Attendance\\qr\\mainQR.png"
    qr  = QRCodeGenerator()

    def on_enter(self):      
        self.qr.generateQR(text="test",qrfillshape=globalVar.qrfillshape, gradient_style=globalVar.gradient_style)
        self.ids.qrImage.source = self.qrImagePath

    def backButton(self):

        # deselect togglebutton group 'sub' when press back button
        try:
            tb = next((t for t in ToggleButton.get_widgets('sem') if t.state=='down'), None)
            tb.state = 'normal' if tb else None

            tb = next((t for t in ToggleButton.get_widgets('sub') if t.state=='down'), None)
            tb.state = 'normal' if tb else None
        except:
            pass

        self.parent.current = "DeptSelection" # switching the current screen

class CurrentAnalytics(Screen):


    def on_enter(self):

        self.ids.analyticsBox.clear_widgets()

        data = req.get("http://localhost/new/api/attendance_stats/branchStat.php").text
        data = json.loads(data)

        total_student = int(data["total_student"])
        present = int(data["itemCount"])
        absent = total_student - present

        # Pie chart
        labels = 'Present', 'Absent'
        sizes = [present, absent]
        explode = (0.2, 0,)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal') 

        self.ids.analyticsBox.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        #bar Chart
        labels = ['2 July', '3 July', '4 July', 'Today']
        present = [34, 30, 35, present]
        absent = [32, 34, 20, absent]

        x = np.arange(len(labels))  # the label locations
        width = 0.25  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, present, width, label='Present')
        rects2 = ax.bar(x + width/2, absent, width, label='Absent')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Students')
        ax.set_title('Total Attendance')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        self.ids.analyticsBox.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("design/main.kv")
# Config.set('graphics', 'resizable', False)
# Config.set('graphics', 'width', '600')
# Config.set('graphics', 'height', '900')

class AutoAttendance(App):
    def build(self):
        Window.size = [900,500]
        return kv

if __name__ == "__main__":
    AutoAttendance().run()