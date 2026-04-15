from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from screen.home import HomeScreen
from screen.categories import CategoriesScreen, ProductsScreen
from screen.inbox import InboxScreen, NewMessageScreen, ChatScreen, InboxManager
from screen.RFQ import RFQScreen
from screen.BuyOffers import BuyOffersScreen
from screen.Shop import ShopScreen
from screen.Communitychat import CommunityChatScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from screen.ProductsInfo.ProductInfo import ProductsInfoScreen
from screen.Account import AccountScreen
from screen.newquestion import NewQuestionScreen
from screen.Supplier.Addnewproduct import AddNewProductScreen

Window.size = (390, 844)

KV = """


MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDBottomNavigation:
            id: bottom_nav

            MDBottomNavigationItem:
                id: home_tab
                name: "home"
                text: "Home"
                icon: "home"


            MDBottomNavigationItem:
                id: categories_tab
                name: "categories"
                text: "Categories"
                icon: "view-grid"

            MDBottomNavigationItem:
                id: inbox_tab
                name: "inbox"
                text: "Inbox"
                icon: "inbox"

            MDBottomNavigationItem:
                name: "settings"
                text: "Settings"
                icon: "cog"
                MDBoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "Settings"
                    MDLabel:
                        text: "Settings Screen"
                        halign: "center"
"""


class MyKivyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = 'Light'
        self.root = Builder.load_string(KV)

        self.home_manager = ScreenManager()
        self.home_manager.add_widget(HomeScreen(name="home_main"))
        self.home_manager.add_widget(RFQScreen(name="rfq_scr"))
        self.home_manager.add_widget(BuyOffersScreen(name="buyoffers_scr"))
        self.home_manager.add_widget(CommunityChatScreen(name="cmc_scr"))
        self.home_manager.add_widget(ShopScreen(name="shop_scr"))
        self.home_manager.add_widget(ProductsInfoScreen(name="productinfo_scr"))
        self.home_manager.add_widget(AccountScreen(name="account_scr"))
        self.home_manager.add_widget(NewQuestionScreen(name="newquestion_scr"))
        self.home_manager.add_widget(AddNewProductScreen(name="newproduct_scr"))
        self.home_manager.current = "home_main"
        home_tab = self.root.ids.home_tab
        home_tab.add_widget(self.home_manager)
        self.cat_manager = ScreenManager()
        self.categories_screen = CategoriesScreen(name="cat_main")
        self.products_screen = ProductsScreen(name="cat_products")

        self.cat_manager.add_widget(self.categories_screen)
        self.cat_manager.add_widget(self.products_screen)


        categories_tab = self.root.ids.categories_tab
        categories_tab.add_widget(self.cat_manager)

        self.categories_screen.load_categories()

        self.inbox_manager = InboxManager()

        self.inbox_manager.add_widget(InboxScreen(name="inbox"))
        self.inbox_manager.add_widget(NewMessageScreen(name="new_message"))
        self.inbox_manager.add_widget(ChatScreen(name="chat"))

        self.inbox_manager.current = "inbox"
        self.root.ids.inbox_tab.add_widget(self.inbox_manager)

    def open_details(self, data):

        info_screen = self.home_manager.get_screen('product_info')
        info_screen.product_data = data
        self.home_manager.current = 'product_info'

    def switch_tab(self, tab_name: str):
        self.root.ids.bottom_nav.switch_tab(tab_name)

    def open_products(self, category_name):
        self.products_screen.category_name = category_name
        self.products_screen.load_products(category_name)
        self.cat_manager.current = "cat_products"

    def go_back(self):
        self.cat_manager.current = "cat_main"
        self.home_manager.current = "home_main"


    def go_to_profile(self):

        print("Open profile")


if __name__ == '__main__':
    Window.size = (390, 844)
    MyKivyApp().run()