from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.webview import WebView

class WebSDR_App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.webview = WebView(url='http://websdr.ewi.utwente.nl:8901/')
        layout.add_widget(self.webview)
        botones = BoxLayout(size_hint=(1, 0.08))
        btn_recargar = Button(text='Recargar')
        btn_recargar.bind(on_press=lambda x: self.webview.reload())
        botones.add_widget(btn_recargar)
        btn_home = Button(text='Home')
        btn_home.bind(on_press=lambda x: setattr(self.webview, 'url', 'http://websdr.ewi.utwente.nl:8901/'))
        botones.add_widget(btn_home)
        layout.add_widget(botones)
        return layout
WebSDR_App().run()
