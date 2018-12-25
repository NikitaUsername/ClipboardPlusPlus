import sublime, sublime_plugin
import json
import os


class ClipboardCopyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		history_path = os.path.expanduser('~/.config/sublime-text-3/Packages/ClipboardPlusPlus/hist.json')
		html_path = os.path.expanduser('~/.config/sublime-text-3/Packages/ClipboardPlusPlus/popup-window.html')

		self.view.run_command('copy')
		data = self.get_data(history_path)
		self.set_data(data, history_path)
		self.set_html_file(html_path, history_path)

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

		html = []
		with open(html_path, 'r') as f:
		    html = f.read().splitlines()

		with open(html_path, 'w') as f:
		    for i  in self.add_to_html(html, history_path):
		    	f.write(i + '\n')


	def add_to_html(self, html, history_path):

		data = self.get_data(history_path)

		for i in range(32, 10, -4):
			html[i + 4] = html[i]

		short_text = ""

		for i in data["clipboardHistory"][data["index"]]["content"][:13]:
			if i is "<":
				short_text +="〈"
				continue
			elif i is ">":
				short_text +="〉"
				continue
			elif i is not "\n":
				short_text +=i
			else:
				short_text +="\t"

		html[12] = html[8]
		html_str = html[8][:13] + str(data["index"]) + html[8][14:23] + "\"other\">" + short_text + html[8][-4:]
		html[8] = html_str
		return html





