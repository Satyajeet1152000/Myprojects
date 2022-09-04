from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen

import globalVar
import requests as req
import json
import os
from QrCodeGen import QRCodeGenerator
from Navbar import ContentNavigationDrawer, ItemDrawer, DrawerList




class MyToggleButton(MDRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.background_down = (1,1,0,1)
        self.font_color_down = (1,1,0,1)


class Login(MDScreen):
    Builder.load_file("design/Login.kv")

    email = ObjectProperty(None)
    password = ObjectProperty(None)
    errorLabel = ObjectProperty(None)

    btn_color = ListProperty((177/255, 35/255, 65/255, 1))

    def validate(self):      
        print(self.email.text)
        # data = req.get(f'http://localhost/new/api/faculty/single_read.php?email=rehan@gmail.com')
        data = req.get(f'http://localhost/new/api/faculty/single_read.php?email={self.email.text}')

        data = json.loads(data.text)
        print(data) 
        # print(data["email"])
        # print(type(data["name"]))

        try: 
            url = "http://localhost/new/api/faculty/query.php"            
            bdata = {'query' : f"select total_num_of_sem from branch where branch_name= '{globalVar.faculty_branch }'"}
            data = req.put(url, json=bdata)
            data = json.loads(data.text)
            print(data[0]["total_num_of_sem"])
            globalVar.faculty_total_sem = int(data[0]["total_num_of_sem"])
        except:
            print("def on_enter(self): Error")

            
        print("Login Button pressed")

        # Builder.load_file("design/main.kv")

        self.parent.current = "MainScreen"
        # self.parent.current = "DeptSelection"

        # if data == "Faculty not found.":
        #     if self.email.text == "" or self.password.text == "":
        #         self.errorLabel.text = "Please Enter all fields."
        #     else:
        #         self.errorLabel.text = "User not Found."
        # else:
        #     if (self.email.text == data["email"] and self.password.text == str(data["password"])):
        #     # if (self.email.text == "s" and self.password.text == "s"):
        #         #save global variable
                
        #         globalVar.facultyname = data["name"]
        #         globalVar.faculty_branch = data["branch_name"]
        #         self.parent.current = "DeptSelection" # switching the current screen
        #         print("Corrrrrrrrrrrrect")

        #     else:
        #         self.errorLabel.text = "Please Enter correct Password."   
    
         
class DeptSelection(MDScreen):
    rowsForSem = int(globalVar.faculty_total_sem/6 + 1)
    rowsForSub = int(globalVar.faculty_total_sem/6 + 1)
    btn_color = ListProperty((177/255, 35/255, 65/255, 1))
    

    # def __init__(self, **kw):
    #     super().__init__(**kw)

    def on_enter(self): 
        # self.ids.displaySemButton.clear_widgets()
        # self.ids.displaySubButton.clear_widgets()

        # try: 
        #     url = "http://localhost/new/api/faculty/query.php"            
        #     bdata = {'query' : f"select total_num_of_sem from branch where branch_name= '{globalVar.faculty_branch }'"}
        #     data = req.put(url, json=bdata)
        #     data = json.loads(data.text)
        #     print(data[0]["total_num_of_sem"])
        #     globalVar.faculty_total_sem = int(data[0]["total_num_of_sem"])
        # except:
        #     print("def on_enter(self): Error")

        faculty_total_sem = globalVar.faculty_total_sem

        print("faculty total sem",faculty_total_sem)

        for i in range(1,faculty_total_sem+1):
            btn = MyToggleButton(text=f"{i}",font_size=30,line_width = 2,
            # line_color = (0,1,1,1),
            # text_color= (0,1,1,1), 
            font_color_normal = (0,1,1,1),
            group="sem",on_press=self.displaySubButton)    
               
            try:
                print(self.parent.ids)
                # self.parent.DeptSelection.ids.displaySemButton.add_widget(btn)
            except Exception as e:
                print(e)
        
        
    # Display subjects according to semester
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
            # line_color = (0,1,1,1),
            # text_color= (0,1,1,1),
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
            print("-->",selected_sem)

            tb = next((t for t in MyToggleButton.get_widgets('sub') if t.state=='down'), None)
            selected_sub = tb.text if tb else None
            print("-->",selected_sub)


            if selected_sem != None and selected_sub != None:
                globalVar.selected_sem = selected_sem
                globalVar.selected_sub = selected_sub            
                self.parent.current = "DisplayQR" # switching the current screen
        except:
            pass


class DisplayQR(MDScreen):
    # qrLabel = ObjectProperty(None)
    
    qrImagePath = f"{os.getcwd()}\\kivymd\\qr\\mainQR.png"
    qr  = QRCodeGenerator()

    def on_enter(self):      
        self.qr.generateQR(text="test",qrfillshape=globalVar.qrfillshape, gradient_style=globalVar.gradient_style)
        self.ids.qrImage.source = self.qrImagePath

    def backButton(self):

        # deselect togglebutton group 'sub' when press back button
        # try:
        #     tb = next((t for t in ToggleButton.get_widgets('sem') if t.state=='down'), None)
        #     tb.state = 'normal' if tb else None

        #     tb = next((t for t in ToggleButton.get_widgets('sub') if t.state=='down'), None)
        #     tb.state = 'normal' if tb else None
        # except:
        #     pass

        self.parent.current = "DeptSelection" # switching the current screen
        self.manager.transition.dorection = "right"


# Builder.load_file("design/main.kv")
class newApp(MDApp):    
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("design/SplashScreen.kv"))
        sm.add_widget(Login(name= "LoginScreen"))
        sm.add_widget(Builder.load_file("design/main.kv"))
        # sm.add_widget(DeptSelection(name= "DeptSelection"))
        return sm
    

    def on_start(self):  
        Clock.schedule_once(self.login, 3)
        
    def login(self, *args):
        sm.current = "LoginScreen"
    #     print("going to login screen")
        # sm.current = "MainScreen"

       

if __name__ == "__main__":
    newApp().run()