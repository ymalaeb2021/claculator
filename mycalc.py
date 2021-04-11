from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_string('''
<MainWindow1>:
        lbl: in_text
        orientation: "vertical"
        TextInput:
                id: in_text
                halign: "left"
                multiline: False
                font_size:50

        BoxLayout:
                size_hint_y:None
                height: 110
                size_hint_x: 1
                Button:
                        text: "9"
                        font_size: 30
                        on_press: root.on_press_button(1)
                Button:
                        text: "8"
                        font_size: 30
                        on_press: root.on_press_button(2)
                Button:
                        text: "7"
                        font_size: 30
                        on_press: root.on_press_button(3)
                Button:
                        text: "*"
                        font_size: 30
                        on_press: root.on_press_button(4)
        BoxLayout:
                size_hint_y:None
                height: 110
                size_hint_x: 1
                Button:
                        text: "6"
                        font_size: 30
                        on_press: root.on_press_button(5)
                Button:
                        text: "5"
                        font_size: 30
                        on_press: root.on_press_button(6)
                Button:
                        text: "4"
                        font_size: 30
                        on_press: root.on_press_button(7)
                Button:
                        text: "/"
                        font_size: 30
                        on_press: root.on_press_button(8)
        BoxLayout:
                size_hint_y:None
                height: 110
                size_hint_x:None
                size_hint_x: 1
                Button:
                        text: "3"
                        font_size: 30
                        on_press: root.on_press_button(9)
                Button:
                        text: "2"
                        font_size: 30
                        on_press: root.on_press_button(10)
                Button:
                        text: "1"
                        font_size: 30
                        on_press: root.on_press_button(11)
                Button:
                        text: "-"
                        font_size: 30
                        on_press: root.on_press_button(12)
        BoxLayout:
                size_hint_y:None
                height: 110
                font_size: 30
                size_hint_x: 1
                Button:
                        text: "."
                        font_size: 30
                        on_press: root.on_press_button(13)
                Button:
                        text: "0"
                        font_size: 30
                        on_press: root.on_press_button(14)
                Button:
                        font_size: 100
                        background_color:(1, 0,0,1)
                        font_color:(1,.5,.6,0.8)
                        text: "C"

                        on_press: root.on_press_button(15)
                Button:

                        text: "+"
                        font_size: 30
                        on_press: root.on_press_button(16)
        BoxLayout:
                size_hint_y: None
                height: 100
                Button:
                        text: "="
                        font_size: 150
                        size_hint_x: .75
                        on_press: root.on_press_button(17)
                Button:
                        text:"Quit"
                        size_hint_x: .25
                        font_size: 50
                        on_press:root.on_press_button(18)

''')

global nbr
nbr=''
class MainWindow1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        nbr = ''
    def on_press_button(self, index):
        global nbr
        one = ''
        if index == 1:
            self.lbl.text = self.lbl.text + str('9')
            one = '9'
        if index == 2:
            self.lbl.text = self.lbl.text + str('8')
            one = '8'
        if index == 3:
            self.lbl.text = self.lbl.text + str('7')
            one = '7'
        if index == 4:
            self.lbl.text = self.lbl.text + str('*')
            one = '*'
        if index == 5:
            self.lbl.text = self.lbl.text + str('6')
            one = '6'
        if index == 6:
            self.lbl.text = self.lbl.text + str('5')
            one = '5'
        if index == 7:
            self.lbl.text = self.lbl.text + str('4')
            one = '4'
        if index == 8:
            self.lbl.text = self.lbl.text + str('/')
            one = '/'
        if index == 9:
            self.lbl.text = self.lbl.text + str('3')
            one = '3'
        if index == 10:
            self.lbl.text = self.lbl.text + str('2')
            one = '2'
        if index == 11:
            self.lbl.text = self.lbl.text + str('1')
            one = '1'
        if index == 12:
            self.lbl.text = self.lbl.text + str('-')
            one = '-'
        if index == 13:
            self.lbl.text = self.lbl.text + str('.')
            one = '.'
        if index == 14:
            self.lbl.text = self.lbl.text + str('0')
            one = '0'
        if index == 15:
            self.lbl.text = str('')
        if index == 16:
            self.lbl.text = self.lbl.text + str('+')
            one = '+'
        if index == 17 and len(self.lbl.text)>0:
            sum = eval(self.lbl.text)
            self.lbl.text =str(sum)
            print('sum =', sum)
            # self.lbl.text = sum
        if index == 18:
            quit()
        nbrs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if one in nbrs:
            nbr = nbr+one
            print(self.lbl.text , nbr)
            print(eval(self.lbl.text))


class MainApp(App):
    def build(self):
        self.title=("Calculator")

        widget = MainWindow1()

        return widget


if __name__ == '__main__':
    MainApp().run()
