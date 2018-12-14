import sublime, sublime_plugin
import json


class ClipboardCopyCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		history_path = '/home/denis/.config/sublime-text-3/Packages/ClipboardPlusPlus/hist.json'
		html_path = '/home/denis/.config/sublime-text-3/Packages/ClipboardPlusPlus/popup-window.html'

		self.view.run_command('copy')
		data = self.get_data(history_path)
		self.set_data(data, history_path)
		self.set_html_file(html_path, history_path)
		##self.view.insert(edit, 0, data["clipboardHistory"][data["index"]]["content"])

	def get_data(self, history_path):
		with open(history_path, 'r') as f:
		    data = json.loads(f.read())
		return data

	def set_data(self, data, history_path):
		if data["index"] is not 7:
			data["index"] += 1
		else:
			data["index"] = 0

		data["clipboardHistory"][data["index"]]["content"] = sublime.get_clipboard()

		with open(history_path, 'w') as f:
		    f.write(json.dumps(data))

	def set_html_file(self, html_path, history_path):
		
		cl = sublime.get_clipboard()

		html = []
		with open(html_path, 'r') as f:
		    html = f.read().splitlines()

		with open(html_path, 'w') as f:
		    for i  in self.add_to_html(html):
		    	f.write(i + '\n')


	def add_to_html(self, html):

		for i in range(32, 10, -4):
			html[i + 4] = html[i]

		return html





