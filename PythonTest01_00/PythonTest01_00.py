

import kivy
import string
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class RootContainer(BoxLayout):
    instance = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootContainer, self).__init__(**kwargs)

    def clickAction1(self, instance):
        #identify the button pressed
        buttonText = instance.text

        
        self.lbl1.text = instance.text + " some text goes here ... "
        myresult = " this is scrolling text.\n " * 30
        self.lbl5.text = myresult
    
class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()
