from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.lang import Builder
import os


Builder.load_file(os.path.join(os.path.dirname(__file__), "productsinfo.kv"))


class ProductsInfoScreen(MDScreen):
    def go_back(self):
        app = App.get_running_app()
        print("SCREENS:", app.home_manager.screen_names)
        app.home_manager.current = "shop_scr"
