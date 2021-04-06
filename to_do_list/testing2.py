from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage,Image
Window.clearcolor = (1, 1, 1, 1)


class RootWidget(BoxLayout):
    pass

class myApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.spacing = 30
        self.orientation = 'vertical'
        self.size_hint = (0.5, 0.5)
        self.pos_hint = {'center_x':0.5,'center_y':0.5}
        self.font_name = 'OpenSans-Light.ttf'

        # label 1
        self.l1 = Label(
            text='Welcome to Page !',
            color=(0, 0, 0, 1),
            font_size=40,
            font_name = 'OpenSans-ExtraBold',
            pos_hint = {'center_x':0.5,'center_y':0.5}
        )
        self.add_widget(self.l1)
        #label 2
        self.l2 = Label(
            text = 'created by shivam anand',
            color = (0,0,0,1),
            font_size = 15,
            font_name = self.font_name
        )
        self.add_widget(self.l2)

        # text input 1
        self.t1 = TextInput(
            text = '',
            multiline=True,
            background_normal='',
            background_color=(0.925, 0.937, 0.945, 1),
            size_hint = (1,0.9),
            font_name = self.font_name
        )
        self.add_widget(self.t1)

        #button 1
        self.b1 = Button(
            text='Submit',
            color=(1, 1, 1, 1),
            background_normal='',
            background_color=(0, 0.514, 0.561, 1),
            size_hint=(0.2, 0.5),
            font_size=15,
            font_name='OpenSans-Bold'
        )
        self.add_widget(self.b1)

        #button 2
        self.b2 = Button(
            text='print on',
            color=(1,1,1, 1),
            background_normal='',
            background_color=(0.251, 0.769, 1, 1),
            size_hint=(0.2, 0.5),
            font_size=15,
            font_name = 'OpenSans-Bold',
            on_press = self.print_on

        )
        self.add_widget(self.b2)


        # PopUp 1
        self.pop1 = Popup(
            title='congratulations !',
            size_hint=(0.4, 0.4),
            background_color=(1, 0.922, 0.933, 1),
            content=Label(
                text='ohh ! he is madarchod'
            )
        )

        self.b1.bind(on_press = self.popup_1)

    def print_on(self,obj):
        print("shit it is :" + self.t1.text)

    def popup_1(self,obj):
        box = BoxLayout(orientation='horizontal', padding=(30),pos =(100,100))
        t1 = Label(
            text = 'Submitted Sucessfully',
            font_size = 20,
            font_name = self.font_name
             )
        box.add_widget(t1)
        b1 = Button(text ='close',size_hint =(0.3,0.1),background_normal = '',background_color = (1, 0.922, 0.933, 1),color = (0,0,0,1))
        box.add_widget(b1)
        popup = Popup(title='Congratulations !', title_size= (15),
                  title_align = 'center', content = box,
                  size_hint=(0.5, 0.4),
                  auto_dismiss = True)

        b1.bind(on_press=popup.dismiss)
        popup.open()



class to_do_listApp(App):
    def build(self):
        return myApp()


to_do_listApp().run()
