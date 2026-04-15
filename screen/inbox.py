from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem,TwoLineAvatarListItem, ThreeLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "inbox.kv"))

ALL_USERS = [
    "Catherine",
    "Ryan",
    "Mark"
]
CONVERSATIONS = [
    ("PNG/Users/catherineacc2.png", "Catherine", "Hey! Is this still available?")
]



class InboxManager(ScreenManager):


    def open_chat(self, username: str):
        chat = self.get_screen("chat")
        chat.username = username

        self.transition = SlideTransition(direction = "left")
        self.current = "chat"

    def go_back(self):

        self.transition = SlideTransition(direction="right")
        self.current ="inbox"

class InboxScreen(MDScreen):

    def go_to_new_message(self):
        new_msg = self.manager.get_screen("new_message")
        new_msg.ids.username_input.text = ""
        new_msg.ids.result_list.clear_widgets()

        self.transition = SlideTransition(direction="left")
        self.manager.current = "new_message"

    def on_enter(self):
        self.load_conversations()

    def load_conversations(self):
        inbox_list = self.ids.inbox_list
        inbox_list.clear_widgets()

        for img_path,name,preview in CONVERSATIONS:

            abs_img = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),  # project root
                img_path
            )
            image = ImageLeftWidget(source=abs_img)
            image.size_hint = (None, None)
            image.size = ("60dp", "60dp")
            image.pos_hint = {"center_y": 0.5}

            item = ThreeLineAvatarListItem(
                text=f"   {name}",
                secondary_text = f"      {preview}",
                tertiary_text = " ",
                on_release=lambda x, n=name: self.manager.open_chat(n)
            )
            inbox_list.add_widget(item)
            item.ids._lbl_primary.font_style = "H5"
            item.ids._lbl_secondary.font_size = "12sp"
            item.pos_hint = {"center_y": 0.5}
            item.add_widget(image)


class NewMessageScreen(MDScreen):
    def filter_user(self, query: str):
        results_list = self.ids.results_list
        results_list.clear_widgets()
        if not query.strip():
            return  # show nothing if the search bar is empty

        query_lower = query.lower().strip()

        for username in ALL_USERS:
            if query_lower in username.lower():   # partial match, case-insensitive
                item = OneLineAvatarListItem(
                    text=username,
                    on_release=lambda x, u=username: self.manager.open_chat(u)
                )
                results_list.add_widget(item)

class ChatScreen(MDScreen):

    username = StringProperty("")

    def send_message(self):

        msg_input = self.ids.message_input
        chat_content = self.ids.chat_content
        text      = msg_input.text.strip()

        if not text:
            return

        bubble = OneLineAvatarListItem(
            text=f"You: {text}",
        )

        chat_content.add_widget(bubble)
        msg_input.text = ""


