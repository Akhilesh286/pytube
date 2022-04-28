from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import ScreenManager, Screen

from sqldb import dataBase


# multiple screen

#Define our different screens
class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass


# Database created 
db = dataBase("bd.sqlite")

colam = "on_off integer"
# table created  
db.create_table('on_off',colam)
# chacking table has any value 
select_all = db.select_all("on_off")
# print (select_all)
# print (type (select_all))
# print (len(select_all))
if len(select_all) == 0:
    val = {"on_off":0}
    col = "(:on_off)"
    db.insert_table('on_off',val,col)
# cheaking switch on or off

class ContentNavigationDrawer(MDBoxLayout):
    switchCheaking = False
    if select_all[0][0] == True:
        switchCheaking = True
    def switchActive (self):
        onOFF = self.ids.darkSwitch.active
        if onOFF == False:
            self.ids.darkSwitch.active = True
        else:
            self.ids.darkSwitch.active = False
        # print(switchObject)
    

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class pytubeApp(MDApp):
    def build(self):
        print (select_all)
        print (type(select_all[0][0]))
        if (select_all[0][0] == 1):
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


        # run kv file
        return Builder.load_file("main.kv")


    def on_start(self):
        pass
        # icons_item = {
        #     "folder": "My files",
        #     "account-multiple": "Shared with me",
        #     "star": "Starred",
        #     "history": "Recent",
        #     "checkbox-marked": "Shared with me",
        #     "upload": "Upload",
        # }
        # for icon_name in icons_item.keys():
        #     self.root.ids.content_drawer.ids.md_list.add_widget(
        #         ItemDrawer(icon=icon_name, text=icons_item[icon_name])
        #     )

    def press (self):
        pass

    def switch_click (self,switchObject,switchValue):
        if  switchValue == True:
            self.theme_cls.theme_style = "Dark"
            print("sneha")
            db.update(table="on_off",SET="on_off = 1",where="on_off = 0")
        else:
            self.theme_cls.theme_style = "Light"
            db.update(table="on_off",SET="on_off = 0",where="on_off = 1")



pytubeApp().run()