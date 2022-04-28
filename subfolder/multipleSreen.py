from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 

#Define our different screens
class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

# Designate Our .kv design file 
kv = Builder.load_string("""
WindowManager:
	FirstWindow:
	SecondWindow:


<FirstWindow>:
	name: "first"

	BoxLayout:
		orientation: "vertical"
		size: root.width, root.height

		Label:
			text: "First Screen"
			font_size: 32

		Button:
			text: "Next Screen"
			font_size: 32
			on_release: 
				app.root.current = "second"
				root.manager.transition.direction = "left"


<SecondWindow>:
	name: "second"

	BoxLayout:
		orientation: "vertical"
		size: root.width, root.height

		Label:
			text: "Second Screen"
			font_size: 32

		Button:
			text: "Go Back"
			font_size: 32
			on_release: 
				app.root.current = "first"
				root.manager.transition.direction = "right"
""")


class AwesomeApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	AwesomeApp().run()