from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color,Rectangle
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.clearcolor = (1, 1, 1, 1)

class myApp(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.l1 = Label(
            text = 'welcome to Page !',
            color = (0,0,0,1),
            font_size = 30
        )
        self.add_widget(self.l1)
        self.b1 = Button(
            text='submit !',
            color = (0,0,0,1),
            background_normal = '',
            background_color=(0, 0.514, 0.561, 1),
            size_hint=(0.2, 0.2),
            font_size = 20,
        )
        self.b1.bind(on_press = self.call_back)
        self.b2 = Button(
            text = 'log out',
            color = (0,0,0,1),
            background_normal = '',
            background_color=(1, 0.239, 0,1),
            size_hint = (0.2,0.2),
            font_size = 20,
        )
        self.add_widget(self.b1)
        self.add_widget(self.b2)
        self.pop1 = Popup(
            title = 'congratulations !',
            size_hint = (0.3,0.3),
            background_color=(1, 0.922, 0.933, 1),
            content = Label(
                text = 'You have submitted sucessfully !',
            )
        )
        self.size_hint = (0.5, 0.5)
        self.pos = (150, 150)

    def call_back(self,elem):
        self.pop1.open()


class to_do_listApp(App):
    def build(self):
        return myApp()


to_do_listApp().run()
