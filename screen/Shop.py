from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.lang import Builder
import os


Builder.load_file(os.path.join(os.path.dirname(__file__), "Shop.kv"))


class ShopScreen(MDScreen):

    def go_back(self):
        App.get_running_app().home_manager.current = "home_main"

    def go_to_productsinfo(self):
        App.get_running_app().home_manager.current = "productinfo_scr"
