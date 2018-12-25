import sublime, sublime_plugin
import json
import os
from sys import platform

class ClipboardPasteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		content = self.get_popup_content()
		self.view.show_popup(content, sublime.HTML, location=-1, max_height=640, on_navigate=self.on_choice_textbox)

	def get_popup_content(self):
		resources = sublime.find_resources('popup-window.html')
		content = sublime.load_resource(resources[0])
		return content

	def on_choice_textbox(self, symbol):
		history_path = ""
		if platform == "linux" or platform == "linux2" or platform == "darwin":
		    history_path = os.path.expanduser('~/.config/sublime-text-3/Packages/ClipboardPlusPlus/hist.json')
		else :
		    history_path = os.path.expanduser('~\\AppData\\Roaming\\Sublime Text 3\\Packages\\ClipboardPlusPlus\\hist.json')
		with open(history_path, 'r') as f:
		    data = json.loads(f.read())

		self.view.run_command("insert", {"characters": data["clipboardHistory"][int(symbol)]["content"]})
		self.view.hide_popup()