from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen


class FirstWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = """
Screen:
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation:'vertical'
            Button:
                text:"ThirdWindow"
                on_release: root.ids.manager.current = "ThirdWindow"
    StackLayout:
        MDToolbar:
            title: "NearMe Application"
            size_hint: (1, 0.1)
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
        WindowManager:
            id: manager
            FirstWindow:
            ThirdWindow:

<FirstWindow>:
    name:"FirstWindow"
    Screen:
        BoxLayout:
            orientation: 'vertical'
            Widget:
<ThirdWindow>:
    name:"ThirdWindow"      
    anchorID:anchorID

    AnchorLayout:
        id:anchorID
        canvas.before:
            Color:
                rgba: .2, .2, .2, 1
            Rectangle:
                pos: self.pos
                size: self.size
"""


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(kv)

    def build(self):
        return self.screen


the_app = Test()
the_app.run()