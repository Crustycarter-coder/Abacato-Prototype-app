from kivy.clock import Clock
from kivy.properties import DictProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
import os


from db.database import db

# Screen name constants
LOGIN_SCR        = "log_in_scr"
REGISTER_SCR     = "register_scr"
USER_MANAGER_SCR = "user_manager_scr"
MAIN_SCR         = "main"


def show_snackbar(message: str):
    """KivyMD 1.2.0 snackbar fix"""
    Snackbar(
        text=message,
        snackbar_x="10dp",
        snackbar_y="10dp",
        size_hint_x=0.9,
        duration=2,
    ).open()


# ── Screen 1: UserManagerScreen ─────────────────────────────────────────────
class UserManagerScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None
        self.bind(on_kv_post=self.on_kv_ready)

    def on_kv_ready(self, *args):
        """Ensure KV is fully loaded before accessing ids"""
        self.sm = self.ids.get("signin_signup_manager")

    def switch_scr(self, *args):
        tab_text = args[3]

        if tab_text.lower() == "log in":
            self.sm.current = "log_in_scr"
        else:
            self.sm.current = "register_scr"

# ── Screen 2: LoginScr ───────────────────────────────────────────────────────
class LoginScr(MDScreen):
    user_data = DictProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.enter_user = None
        self.enter_pass = None
        self.bind(on_kv_post=self.on_kv_ready)

    def on_kv_ready(self, *args):
        self.enter_user = self.ids.get("enter_user")
        self.enter_pass = self.ids.get("enter_pass")

    def perform_login(self):
        if not self.enter_user or not self.enter_pass:
            return

        username = self.enter_user.text.strip()
        password = self.enter_pass.text.strip()

        if not username or not password:
            show_snackbar("Please fill in all fields")
            return

        user_data = db.get_login_user(username, password)

        if not user_data:
            show_snackbar("Invalid username or password")

            if self.enter_user:
                self.enter_user.error = True
            if self.enter_pass:
                self.enter_pass.error = True
            return

        self.app.set_app_user(user_data)
        self.app.go_to_main()


# ── Screen 3: RegisterScr ───────────────────────────────────────────────────
class RegisterScr(MDScreen):
    user_data = DictProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

        self.created_user = None
        self.created_email = None
        self.created_pass = None
        self.created_dob = None

        self.bind(on_kv_post=self.on_kv_ready)

    def on_kv_ready(self, *args):
        self.created_user  = self.ids.get("create_user")
        self.created_email = self.ids.get("create_email")
        self.created_pass  = self.ids.get("pswd")
        self.created_dob   = self.ids.get("dob")

    def perform_register(self):
        if not all([self.created_user, self.created_email, self.created_pass]):
            return

        username = self.created_user.text.strip()
        email    = self.created_email.text.strip()
        password = self.created_pass.text.strip()
        confirm  = self.ids.get("cmpswd").text.strip()

        if not all([username, email, password, confirm]):
            show_snackbar("Please fill in all fields")
            return

        if password != confirm:
            show_snackbar("Passwords do not match")
            self.created_pass.error = True
            self.ids.cmpswd.error = True
            return

        user_data = db.add_user(username, email, password)

        if not user_data:
            show_snackbar("Username or email already exists")
            return

        self.app.set_app_user(user_data)
        self.app.go_to_main()

