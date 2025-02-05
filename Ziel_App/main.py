from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from plyer import gps
from geopy.geocoders import Nominatim


class Ruido_Ambiental_Window(Screen):

    def on_tipo_ruido(self, instance):

        for btn in self.ids.toggle_group.children:
            btn.background_color = (1, 1, 1, 1)  # Branco (RGBA)
        
        # Muda a cor da opção selecionada
        instance.background_color = (0, 1, 0, 1)  # Verde (RGBA)
        print(f"Selecionado: {instance.text}")


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
    
    def get_location(self):
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            gps.start()
        except NotImplementedError:
            screen = self.root.get_screen("Ruido_Ambiental")
            screen.ids["location_label"].text = "GPS não suportado neste dispositivo"
    
    def on_location(self, **kwargs):
        """Este método será chamado quando a localização for encontrada"""
        lat = kwargs.get("lat", "N/A")  # Obtém latitude (ou "N/A" se não existir)
        lon = kwargs.get("lon", "N/A")  # Obtém longitude (ou "N/A" se não existir)
        screen = self.root.get_screen("Ruido_Ambiental")
        screen.ids["location_label"].text = f"Latitude: {lat}, Longitude: {lon}"
        gps.stop()
    
    def on_status(self, stype, status):
        screen = self.root.get_screen("Ruido_Ambiental")
        screen.ids["location_label"].text = f"Status do GPS: {status}"

    def corvert(self):
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.geocode(self.root.ids["location_label"].text)
        screen = self.root.get_screen("Ruido_Ambiental")
        screen.ids["endereco_label"].text = f"{screen.ids["location_label"].text}"

if __name__ == '__main__':
    HomeApp().run()