from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem,TwoLineAvatarListItem, ThreeLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

from kivymd.uix.menu import MDDropdownMenu

Builder.load_file(os.path.join(os.path.dirname(__file__), "rfq.kv"))


class RFQScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu = None

    def open_menu(self):
        menu_items = [
            {"text": "Abaca", "on_release": lambda x="Abaca": self.set_item(x)},
            {"text": "Accessories", "on_release": lambda x="Accessories": self.set_item(x)},
            {"text": "Bags", "on_release": lambda x="Bags": self.set_item(x)},
            {"text": "Furniture", "on_release": lambda x="Furniture": self.set_item(x)},
            {"text": "Gears", "on_release": lambda x="Gears": self.set_item(x)},
            {"text": "Handicrafts", "on_release": lambda x="Handicrafts": self.set_item(x)},
            {"text": "Shoes and Slippers", "on_release": lambda x="Shoes and Slippers": self.set_item(x)},
            {"text": "Textile", "on_release": lambda x="Textile": self.set_item(x)},

        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.select_category_field,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def set_item(self, text):
        self.ids.select_category_field.text = text
        self.menu.dismiss()

    def go_back(self):
        App.get_running_app().home_manager.current = "home_main"




