from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem,TwoLineAvatarListItem, ThreeLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "communitychat.kv"))

class CommunityChatScreen(MDScreen):

    def go_back(self):
        App.get_running_app().home_manager.current = "home_main"

    def go_to_newquestion(self):
        App.get_running_app().home_manager.current = "newquestion_scr"

    def go_to_new_question(self):
        pass