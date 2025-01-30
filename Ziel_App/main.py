from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


class Ruido_Ambiental_Window(Screen):
    pass

class Home_Window(Screen):
    pass

class HomeApp(App):
    def build(self):

        Builder.load_file("Home.kv")
        Builder.load_file("Ruido_Ambiental.kv")

        sm = ScreenManager()
        sm.add_widget(Home_Window(name="Home"))
        sm.add_widget(Ruido_Ambiental_Window(name="Ruido_Ambiental"))
        return sm
    
    def animar_cor(self, widget, nova_cor):
        anim = Animation(background_color=nova_cor, duration=0.01)
        anim.start(widget)

if __name__ == '__main__':
    HomeApp().run()