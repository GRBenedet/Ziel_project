from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from plyer import gps
from geopy.geocoders import Nominatim


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
    
    def get_location(self, instance):
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            gps.start()
        except NotImplementedError:
            self.root.ids.location_label.text = "GPS não suportado neste dispositivo"
    
    def on_location(self, **kwargs):
        self.root.ids.location_label.text = f"Latitude: {kwargs['lat']}, Longitude: {kwargs['lon']}"
        gps.stop()
    
    def on_status(self, stype, status):
        self.root.ids.location_label.text = f"Status do GPS: {status}"

    def corvert(self):
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.geocode(self.root.ids.location_label.text)
        self.root.ids.endereco_label.text = f"{self.root.ids.location_label.text}"

if __name__ == '__main__':
    HomeApp().run()