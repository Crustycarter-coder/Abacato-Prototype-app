from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "categories.kv"))


CATEGORIES_DATA = [
    ("Abaca",             "ICONS/Categories/abaca category icon.png"),
    ("Accessories",       "ICONS/Categories/accessories icon.png"),
    ("Bags",              "ICONS/Categories/bags icon.png"),
    ("Furniture",         "ICONS/Categories/furniture icon.png"),
    ("Gears",             "ICONS/Categories/gears icon.png"),
    ("Handicrafts",       "ICONS/Categories/handicrafts icon.png"),
    ("Shoes and Slippers",   "ICONS/Categories/slippers icon.png"),
    ("Textile",           "ICONS/Categories/Textile and fashion icon.png"),
]

CATEGORY_PRODUCTS = {
    "Abaca":            ["Abaca Rope", "Abaca Fabric"],
    "Accessories":      ["Bracelet", "Necklace"],
    "Bags":             ["Tote Bag", "Backpack"],
    "Furniture":        ["Chair", "Table"],
    "Gears":            ["Gear Set A", "Gear Set B"],
    "Handicrafts":      ["Wooden Craft", "Woven Craft"],
    "Shoes and Slippers": ["Sandals", "Slippers"],
    "Textile":          ["Cotton Fabric", "Woven Textile"],
}



class CategoriesScreen(MDScreen):

    def load_categories(self):
        list_view = self.ids.list_view
        list_view.clear_widgets()  # prevent duplicates on re-entry

        for label, img_path in CATEGORIES_DATA:
            # Build absolute path from project root
            abs_img = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),  # project root
                img_path
            )

            item = ThreeLineAvatarListItem(
                text=f"       {label}",
                tertiary_text=" ",
                on_release=lambda x, t=label: self.open_products(t),
            )
            item.ids._lbl_primary.font_size = "18sp"

            image = ImageLeftWidget(source=abs_img)
            image.size_hint = (None, None)
            image.size = ("80dp", "80dp")
            image.pos_hint = {"center_y": 0.5}
            item.add_widget(image)

            list_view.add_widget(item)

    def open_products(self, category_name):
        App.get_running_app().open_products(category_name)


class ProductsScreen(MDScreen):
    category_name = ""

    def load_products(self, category_name):
        products_list = self.ids.products_list
        products_list.clear_widgets()

        for product in CATEGORY_PRODUCTS.get(category_name, []):
            item = ThreeLineAvatarListItem(
                text=product,
                secondary_text=" ",
                tertiary_text=" ",
            )
            products_list.add_widget(item)