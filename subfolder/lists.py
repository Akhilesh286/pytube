from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

KV = """
ScrollView:

    MDList:
        id: container
        OneLineListItem:
            text:"hello"
            MDSwitch:
                pos_hint:{"center_x":.9,"center_y":.5}

"""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # def on_start(self):
    #     for i in range(20):
    #         self.root.ids.container.add_widget(
    #             OneLineListItem(text=f"Single-line item {i}")
    #         )


Example().run()
