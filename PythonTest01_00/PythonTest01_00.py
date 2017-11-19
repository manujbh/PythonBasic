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

NUMBER_OF_BUTTONS = 5

class RootContainer(BoxLayout):
    instance = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootContainer, self).__init__(**kwargs)

    def clickAction1(self, instance):
        #identify the button pressed
        self.lbl1.text = instance.text + " some text goes here ... "
        #self.lbl2.text = " this is scrolling text.\n " * 30
        self.lbl3.bind(minimum_height=self.lbl3.setter('height'))
        x=0
        while x < 4:
            self.lbl3.add_widget(Button(text="B0" + str(x)))
            x = x + 1

    
class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()
