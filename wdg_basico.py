from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='amo ds, josi o melhor prof', font_size=70)

if __name__ == '__main__':
    MyApp().run()