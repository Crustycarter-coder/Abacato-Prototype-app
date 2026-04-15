from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os
import db.database  # Import our database file

Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))


class LoginScreen(MDScreen):

    def login_btn(self):
        username = self.ids.user_input.text
        password = self.ids.pass_input.text

        # Check the database
        if db.database.verify_login(username, password):
            print("Login Successful!")
            self.manager.current = "main_app_screen"
        else:
            print("Invalid credentials")

    def register_btn(self):
        username = self.ids.user_input.text
        password = self.ids.pass_input.text

        if db.database.register_user(username, password):
            print("Registration Successful! You can now log in.")
        else:
            print("Username already taken.")