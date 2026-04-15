from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "account.kv"))


class AccountScreen(MDScreen):
    def back_to_home(self):
        App.get_running_app().switch_tab("home")

    def go_to_addnewproduct(self):
        App.get_running_app().home_manager.current = "newproduct_scr"
