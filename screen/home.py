from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.app import App
from screen.RFQ import RFQScreen
from screen.BuyOffers import  BuyOffersScreen

import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "home.kv"))


class HomeScreen(MDScreen):

    def go_to_rfq(self):
        App.get_running_app().home_manager.current = "rfq_scr"

    def go_to_buyoffers(self):
        App.get_running_app().home_manager.current = "buyoffers_scr"

    def go_to_communitychat(self):
        App.get_running_app().home_manager.current = "cmc_scr"

    def go_to_shop(self):
        App.get_running_app().home_manager.current = "shop_scr"

    def go_to_productsinfo(self):
        App.get_running_app().home_manager.current = "productinfo_scr"

    def go_to_account(self):
        App.get_running_app().home_manager.current = "account_scr"

    def go_to_newquestion(self):
        App.get_running_app().home_manager.current = "newquestion_scr"


