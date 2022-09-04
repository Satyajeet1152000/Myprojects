designer = '''
#:include design/SplashScreen.kv
#:include design/LoginScreen.kv
#:include design/DeptSelectionScreen.kv
#:include design/DisplayQRScreen.kv
#:include design/AttendanceStatScreen.kv


Screen:
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:"Auto Attendance System"
            left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
            elevation:5
            size_hint: 1, .1
        ScreenManager:
            size_hint: 1, 1

            # SplashScreen:
            LoginScreen:
            DeptSelectionScreen:
            DisplayQRScreen:
            AttendanceStatScreen:
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"
            MDCard:
                size_hint: 1, .3
                orientation: "vertical"
                MDIcon:
                    icon: "account-circle"    
                    # size_hint_y: None  
                    pos_hint: {"center_x":.6}
                    # size_hint: .4,.4
                    font_size: 80
                    # color: 0,1,1,1    
            
                MDLabel:
                    text: "KivyMD library"
                    font_style: "Button"
                    adaptive_height: True
                    pos_hint: {"center_x":.6}

                MDLabel:
                    text: "kivydevelopment@gmail.com"
                    font_style: "Caption"
                    adaptive_height: True
                    pos_hint: {"center_x":.6}
            ScrollView:
                MDList:
                    id: md_list
                    OneLineIconListItem:
                        text: "Take Attendance Mannualy"
                        IconLeftWidget:                                    
                            icon: "checkbox-multiple-marked-outline"
                                                        
                    OneLineIconListItem:
                        text: "Update Profile"
                        IconLeftWidget:
                            icon: "account-edit-outline"
                        
                    OneLineIconListItem:
                        text: "Update Database"
                        IconLeftWidget:
                            icon: "database-sync-outline"
                        
                    OneLineIconListItem:                                
                        text: "Analytics"
                        IconLeftWidget:
                            icon: "chart-bar-stacked"
                        
                    OneLineIconListItem:
                        text: "Settings"
                        IconLeftWidget:
                            icon: "cog-outline"
                        
                    OneLineIconListItem:
                        text: "Logout"
                        IconLeftWidget:
                            icon: "logout"
                                


'''