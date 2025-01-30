from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Ruido_Ambiental_Window(FloatLayout):
    pass


class HomeApp(App):
    def build(self):
        return Ruido_Ambiental_Window()

if __name__ == '__main__':
    HomeApp().run()