import sublime, sublime_plugin


class ClipboardPasteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		content = self.get_characters_html()
		self.view.show_popup(content, sublime.HTML, location=-1, max_height=640, on_navigate=self.on_choice_symbol)

	def get_characters_html(self):
		resources = sublime.find_resources('popup-window.html')
		content = sublime.load_resource(resources[0])
		return content

	def on_choice_symbol(self, symbol):
		self.view.run_command("insert", {"characters": symbol})
		self.view.hide_popup()