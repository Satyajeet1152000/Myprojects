import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

class Navbar(MDScreen):
    pass

class FirstWindow(Screen):
    pass

class ThirdWindow(Screen):

    def on_pre_enter(self):
        anchor = AnchorLayout(size=(1,1))
        test = "This is the new window"
        card = MDCard(orientation='vertical',padding="8dp",size_hint=(1,0.5),pos_hint={'top': 0.1,'right':1},radius=[5, ])
        card.test = test
        card.add_widget(MDLabel(text=test, halign="center"))
        anchor.add_widget(card)
        self.anchorID.add_widget(anchor)
            

class WindowManager(ScreenManager):
    pass

class NearMeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_palette = "Purple"
        self.root = Builder.load_file('main1.kv')

if __name__ == '__main__':
    NearMeApp().run()