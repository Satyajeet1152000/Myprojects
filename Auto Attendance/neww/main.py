from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty, ListProperty

from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from matplotlib.pyplot import title
import matplotlib.pyplot as plt
import numpy as np

import os
import requests as req
import json
from desiner1 import designer
from QrCodeGen import QRCodeGenerator

# from Navbar import ContentNavigationDrawer, ItemDrawer, DrawerList


class SplashScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    errorLabel = ObjectProperty(None)

    btn_color = ListProperty((177/255, 35/255, 65/255, 1))

    def validate(self):
        try:
            if self.email.text == "" and self.password.text == "":
                dialogBox().open(title="Enter Fields", message="Please enter all fields", close_btn_text="Retry")
            elif self.email.text == "":
                dialogBox().open(title="Enter Email Id", message="Please enter Email Id.", close_btn_text="Retry")
            elif self.password.text == "":
                dialogBox().open(title="Enter Password", message="Please enter Password", close_btn_text="Retry")
            else:
                try:
                    # data = req.get(f'http://localhost/new/api/faculty/single_read.php?email=rehan@gmail.com')
                    data = req.get(f'http://localhost/new/api/faculty/single_read.php?email={self.email.text}')  
                                      
                    data = json.loads(data.text)
                    print(data)
                    if data == "Faculty not found.":
                        dialogBox().open(title="Not Found", message="Please Enter Valid Email and Password", close_btn_text="Retry")
                    else:
                        print("Login Button pressed")
                        if self.email.text == data['email'] and self.password.text == data['password']:
                            
                            try:
                                # store data in Userdata 
                                dataStore().store.put('userInfo',id=data['id'], name= data['name'], email= data['email'], branch_id= data['branch_id'])

                                data = req.get(f'http://localhost/new/api/faculty/getBranchInfo.php?branch_id={data["branch_id"]}')                           
                                data = json.loads(data.text)
                                print(data)
                                dataStore().store.put('branchInfo',id=data['branch_id'], name= data['branch_name'], short_name= data['branch_short_name'], total_num_of_sem= data['total_num_of_sem'])

                                # Switch to deptSelectionscreen
                                # self.parent.ids.navUsername.text = "GHiiiii"

                                self.parent.current = "deptSelectionScreen"

                            except:
                                print("branch info error")
                        else:
                            dialogBox().open(title="Invalid Credentials", message="Please enter correct Email and Password.", close_btn_text="Retry")

                except:
                    dialogBox().open(title="Login Btn Error", message="Login Btn Error", close_btn_text="Retry")

        except:
            dialogBox().open(title="Connection Error", message="Unable to fetch detail.\nTry Later", close_btn_text="Close")

class DeptSelectionScreen(MDScreen):
    btn_color = ListProperty((177/255, 35/255, 65/255, 1))

    def on_enter(self): 
        self.ids.displaySemButton.clear_widgets()
        self.ids.displaySubButton.clear_widgets()
        
        total_num_of_sem = int(dataStore().store.get("branchInfo")['total_num_of_sem'])
        print("total_num_of_sem  ",total_num_of_sem)
        for i in range(1,total_num_of_sem+1):
            btn = MyToggleButton(text=f"{i}",font_size=30,line_width = 2,
            font_color_normal = (0,1,1,1),
            group="sem",
            on_press=self.displaySubButton
            )    
            try:
                self.ids.displaySemButton.add_widget(btn)
            except Exception as e:
                print(e)
        
    def displaySubButton(self,button):
        print(button.text," semester selected")
        self.ids.displaySubButton.clear_widgets()

        try:
            url = "http://localhost/new/api/faculty/query.php"
            bdata = {'query' : f"select subject_short_name from subject where semester= {button.text}"}
            data = req.put(url, json=bdata)
            data = json.loads(data.text)
            print(data[0]["subject_short_name"])
        except:
            print(" def displaySubButton Error")

        for i in range(0,len(data)):
            btn = MyToggleButton(text=f"{data[i]['subject_short_name']}",
            font_size=30,line_width = 2,
            font_color_normal = (0,1,1,1),
            group="sub")    

            try:
                self.ids.displaySubButton.add_widget(btn)
            except Exception as e:
                print(e)
    
    def validate(self):
        try:
            tb = next((t for t in MyToggleButton.get_widgets('sem') if t.state=='down'), None)
            selected_sem = tb.text if tb else None
            # print(tb.state)
            print("-->",selected_sem)

            tb = next((t for t in MyToggleButton.get_widgets('sub') if t.state=='down'), None)
            selected_sub = tb.text if tb else None
            print("-->",selected_sub)

            if selected_sem == None:
                dialogBox().open(title="Semester Not Selected", message="Please select semester.", close_btn_text="Retry")
            elif selected_sub== None:
                dialogBox().open(title="Subject Not Selected", message="Please select Subject.", close_btn_text="Retry")

            elif selected_sem == None and selected_sub == None:
                dialogBox().open(title="Not Selected", message="Please select Semester & Subject.", close_btn_text="Retry")
           
            elif selected_sem != None and selected_sub != None:
                # generate Qrcode
                linktext = "http://localhost/new/api/student/submitAttendance.php"
                qr = QRCodeGenerator()
                dt = dataStore()
                qrfillshape = dt.store.get("qrCodeInfo")['qrfillshape']
                gradient_style = dt.store.get("qrCodeInfo")['gradient_style']
                qr.generateQR(text=str(linktext),qrfillshape=qrfillshape, gradient_style=gradient_style)
                # self.ids.qrImage.source = self.qrImagePath

                dt.store.put('subject', selected=selected_sub)
                self.parent.current = "displayQRScreen" # switching the current screen

        except:
            print("Semester and Subject selection error.")

class DisplayQRScreen(MDScreen):
    qrImagePath = f"{os.getcwd()}\\kivymd\\qr\\mainQR.png"

    def backButton(self):
        self.parent.current = "deptSelectionScreen"
    def nextButton(self):
        self.parent.current = "attendanceStatScreen"

class AttendanceStatScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def on_enter(self):

        self.ids.analyticsBox.clear_widgets()

        data = req.get(f"http://localhost/new/api/attendance_stats/branchStat.php").text
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

    def backButton(self):
        self.parent.current = "displayQRScreen"

class dialogBox():
    def open(self,title="",message="",close_btn_text="Close"):
        cancel_btn_username_dialogue = MDFlatButton(text= f'{close_btn_text}', on_release = self.close)
        self.dialog = MDDialog(title= f'{title}', text= f"{message}", size_hint=(.7,.2), buttons= [cancel_btn_username_dialogue])
        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()

class dataStore():
    store = JsonStore("UserData.json")

class MyToggleButton(MDRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.background_down = (1,1,0,1)
        self.font_color_down = (1,1,0,1)

class Navbar(MDScreen):
    pass
sm = ScreenManager()
sm.add_widget(SplashScreen(name= 'splashScreen'))
sm.add_widget(LoginScreen(name= 'loginScreen'))
sm.add_widget(DeptSelectionScreen(name= 'deptSelectionScreen'))
sm.add_widget(DisplayQRScreen(name= 'displayQRScreen'))
sm.add_widget(AttendanceStatScreen(name= 'attendanceStatScreen'))

class  newApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(designer)
        return self.strng

    def on_start(self):
        # self.store = JsonStore("UserData.json")
        dataStore().store
        Clock.schedule_once(self.loginvalidator, 3)


    def loginvalidator(self, *args):   
        try:
            if dataStore().store.get("userInfo")['name'] != "":
                # self.username_changer()
                self.strng.get_screen("deptSelectionScreen").manager.current = 'deptSelectionScreen'
            else:  
                self.strng.get_screen("loginScreen").manager.current = 'loginScreen'
        except:
            pass


    # def gotoLoginScreen(self, *args):
    #     self.strng.get_screen('loginScreen').manager.current = 'loginScreen'

    

    


newApp().run()


